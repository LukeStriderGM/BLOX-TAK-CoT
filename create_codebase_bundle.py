#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import datetime
import re

# --- CONFIGURATION HEADERS ---
# --- NAGŁÓWKI KONFIGURACYJNE ---

# --- SECURITY FILTER CONFIGURATION ---
# --- KONFIGURACJA FILTRÓW BEZPIECZEŃSTWA ---

# Directories to ignore entirely (security and system junk)
# Katalogi do całkowitego zignorowania (bezpieczeństwo i śmieci systemowe)
IGNORE_DIRS = [
    'certs',  # CRITICAL: SSL certificates / KRYTYCZNE: Certyfikaty SSL
    '.venv', 'venv', 'env',  # Virtual environments / Środowiska wirtualne
    '.git',  # Git history / Historia git
    '__pycache__',  # Python cache / Cache pythona
    '.idea', '.vscode'  # IDE configuration / Konfiguracja IDE
]

# Specific file extensions to ignore (e.g., configuration files)
# Konkretne rozszerzenia plików do zignorowania (np. pliki konfiguracyjne)
IGNORE_EXTENSIONS = [
    '.yaml', '.yml'
]

# Specific system junk files to ignore
# Konkretne śmieci systemowe do zignorowania
IGNORE_FILES_EXACT = [
    '.DS_Store',
    'Thumbs.db'
]

# --- PROJECT SETTINGS ---
# --- USTAWIENIA PROJEKTU ---

README_PATH = "README.md"
PROJECT_NAME = "BLOX-TAK-CoT"


# --- FUNCTION DEFINITIONS ---
# --- DEFINICJE FUNKCJI ---

def get_version_from_readme():
    """
    Attempts to extract version from the first line of README.md.
    Próbuje wyciągnąć wersję z pierwszej linii README.md.
    """
    default_version = "v0.0.0.1"

    # Check if README file exists
    # Sprawdź, czy plik README istnieje
    if not os.path.exists(README_PATH):
        return default_version

    try:
        # Open README and read the first line
        # Otwórz README i przeczytaj pierwszą linię
        with open(README_PATH, 'r', encoding='utf-8') as f:
            first_line = f.readline()

            # Regex search for version pattern like v1.0.0.1 or (v1.0.0.1)
            # Wyszukiwanie regexem wzorca wersji typu v1.0.0.1 lub (v1.0.0.1)
            match = re.search(r'\(?(v\d+\.\d+\.\d+\.\d+)\)?', first_line)

            if match:
                return match.group(1)
            else:
                return default_version

    except Exception:
        return default_version


def is_ignored_secure(path, filename):
    """
    Checks if a file should be ignored based on security rules.
    Sprawdza, czy plik powinien zostać zignorowany na podstawie reguł bezpieczeństwa.
    """
    path_parts = path.split(os.sep)

    # 1. Check if in an ignored directory (e.g., certs, venv)
    # 1. Sprawdź, czy znajduje się w ignorowanym katalogu (np. certs, venv)
    for d in IGNORE_DIRS:
        if d in path_parts: return True

    # 2. Check if it is an exact ignored filename match
    # 2. Sprawdź, czy jest to dokładne dopasowanie ignorowanej nazwy pliku
    if filename in IGNORE_FILES_EXACT: return True

    # 3. Check if it has an ignored extension (e.g., .yaml)
    # 3. Sprawdź, czy ma ignorowane rozszerzenie (np. .yaml)
    for ext in IGNORE_EXTENSIONS:
        if filename.endswith(ext): return True

    # If it passed all checks, include the file
    # Jeśli przeszedł wszystkie testy, dołącz plik
    return False


def collect_files():
    """
    Walks directory structure and collects all safe file paths.
    Przechodzi strukturę katalogów i zbiera wszystkie bezpieczne ścieżki plików.
    """
    file_list = []

    # Walk through the current directory
    # Przejdź przez bieżący katalog
    for root, dirs, files in os.walk("."):

        # Modify dirs in-place to skip ignored directories during walk
        # Modyfikuj dirs in-place aby nie wchodzić do ignorowanych katalogów
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            # Skip codebase bundles themselves and the packaging script itself
            # Pomiń same paczki kodu oraz sam skrypt pakujący
            if "_CODEBASE__" in file or file == os.path.basename(__file__): continue

            # Skip files marked as unsafe or junk
            # Pomiń pliki oznaczone jako niebezpieczne lub śmieci
            if is_ignored_secure(root, file): continue

            # Construct relative path and add to list
            # Skonstruuj ścieżkę względną i dodaj do listy
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, ".")
            file_list.append(relative_path)

    # Sort list for consistent output order
    # Posortuj listę dla spójnej kolejności wyjścia
    file_list.sort()
    return file_list


def create_codebase_bundle():
    """
    Creates a single TEXT file containing a manifest and all source content.
    Tworzy jeden plik TEXT zawierający manifest i całą zawartość źródłową.
    """
    # Generate timestamps and version strings
    # Generuj znaczniki czasu i ciągi wersji
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    version = get_version_from_readme()
    version_safe = version.replace('.', '-')

    # Define output filename
    # Zdefiniuj nazwę pliku wyjściowego
    txt_filename = f"{PROJECT_NAME}_{version_safe}_CODEBASE__{timestamp}.txt"

    print(f"\n🔄 === STARTING CODEBASE BUNDLING ===")
    print(f"🔄 === ROZPOCZYNAM TWORZENIE PACZKI KODU ===")

    print(f"📂 [TXT] Generating: {txt_filename}...")
    print(f"📂 [TXT] Generowanie: {txt_filename}...")

    # Collect files to bundle
    # Zbierz pliki do spakowania
    files_to_bundle = collect_files()

    try:
        # Open output file for writing
        # Otwórz plik wyjściowy do zapisu
        with open(txt_filename, 'w', encoding='utf-8') as outfile:

            # --- HEADER SECTION ---
            # --- SEKCJJA NAGŁÓWKA ---

            outfile.write(f"PROJECT: {PROJECT_NAME}\n")
            outfile.write(f"VERSION: {version}\n")
            outfile.write(f"DATE:    {timestamp}\n")
            outfile.write("=" * 60 + "\n\n")

            outfile.write("NOTE: Full codebase dump excluding secrets (certs/) and environments.\n")
            outfile.write("UWAGA: Pełny zrzut kodu źródłowego z pominięciem sekretów (certs/) i środowisk.\n")
            outfile.write("=" * 60 + "\n\n")

            # --- FILE MANIFEST SECTION ---
            # --- SEKCJA MANIFESTU PLIKÓW ---

            outfile.write("FILE MANIFEST / LISTA PLIKÓW:\n")
            outfile.write("-" * 30 + "\n")

            if not files_to_bundle:
                outfile.write("(No files found / Nie znaleziono plików)\n")
            else:
                for file_path in files_to_bundle:
                    outfile.write(f"{file_path}\n")

            outfile.write("\n" + "=" * 60 + "\n\n")

            # --- FILE CONTENT SECTION ---
            # --- SEKCJA ZAWARTOŚCI PLIKÓW ---

            for relative_path in files_to_bundle:
                outfile.write(f"\n--- START FILE: {relative_path} ---\n")

                try:
                    # Open file for reading content
                    # Otwórz plik do odczytu zawartości
                    with open(relative_path, 'r', encoding='utf-8') as infile:
                        outfile.write(infile.read())

                except UnicodeDecodeError:
                    # Handle binary or non-UTF8 files graciously
                    # Obsłuż pliki binarne lub nie-UTF8 łaskawie
                    outfile.write(f"[WARNING: File is not UTF-8 encoded text. Content skipped.]\n")
                    outfile.write(f"[OSTRZEŻENIE: Plik nie jest tekstem kodowanym w UTF-8. Pominięto zawartość.]\n")

                except Exception as e:
                    # Handle other reading errors
                    # Obsłuż inne błędy odczytu
                    outfile.write(f"[Error reading file / Błąd odczytu pliku: {e}]\n")

                outfile.write(f"\n--- END FILE: {relative_path} ---\n")

        print(f"✅ SUCCESS! Created: {txt_filename}")
        print(f"✅ SUKCES! Utworzono: {txt_filename}")

    except Exception as e:
        print(f"❌ ERROR: Failed to create bundle: {e}")
        print(f"❌ BŁĄD: Nie udało się utworzyć paczki: {e}")


# --- MAIN EXECUTION ---
# --- GŁÓWNE WYKONANIE ---

if __name__ == "__main__":
    create_codebase_bundle()