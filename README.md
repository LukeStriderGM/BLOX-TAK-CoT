# 🇺🇸 / 🇵🇱 BLOX-TAK-CoT

Welcome to **BLOX-TAK-CoT**. This project is a universal, Python-based integration bridge designed to track **any** orbital object (Satellites, Rocket Bodies, Debris, Space Stations) in real-time via the N2YO API and visualize its telemetry within the ATAK (Android Team Awareness Kit) ecosystem using the Cursor on Target (CoT) protocol.

While initially developed to research "Ghost Satellite" phenomena during uncontrolled reentries (like ZQ-3), **BLOX-TAK-CoT** is fully configurable to track stable assets (ISS, Starlink, Tiangong) or high-value targets by simply changing the configuration ID.

📺 #YouTube:

CORE - https://youtu.be/lcWTPbxM3_g

REPLAY - https://youtu.be/nNv6e3a4rn4

🌐 Socials:

Linkedin: https://www.linkedin.com/posts/lukebluelox_zq3-reentry-blox-share-7423271365610393600-aTHS

𝕏: https://x.com/LukeStriderGM/status/2017505686943314412

<details>

<summary>🇵🇱 [Kliknij Trójkąt Po Lewej Stronie Aby Rozwinąć Opis w Języku Polskim]</summary>

# 🇵🇱 BLOX-TAK-CoT

Witaj w **BLOX-TAK-CoT**. Ten projekt to uniwersalny most integracyjny oparty na języku Python, zaprojektowany do śledzenia **dowolnego** obiektu orbitalnego (satelity, człony rakiet, śmieci kosmiczne, stacje kosmiczne) w czasie rzeczywistym za pośrednictwem API N2YO i wizualizacji jego telemetrii w ekosystemie ATAK (Android Team Awareness Kit) przy użyciu protokołu Cursor on Target (CoT).

Choć narzędzie to zostało pierwotnie opracowane do badania zjawisk "Satelitów Duchów" podczas niekontrolowanych wejść w atmosferę (jak ZQ-3), **BLOX-TAK-CoT** jest w pełni konfigurowalne do śledzenia stabilnych zasobów (ISS, Starlink, Tiangong) lub celów o wysokim znaczeniu poprzez prostą zmianę identyfikatora w konfiguracji.

📺 #YouTube:

CORE - https://youtu.be/lcWTPbxM3_g

REPLAY - https://youtu.be/nNv6e3a4rn4

🌐 Socials:

Linkedin: https://www.linkedin.com/posts/lukebluelox_deorbitacja-zq3-blox-share-7423271298686173184-G4w8

𝕏: https://x.com/LukeStriderGM/status/2017505668349968509

</details>

---

## 🇺🇸 Core Features / 🇵🇱 Główne Funkcjonalności

* **Universal Architecture**: Compatible with the entire NORAD database. Whether it's a falling rocket body or the ISS, if it has an ID, this tool can track it.
* **Real-Time Telemetry Bridge**: Fetches precise orbital data (Latitude, Longitude, Altitude) every second and injects it into the TAK network.
* **Native CoT Transformation**: Instantly converts API data into XML-based Cursor on Target (CoT) events compatible with TAK Servers (CivTAK/FreeTAKServer) and ATAK Civ/Mil clients.
* **Dynamic Hostility Tagging**: Configurable tagging system to flag objects as "Hostile" (Imminent Threat/Debris) or "Friendly/Neutral" (Active Assets).
* **Mission Replay Module**: Includes a dedicated `replay_cot.py` engine to re-broadcast captured log data for post-mission analysis, training, and simulation.
* **Secure SSL/TLS Transmission**: Supports encrypted communication channels for professional deployments.
* **Bilingual Logs**: Console outputs and system logs are formatted in a clean, vertical bilingual style (English/Polish) for international collaboration.

<details>

<summary>🇵🇱</summary>

## 🇵🇱 Główne Funkcjonalności

* **Uniwersalna Architektura**: Kompatybilność z całą bazą danych NORAD. Niezależnie od tego, czy jest to spadający człon rakiety, czy ISS – jeśli obiekt ma ID, to narzędzie może go śledzić.
* **Most Telemetryczny w Czasie Rzeczywistym**: Pobiera precyzyjne dane orbitalne (Szerokość, Długość, Wysokość) co sekundę i wstrzykuje je do sieci TAK.
* **Natywna Transformacja CoT**: Natychmiastowo konwertuje dane API na zdarzenia Cursor on Target (CoT) oparte na XML, kompatybilne z serwerami TAK (CivTAK/FreeTAKServer) i klientami ATAK Civ/Mil.
* **Dynamiczne Oznaczanie Wrogości**: Konfigurowalny system tagowania do oznaczania obiektów jako "Wrogie" (Bezpośrednie Zagrożenie/Śmieci) lub "Przyjazne/Neutralne" (Aktywne Zasoby).
* **Moduł Odtwarzania Misji**: Zawiera dedykowany silnik `replay_cot.py` do ponownego nadawania przechwyconych danych logów w celu analizy po misji, szkoleń i symulacji.
* **Bezpieczna Transmisja SSL/TLS**: Obsługuje szyfrowane kanały komunikacji dla profesjonalnych wdrożeń.
* **Dwujęzyczne Logi**: Wyjścia konsoli i logi systemowe są sformatowane w czystym, pionowym stylu dwujęzycznym (Angielski/Polski) dla współpracy międzynarodowej.

</details>

---

## 🇺🇸 Prerequisites / 🇵🇱 Wymagania Wstępne

To deploy **BLOX-TAK-CoT**, you will need the following environment (optimized for Orange Pi 5 / Ubuntu / Debian):

1.  **Hardware**: Orange Pi 5 (or any Linux-based edge device/server).
2.  **OS**: Ubuntu 22.04 LTS or Debian Bookworm.
3.  **Python 3.10+**: With `venv` support.
4.  **Data Source**: A valid API key from [n2yo.com](https://www.n2yo.com/api/).
5.  **Target System**: A running TAK Server instance reachable via IP.
6.  **Security**: Valid client certificates (`.pem`, `.key`, `trusted-root.pem`) for the TAK connection.

<details>

<summary>🇵🇱</summary>

## 🇵🇱 Wymagania Wstępne

Aby wdrożyć **BLOX-TAK-CoT**, będziesz potrzebować następującego środowiska (zoptymalizowanego dla Orange Pi 5 / Ubuntu / Debian):

1.  **Sprzęt**: Orange Pi 5 (lub dowolne urządzenie brzegowe/serwer oparty na Linuxie).
2.  **System Operacyjny**: Ubuntu 22.04 LTS lub Debian Bookworm.
3.  **Python 3.10+**: Z obsługą `venv`.
4.  **Źródło Danych**: Ważny klucz API ze strony [n2yo.com](https://www.n2yo.com/api/).
5.  **System Docelowy**: Działająca instancja serwera TAK dostępna przez IP.
6.  **Bezpieczeństwo**: Ważne certyfikaty klienta (`.pem`, `.key`, `trusted-root.pem`) do połączenia TAK.

</details>

---

## 🇺🇸 Installation Guide / 🇵🇱 Instrukcja Instalacji

Follow these steps to set up the **BLOX-TAK-CoT** environment.

### 🇺🇸 Step 1: Clone & Configure Environment

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/LukeStriderGM/BLOX-TAK-CoT
    cd BLOX-TAK-CoT
    ```

2.  **Create Virtual Environment**:
    It is crucial to use a virtual environment to manage dependencies properly without affecting the system root.
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install Requirements**:
    ```bash
    pip install -r requirements.txt
    ```
    https://pypi.org/project/PyCoT

<details>

<summary>🇵🇱</summary>

### 🇵🇱 Krok 1: Klonowanie i Konfiguracja Środowiska

1.  **Sklonuj Repozytorium**:
    ```bash
    git clone https://github.com/LukeStriderGM/BLOX-TAK-CoT
    cd BLOX-TAK-CoT
    ```

2.  **Utwórz Wirtualne Środowisko**:
    Użycie wirtualnego środowiska jest kluczowe dla poprawnego zarządzania zależnościami bez wpływu na system główny (root).
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Zainstaluj Wymagania**:
    ```bash
    pip install -r requirements.txt
    ```
    https://pypi.org/project/PyCoT

</details>

---

## 🇺🇸 Configuration / 🇵🇱 Konfiguracja

The system is designed to be easily reconfigurable for different missions. Edit the top section of `N2YO-API-Query_PyCoT-TAK-Server.py`.

### 🇺🇸 Target Selection
Modify the `SAT_ID` variable to track different objects.

```python
# --- USER SETTINGS ---
N2YO_API_KEY = "YOUR-API-KEY"

# Target Definition (NORAD ID)
SAT_ID = 66877      # Target: ZQ-3 R/B (Debris/Reentry)
# SAT_ID = 25544    # Target: ISS (International Space Station)
# SAT_ID = 48274    # Target: CSS (Tiangong Space Station)
```

### 🇺🇸 Tactical Identity (Hostility)

Adjust the CoT type to reflect the tactical nature of the object.

https://github.com/wcrum/py-cot/blob/main/CoT/types.py

```python
# For Threats / Debris / Hostiles:
type="a-h-P-S"  # Atom-Hostile-Space-Satellite (Red Icon)

# For Friendly / Neutral Assets:
type="a-n-P-S"  # Atom-Neutral-Space-Satellite (Green/Blue Icon)
```

<details>

<summary>🇵🇱</summary>

### 🇵🇱 Wybór Celu

Zmodyfikuj zmienną `SAT_ID`, aby śledzić różne obiekty.

```python
# --- USTAWIENIA UŻYTKOWNIKA ---
N2YO_API_KEY = "TWÓJ-KLUCZ-API"

# Definicja Celu (NORAD ID)
SAT_ID = 66877      # Cel: ZQ-3 R/B (Szczątki/Deorbitacja)
# SAT_ID = 25544    # Cel: ISS (Międzynarodowa Stacja Kosmiczna)
# SAT_ID = 48274    # Cel: CSS (Stacja Kosmiczna Tiangong)
```

### 🇵🇱 Tożsamość Taktyczna (Wrogość)

Dostosuj `type` CoT, aby odzwierciedlić taktyczną naturę obiektu.

https://github.com/wcrum/py-cot/blob/main/CoT/types.py

```python
# Dla Zagrożeń / Szczątków / Wrogów:
type="a-h-P-S"  # Atom-Hostile-Space-Satellite (Czerwona Ikona)

# Dla Zasobów Przyjaznych / Neutralnych:
type="a-n-P-S"  # Atom-Neutral-Space-Satellite (Zielona/Niebieska Ikona)
```

</details>

---

## 🇺🇸 Usage / 🇵🇱 Użycie

### 🇺🇸 Mode 1: Real-Time Tracker

Starts the live bridge between N2YO and the TAK Server. Note: Use `sudo` combined with the `venv` path to ensure access to SSL certs and system sockets.

```bash
sudo ./.venv/bin/python3 N2YO-API-Query_PyCoT-TAK-Server.py
```

*   **Output**: Displays live formatted ALT/LAT/LON telemetry.
*   **Logging**: Automatically saves session data to `cot.log`.

### 🇺🇸 Mode 2: Mission Replay

Re-broadcasts captured telemetry to simulate the event or analyze data post-mission.

```bash
sudo ./.venv/bin/python3 replay_cot.py
```

*   The script prompts for Start/End Time (Format: `YYYY-MM-DD HH:MM:SS`).
*   Reads from `cot.log` and injects packets into the TAK network as if they were live.

<details>

<summary>🇵🇱</summary>

### 🇵🇱 Tryb 1: Tracker Czasu Rzeczywistego

Uruchamia żywy most między N2YO a serwerem TAK. Uwaga: Użyj `sudo` w połączeniu ze ścieżką `venv`, aby zapewnić dostęp do certyfikatów SSL i gniazd systemowych.

```bash
sudo ./.venv/bin/python3 N2YO-API-Query_PyCoT-TAK-Server.py
```

*   **Wyjście**: Wyświetla sformatowaną telemetrię WYS/SZER/DŁU na żywo.
*   **Logowanie**: Automatycznie zapisuje dane sesji do `cot.log`.

### 🇵🇱 Tryb 2: Odtwarzanie Misji (Replay)

Ponownie nadaje przechwyconą telemetrię w celu symulacji zdarzenia lub analizy danych po misji.

```bash
sudo ./.venv/bin/python3 replay_cot.py
```

*   Skrypt prosi o Czas Startu/Końca (Format: `RRRR-MM-DD GG:MM:SS`).
*   Odczytuje dane z `cot.log` i wstrzykuje pakiety do sieci TAK tak, jakby były na żywo.

</details>

---

## 🇺🇸 License / Licencja 🇵🇱

This project is licensed under the MIT License. See the LICENSE file for details.

<details>

<summary>🇵🇱</summary>

## Licencja

Ten projekt jest objęty licencją MIT. Zobacz plik LICENSE, aby uzyskać szczegółowe informacje.

Tłumaczenie [PL]:

Licencja MIT

Prawa autorskie (c) 2025 Łukasz "LukeStriderGM" Andruszkiewicz

Niniejszym udziela się bezpłatnej zgody każdej osobie wchodzącej w posiadanie kopii tego oprogramowania i powiązanych z nim plików dokumentacji (dalej „Oprogramowanie”), na obchodzenie się z Oprogramowaniem bez ograniczeń, włączając w to bez ograniczeń prawa do używania, kopiowania, modyfikowania, łączenia, publikowania, dystrybucji, sublicencjonowania i/lub sprzedaży kopii Oprogramowania, oraz na zezwolenie osobom, którym Oprogramowanie jest dostarczane, aby to czyniły, pod następującymi warunkami:

Powyższa nota o prawach autorskich i ta nota o pozwoleniu muszą być dołączone do wszystkich kopii lub istotnych części Oprogramowania.

OPROGRAMOWANIE JEST DOSTARCZANE "TAKIM, JAKIE JEST", BEZ JAKIEJKOLWIEK GWARANCJI, WYRAŹNEJ LUB DOROZUMIANEJ, WŁĄCZAJĄC W TO, ALE NIE OGRANICZAJĄC SIĘ DO, GWARANCJI PRZYDATNOŚCI HANDLOWEJ, PRZYDATNOŚCI DO OKREŚLONEGO CELU ORAZ NIENARUSZALNOŚCI PRAW. W ŻADNYM WYPADKU AUTORZY LUB POSIADACZE PRAW AUTORSKICH NIE BĘDĄ ODPOWIEDZIALNI ZA JAKIEKOLWIEK ROSZCZENIA, SZKODY LUB INNE ZOBOWIĄZANIA, CZY TO W WYNIKU DZIAŁANIA UMOWY, DELIKTU CZY W INNY SPOSÓB, WYNIKAJĄCE Z, LUB W ZWIĄZKU Z OPROGRAMOWANIEM LUB UŻYCIEM LUB INNYMI DZIAŁANIAMI W OPROGRAMOWANIU.

</details>

---

## 🇺🇸 Code of Conduct / Kodeks Postepowania 🇵🇱

This project and everyone participating in it is governed by the Contributor Covenant. See the CODE_OF_CONDUCT.md file for details.

<details>
<summary>🇵🇱</summary>

Kodeks Postępowania

Ten projekt i wszyscy w nim uczestniczący podlegają Zasadom Współtwórcy (Contributor Covenant). Zobacz plik CODE_OF_CONDUCT.md, aby uzyskać szczegółowe informacje.

Tłumaczenie [PL]:


## Kodeks Postępowania - Contributor Covenant

### Nasza Obietnica

Jako członkinie i członkowie, współtwórczynie i współtwórcy oraz liderki i liderzy
zobowiązujemy się, że udział w naszej społeczności będzie wolny od nękania dla
każdego, bez względu na wiek, budowę ciała, widoczną lub niewidoczną
niepełnosprawność, pochodzenie etniczne, cechy płciowe, tożsamość i ekspresję
płciową, poziom doświadczenia, wykształcenie, status społeczno-ekonomiczny,
narodowość, wygląd, rasę, religię czy tożsamość i orientację seksualną.

Zobowiązujemy się do działania i interakcji w sposób, który przyczynia się do
tworzenia otwartej, przyjaznej, zróżnicowanej, inkluzywnej i zdrowej społeczności.

### Nasze Standardy

Przykłady zachowań, które przyczyniają się do tworzenia pozytywnego środowiska
dla naszej społeczności, obejmują:

* Okazywanie empatii i życzliwości wobec innych osób
* Szacunek dla odmiennych opinii, punktów widzenia i doświadczeń
* Udzielanie i taktowne przyjmowanie konstruktywnej informacji zwrotnej
* Przyjmowanie odpowiedzialności, przepraszanie osób dotkniętych naszymi
    błędami i wyciąganie z nich wniosków
* Skupianie się nie tylko na tym, co najlepsze dla nas jako jednostek, ale dla
    całej społeczności

Przykłady niedopuszczalnych zachowań obejmują:

* Używanie języka lub obrazów o charakterze seksualnym oraz wszelkiego rodzaju
    zaloty lub umizgi o charakterze seksualnym
* Trolling, obraźliwe lub uwłaczające komentarze oraz ataki osobiste lub
    polityczne
* Nękanie publiczne lub prywatne
* Publikowanie prywatnych informacji innych osób, takich jak adres fizyczny lub
    mailowy, bez ich wyraźnej zgody
* Inne zachowania, które można by uznać za niewłaściwe w środowisku
    profesjonalnym

### Obowiązki Egzekwowania Zasad

Liderki i liderzy społeczności są odpowiedzialni za wyjaśnianie i egzekwowanie
naszych standardów oraz podejmą odpowiednie i sprawiedliwe działania naprawcze w
odpowiedzi na każde zachowanie, które uznają za niestosowne, zagrażające,
obraźliwe lub szkodliwe.

Liderki i liderzy społeczności mają prawo i obowiązek usuwać, edytować lub
odrzucać komentarze, commity, kod, edycje wiki, zgłoszenia i inne formy wkładu,
które nie są zgodne z niniejszym Kodeksem Postępowania, i w razie potrzeby
przedstawią powody swoich decyzji moderacyjnych.

### Zakres

Niniejszy Kodeks Postępowania obowiązuje we wszystkich przestrzeniach
społeczności, a także wtedy, gdy dana osoba oficjalnie reprezentuje społeczność w
przestrzeni publicznej. Przykłady reprezentowania naszej społeczności obejmują
używanie oficjalnego adresu e-mail, publikowanie postów za pośrednictwem
oficjalnego konta w mediach społecznościowych lub występowanie w charakterze
wyznaczonej przedstawicielki lub przedstawiciela na wydarzeniu online lub offline.

### Egzekwowanie Zasad

Przypadki obraźliwego, nękającego lub w inny sposób niedopuszczalnego zachowania
mogą być zgłaszane liderkom i liderom społeczności odpowiedzialnym za egzekwowanie
zasad pod adresem **luke.strider.gm@gmail.com**.
Wszystkie skargi zostaną rozpatrzone i zbadane niezwłocznie i sprawiedliwie.

Wszystkie liderki i liderzy społeczności są zobowiązani do poszanowania prywatności i
bezpieczeństwa osoby zgłaszającej incydent.

### Wytyczne Dotyczące Egzekwowania Zasad

Liderki i liderzy społeczności będą postępować zgodnie z niniejszymi Wytycznymi
Dotyczącymi Wpływu na Społeczność przy określaniu konsekwencji za każde
działanie, które uznają za naruszenie niniejszego Kodeksu Postępowania:

### 1. Naprawienie

**Wpływ na Społeczność**: Używanie niestosownego języka lub inne zachowanie uznane
za nieprofesjonalne lub niemile widziane w społeczności.

**Konsekwencja**: Prywatne, pisemne upomnienie od liderek lub liderów społeczności,
wyjaśniające naturę naruszenia i powód, dla którego zachowanie było
niestosowne. Może zostać zażądane publiczne przeproszenie.

### 2. Ostrzeżenie

**Wpływ na Społeczność**: Naruszenie w wyniku pojedynczego incydentu lub serii
działań.

**Konsekwencja**: Ostrzeżenie z konsekwencjami za dalsze zachowanie. Zakaz
interakcji z osobami zaangażowanymi, w tym nieproszonych interakcji z osobami
egzekwującymi Kodeks Postępowania, przez określony czas. Obejmuje to unikanie
interakcji w przestrzeniach społeczności, jak i na kanałach zewnętrznych, takich
jak media społecznościowe. Naruszenie tych warunków może prowadzić do
tymczasowego lub stałego bana.

### 3. Tymczasowy Ban

**Wpływ na Społeczność**: Poważne naruszenie standardów społeczności, w tym
utrzymujące się niestosowne zachowanie.

**Konsekwencja**: Tymczasowy zakaz jakichkolwiek interakcji lub publicznej
komunikacji ze społecznością na określony czas. W tym okresie zabronione są
publiczne i prywatne interakcje z osobami zaangażowanymi, w tym nieproszone
interakcje z osobami egzekwującymi Kodeks Postępowania. Naruszenie tych
warunków może prowadzić do stałego bana.

### 4. Stały Ban

**Wpływ na Społeczność**: Wykazywanie wzorca naruszania standardów społeczności,
w tym utrzymujące się niestosowne zachowanie, nękanie danej osoby lub agresja
wobec lub oczernianie grup osób.

**Konsekwencja**: Stały zakaz jakichkolwiek publicznych interakcji w ramach
społeczności.

---
Atrybucja

Niniejszy Kodeks Postępowania jest adaptacją [Contributor Covenant][homepage],
wersja 2.1, dostępnej pod adresem
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html

---

</details>
