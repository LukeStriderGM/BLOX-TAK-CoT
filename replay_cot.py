import CoT  # https://pypi.org/project/PyCoT
import socket
import ssl
import os
import logging
import datetime
import time
import re
import warnings
from dateutil.parser import parse as parse_date

# --- CONFIGURATION OF WARNINGS ---
# --- KONFIGURACJA OSTRZEŻEŃ ---

# Disable annoying library warnings
# Wyłącz irytujące ostrzeżenia biblioteki
warnings.filterwarnings("ignore")

# --- LOGGING CONFIGURATION ---
# --- KONFIGURACJA LOGOWANIA ---

# Configure logging for the replayer itself
# Konfiguracja logowania dla samego odtwarzacza
logging.basicConfig(
    filename="cot_replay.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- TAK SERVER SETTINGS ---
# --- USTAWIENIA SERWERA TAK ---

# IP address and port (Matches your main script)
# Adres IP i port (Zgodne z głównym skryptem)
TAK_IP = "192.168.1.2"
TAK_PORT = 8089

# --- SSL CERTIFICATES ---
# --- CERTYFIKATY SSL ---

# Define paths to certificates (OrangePi Paths)
# Zdefiniuj ścieżki do certyfikatów (Ścieżki OrangePi)
CERT_DIR = "/home/lukestridergm/BLOX-TAK-CoT/certs"
CLIENT_CERT = os.path.join(CERT_DIR, "BLOX-TAK-SF-ADMIN.pem")
CLIENT_KEY = os.path.join(CERT_DIR, "BLOX-TAK-SF-ADMIN.key")
CA_CERT = os.path.join(CERT_DIR, "BLOX-TAK-SF-ADMIN-trusted.pem")

# --- SSL CONTEXT PREPARATION ---
# --- PRZYGOTOWANIE KONTEKSTU SSL ---

# Load client and CA certificates
# Załaduj certyfikaty klienta i CA
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_cert_chain(certfile=CLIENT_CERT, keyfile=CLIENT_KEY)
ssl_context.load_verify_locations(cafile=CA_CERT)
ssl_context.verify_mode = ssl.CERT_REQUIRED

# --- REPLAY SETTINGS ---
# --- USTAWIENIA ODTWARZANIA ---

# Path to the input log file (Where the main script writes)
# Ścieżka do pliku logów wejściowych (Gdzie zapisuje główny skrypt)
LOG_FILE = "/home/lukestridergm/BLOX-TAK-CoT/cot.log"

# Target Identity for Replay
# Tożsamość celu dla odtwarzania
SAT_ID = 66877  # ZQ-3 R/B
SAT_NAME = "ZQ-3 R/B (REPLAY)"
REFRESH_INTERVAL = 1.0  # Speed of replay (1.0 = Realtime)


def parse_log_for_positions(start_time, end_time):
    """
    Parse the log file for CoT position entries within the given time range.
    Parsuj plik logów w poszukiwaniu pozycji CoT w zadanym zakresie czasu.
    """
    positions = []

    # Regex matching the FIXED logging format: "lat=50.1 lon=15.2 alt=60000.0"
    # Regex pasujący do NAPRAWIONEGO formatu logowania
    regex_standard = re.compile(
        r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}).*lat=(-?\d+\.\d+).*lon=(-?\d+\.\d+).*alt=(-?\d+\.?\d*)"
    )

    try:
        with open(LOG_FILE, "r") as file:
            for line in file:
                match = regex_standard.search(line)
                if match:
                    timestamp_str, lat, lon, alt = match.groups()
                    try:
                        timestamp = parse_date(timestamp_str)
                        # Filter by time range
                        if start_time <= timestamp <= end_time:
                            positions.append((timestamp, float(lat), float(lon), float(alt)))
                    except Exception:
                        continue
    except FileNotFoundError:
        print(f"❌ Error: Log file not found: {LOG_FILE}")
        print(f"❌ Błąd: Nie znaleziono pliku logów: {LOG_FILE}")
        return []
    except Exception as e:
        print(f"❌ Error parsing log file: {e}")
        print(f"❌ Błąd parsowania pliku logów: {e}")
        return []

    return positions


def send_cot_to_tak(lat, lon, alt, timestamp):
    """
    Send a CoT message to the TAK server via SSL.
    Wyślij wiadomość CoT do serwera TAK przez SSL.
    """
    try:
        # Establish SSL connection
        # Nawiąż połączenie SSL
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        wrapped_sock = ssl_context.wrap_socket(sock, server_hostname=TAK_IP)
        wrapped_sock.connect((TAK_IP, TAK_PORT))
        wrapped_sock.settimeout(2.0)

        # Create CoT event
        # Stwórz zdarzenie CoT

        # CoT types: https://github.com/wcrum/py-cot/blob/main/CoT/types.py
        stale = timestamp + datetime.timedelta(minutes=5)
        cot_event = CoT.Event(
            version="2.0",
            type="a-h-P-S",  # Hostile Space Satellite
            uid=f"SAT.{SAT_ID}.REPLAY",  # Unique ID for replay so it doesn't conflict
            time=timestamp,
            start=timestamp,
            stale=stale,
            how="m-g",
            point=CoT.Point(
                lat=lat,
                lon=lon,
                hae=alt,
                ce=9999999,
                le=9999999
            ),
            detail={
                "contact": {"callsign": SAT_NAME},
                "remarks": "REPLAY MODE - SIMULATION"
            }
        )

        # Send CoT message
        # Wyślij wiadomość CoT
        wrapped_sock.sendall(bytes(cot_event.xml(), encoding="utf-8"))

        # Log and print position (IDENTICAL FORMAT TO MAIN SCRIPT)
        # Loguj i wypisz pozycję (FORMAT IDENTYCZNY JAK W GŁÓWNYM SKRYPCIE)
        print(
            f"📡 REPLAY: {timestamp.strftime('%H:%M:%S')} | ALT: {alt:>8.0f} m | LAT: {lat:>7.2f} | LON: {lon:>8.2f} | 🔴 HOSTILE")
        print(
            f"📡 ODTW.:  {timestamp.strftime('%H:%M:%S')} | WYS: {alt:>8.0f} m | SZER:{lat:>7.2f} | DŁU: {lon:>8.2f} | 🔴 WROGI")

        logging.info(f"Replayed CoT: lat={lat}, lon={lon}, alt={alt}")

        # Clear buffer (Receive confirmation)
        # Wyczyść bufor (Odbierz potwierdzenie)
        try:
            _ = wrapped_sock.recv(1024)
        except socket.timeout:
            pass

        wrapped_sock.close()
        return True

    except (ConnectionRefusedError, ssl.SSLError) as e:
        print(f"❌ SSL Error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    # User Interface
    # Interfejs Użytkownika
    print(f"🎞️  CoT REPLAYER STARTING")
    print(f"🎞️  URUCHAMIANIE ODTWARZACZA CoT")
    print(f"📂 Reading from: {LOG_FILE}")
    print(f"📂 Odczyt z: {LOG_FILE}")
    print("-" * 40)

    print("Enter time range (YYYY-MM-DD HH:MM:SS)")
    print("Wprowadź zakres czasu (RRRR-MM-DD GG:MM:SS)")
    print("Example/Przykład: 2026-01-31 03:41:00")

    try:
        start_time_str = input("Start: ")
        end_time_str = input("End/Koniec: ")

        start_time = parse_date(start_time_str)
        end_time = parse_date(end_time_str)

        if start_time >= end_time:
            print("❌ Start time must be before end time.")
            return

        # Parse log file
        # Parsuj plik logów
        print(f"🔄 Scanning log file...")
        positions = parse_log_for_positions(start_time, end_time)

        if not positions:
            print("⚠️ No positions found. Check if cot.log has data with 'lat=' and 'lon='.")
            print("⚠️ Nie znaleziono pozycji. Sprawdź czy cot.log ma dane z 'lat=' i 'lon='.")
            return

        print(f"✅ Found {len(positions)} frames. Starting Replay...")
        time.sleep(1)

        # Replay Loop
        # Pętla Odtwarzania
        for timestamp, lat, lon, alt in positions:
            if send_cot_to_tak(lat, lon, alt, timestamp):
                time.sleep(REFRESH_INTERVAL)
            else:
                print("⚠️ Skipped frame.")

    except ValueError as e:
        print(f"❌ Invalid date format: {e}")
    except Exception as e:
        print(f"❌ Critical Error: {e}")


if __name__ == "__main__":
    main()