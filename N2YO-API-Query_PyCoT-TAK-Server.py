import CoT  # https://pypi.org/project/PyCoT
import requests
import datetime
import socket
import ssl
import time
import os
import logging
import warnings

# --- CONFIGURATION OF WARNINGS ---
# --- KONFIGURACJA OSTRZEŻEŃ ---

# Disable annoying library warnings about date format for cleaner logs
# Wyłącz irytujące ostrzeżenia biblioteki o formacie daty dla czystszych logów
warnings.filterwarnings("ignore")

# --- LOGGING CONFIGURATION ---
# --- KONFIGURACJA LOGOWANIA ---

# Configure file logging
# Konfiguracja logowania do pliku
logging.basicConfig(
    filename="/home/lukestridergm/BLOX-TAK-CoT/cot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# --- USER SETTINGS ---
# --- USTAWIENIA UŻYTKOWNIKA ---

# API Key and Target Satellite ID (ZQ-3 R/B)
# Klucz API i ID docelowego satelity (ZQ-3 R/B)
N2YO_API_KEY = "*****"
SAT_ID = 66877

# Observer coordinates (Your Location)
# Koordynaty obserwatora (Twoja Lokalizacja)
OBSERVER_LAT = 50.81557
OBSERVER_LNG = 15.675225
OBSERVER_ALT = 445

# Prediction settings
# Ustawienia predykcji
SECONDS = 1
REFRESH_INTERVAL = 10

# --- TAK SERVER SETTINGS ---
# --- USTAWIENIA SERWERA TAK ---

# IP address and port
# Adres IP i port
TAK_IP = "192.168.1.2"
TAK_PORT = 8089

# --- SSL CERTIFICATES ---
# --- CERTYFIKATY SSL ---

# Define paths to certificates
# Zdefiniuj ścieżki do certyfikatów
CERT_DIR = "/home/lukestridergm/BLOX-TAK-CoT/certs"
CLIENT_CERT = os.path.join(CERT_DIR, "BLOX-TAK-SF-ADMIN.pem")
CLIENT_KEY = os.path.join(CERT_DIR, "BLOX-TAK-SF-ADMIN.key")
CA_CERT = os.path.join(CERT_DIR, "BLOX-TAK-SF-ADMIN-trusted.pem")

# --- SSL CONTEXT PREPARATION ---
# --- PRZYGOTOWANIE KONTEKSTU SSL ---

# Load client and CA certificates for secure connection
# Załaduj certyfikaty klienta i CA dla bezpiecznego połączenia
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
ssl_context.load_cert_chain(certfile=CLIENT_CERT, keyfile=CLIENT_KEY)
ssl_context.load_verify_locations(cafile=CA_CERT)
ssl_context.verify_mode = ssl.CERT_REQUIRED

# Print startup information
# Wypisz informacje startowe
print(f"🚀 STARTING TRACKING: {SAT_ID}")
print(f"🚀 ROZPOCZYNAM ŚLEDZENIE: {SAT_ID}")

print(f"🎯 TARGET: {TAK_IP}:{TAK_PORT} (SSL)")
print(f"🎯 CEL: {TAK_IP}:{TAK_PORT} (SSL)")

print(f"⚠️ MODE: HOSTILE (IMMINENT IMPACT)")
print(f"⚠️ TRYB: WROGI (NADCHODZĄCE UDERZENIE)")
print("-" * 40)

# --- MAIN LOOP ---
# --- GŁÓWNA PĘTLA ---

while True:
    try:
        # 1. Fetch data from N2YO
        # 1. Pobierz dane z N2YO

        # Measure query start time
        # Zmierz czas rozpoczęcia zapytania
        start_time = time.time()
        url = f"https://api.n2yo.com/rest/v1/satellite/positions/{SAT_ID}/{OBSERVER_LAT}/{OBSERVER_LNG}/{OBSERVER_ALT}/{SECONDS}/&apiKey={N2YO_API_KEY}"

        try:
            # Send GET request with timeout
            # Wyślij żądanie GET z timeoutem
            response = requests.get(url, timeout=10)
        except requests.RequestException as e:
            # Handle connection error
            # Obsłuż błąd połączenia
            print(f"❌ N2YO Connection Error: {e}")
            print(f"❌ Błąd połączenia z N2YO: {e}")
            time.sleep(30)
            continue

        # Check API response status
        # Sprawdź status odpowiedzi API
        if response.status_code != 200:
            print(f"❌ N2YO API Error: {response.status_code}")
            print(f"❌ Błąd API N2YO: {response.status_code}")
            time.sleep(60)
            continue

        # Parse JSON data
        # Parsuj dane JSON
        data = response.json()
        positions = data.get("positions", [])

        # Check if positions are available
        # Sprawdź, czy pozycje są dostępne
        if not positions:
            print(f"⚠️ No position data (Satellite below horizon or error).")
            print(f"⚠️ Brak danych o pozycji (Satelita pod horyzontem lub błąd).")
            time.sleep(30)
            continue

        # Get satellite name
        # Pobierz nazwę satelity
        sat_name = data["info"]["satname"]

        # 2. Connect to TAK Server
        # 2. Połącz z serwerem TAK

        # Initialize socket with SSL wrapper
        # Inicjalizuj gniazdo z opakowaniem SSL
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        wrapped_sock = ssl_context.wrap_socket(sock, server_hostname=TAK_IP)
        wrapped_sock.settimeout(5.0)

        try:
            # Establish connection
            # Nawiąż połączenie
            wrapped_sock.connect((TAK_IP, TAK_PORT))
        except Exception as e:
            # Handle TAK connection failure
            # Obsłuż błąd połączenia z TAK
            print(f"❌ Cannot connect to TAK Server: {e}")
            print(f"❌ Nie można połączyć z TAK Server: {e}")
            time.sleep(5)
            continue

        # 3. Generate and Send CoT
        # 3. Generuj i wyślij CoT

        for sat_data in positions:
            # Extract coordinates
            # Wyciągnij koordynaty
            sat_lat = sat_data["satlatitude"]
            sat_lon = sat_data["satlongitude"]

            # Convert altitude from km to meters (Critical for ATAK)
            # Konwertuj wysokość z km na metry (Kluczowe dla ATAK)
            sat_alt_m = sat_data["sataltitude"] * 1000

            # Set timestamps (UTC)
            # Ustaw znaczniki czasu (UTC)
            now = datetime.datetime.now(datetime.timezone.utc)
            stale = now + datetime.timedelta(minutes=2)

            # Build CoT Event object
            # Zbuduj obiekt zdarzenia CoT

            # CoT types: https://github.com/wcrum/py-cot/blob/main/CoT/types.py
            cot_event = CoT.Event(
                version="2.0",
                type="a-h-P-S",  # Hostile Space Satellite
                uid=f"SAT-{SAT_ID}",
                time=now,
                start=now,
                stale=stale,
                how="m-g",
                point=CoT.Point(
                    lat=sat_lat,
                    lon=sat_lon,
                    hae=sat_alt_m,
                    ce=1000,
                    le=1000
                ),
                detail={
                    "contact": {"callsign": f"{sat_name} (DECAY)"},
                    "remarks": f"ALT: {sat_alt_m / 1000:.1f}km. UNCONTROLLED REENTRY via N2YO.",
                    "track": {"speed": 7800, "course": 0},
                    "status": {"readiness": "true"}
                }
            )

            # Convert to XML and send
            # Konwertuj na XML i wyślij
            xml_data = cot_event.xml()
            wrapped_sock.sendall(bytes(xml_data, encoding="utf-8"))

            # Log to console with FIXED ALIGNMENT
            # Loguj do konsoli ze STAŁYM WYRÓWNANIEM
            # (>8.0f means: align right, 8 chars total width, 0 decimals)
            # (>7.2f means: align right, 7 chars total width, 2 decimals)
            print(
                f"📡 SENT: {now.strftime('%H:%M:%S')} | ALT: {sat_alt_m:>8.0f} m | LAT: {sat_lat:>7.2f} | LON: {sat_lon:>8.2f} | 🔴 HOSTILE")
            print(
                f"📡 WYSŁ: {now.strftime('%H:%M:%S')} | WYS: {sat_alt_m:>8.0f} m | SZER:{sat_lat:>7.2f} | DŁU: {sat_lon:>8.2f} | 🔴 WROGI")

            # Log to file (CORRECTED LINE - THIS IS THE FIX)
            # Loguj do pliku (POPRAWIONA LINIA - TO JEST POPRAWKA)
            logging.info(f"CoT for {sat_name}: lat={sat_lat}, lon={sat_lon}, alt={sat_alt_m}")

            # Clear buffer (Receive confirmation)
            # Wyczyść bufor (Odbierz potwierdzenie)
            try:
                _ = wrapped_sock.recv(1024)
            except socket.timeout:
                pass

        # Close connection and wait
        # Zamknij połączenie i czekaj
        wrapped_sock.close()
        time.sleep(REFRESH_INTERVAL)

    except KeyboardInterrupt:
        # Handle manual stop
        # Obsłuż ręczne zatrzymanie
        print(f"\n🔴 Stopped manually.")
        print(f"\n🔴 Zatrzymano ręcznie.")
        break
    except Exception as e:
        # Handle critical loop error
        # Obsłuż krytyczny błąd pętli
        print(f"\n❌ Critical Loop Error: {e}")
        print(f"\n❌ Błąd krytyczny pętli: {e}")
        logging.error(f"Critical Loop Error: {e}")
        time.sleep(10)