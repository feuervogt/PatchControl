# PatchControl
Verwaltungsprogramm für Netzwerk- und Telefondosen

**PatchControl** ist eine Python-basierte Anwendung zur Verwaltung von Netzwerk- und Telefondosen in einer Unternehmensumgebung. Das Tool erlaubt das Hinzufügen, Bearbeiten und Löschen von Dosen sowie die Zuweisung von IP-Adressen oder Telefonnummern. Es soll die Organisation und Wartung der IT-Infrastruktur effizienter gestalten.

## Inhaltsverzeichnis

1. [Über das Projekt](#über-das-projekt)
2. [Funktionen](#funktionen)
3. [Installation](#installation)
4. [Verwendung](#verwendung)
5. [Geplante Erweiterungen](#geplante-erweiterungen)
6. [Beitragen](#beitragen)
7. [Lizenz](#lizenz)

## Über das Projekt

PatchControl wird entwickelt, um IT-Administratoren eine zentrale Möglichkeit zur Verwaltung von Netzwerk- und Telefondosen zu bieten. Jede Dose ist mit spezifischen Informationen wie Standort (Gebäude, Etage, Raum), Bezeichnung (im Format x-x-x für Bucht-Leiste-Stift), Telefonnummer oder IP-Adresse und Anschluss (Netzwerk oder Telefonnetz) versehen. Die Daten werden in einer Datenbank gespeichert und sind einfach über eine grafische Benutzeroberfläche (GUI) zugänglich und editierbar.

## Funktionen

- **Zentralisierte Verwaltung** von Netzwerk- und Telefondosen.
- **GUI** für benutzerfreundliche Bedienung (erstellt mit PyQt).
- **Datenbank-Speicherung** der Doseninformationen mit Standort, Bezeichnung und Anschlussdetails.
- **Editieren, Hinzufügen und Löschen** von Dosen.
- **Dropdown-Menüs** zur schnellen Auswahl und Bearbeitung von Standorten.

## Installation

### Voraussetzungen

- Python 3.13 oder höher
- [PyQt5](https://pypi.org/project/PyQt5/) für die GUI
- Eine SQL-basierte Datenbank (z.B. SQLite, MySQL) zur Speicherung der Daten

### Schritte zur Installation

1. **Repository klonen**:
   ```bash
   git clone https://github.com/deinBenutzername/PatchControl.git
   cd PatchControl
   ```

2. **Abhängigkeiten installieren**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Datenbank konfigurieren**:
   - Die Datenbankstruktur muss initial erstellt werden. Details zur Einrichtung findest du im Ordner `db/`. Ein SQL-Skript zur Erstellung der Datenbanktabellen ist im Projekt enthalten.

4. **Anwendung starten**:
   ```bash
   python patchcontrol.py
   ```

## Verwendung

- **Starten der Anwendung**: Öffne ein Terminal und führe `python patchcontrol.py` aus.
- **Dosen hinzufügen**: In der GUI gibt es eine Schaltfläche „Neue Dose hinzufügen“, über die alle Informationen wie Standort, Bezeichnung und Anschluss angegeben werden können.
- **Dosen bearbeiten**: Über die Bearbeitungsfunktion können bestehende Doseninformationen aktualisiert werden.
- **Dosen löschen**: Nicht mehr benötigte Dosen können aus der Datenbank entfernt werden.

## Geplante Erweiterungen

- **Schnittstellen für andere Systeme** zur automatischen Synchronisation.
- **Exportfunktion** für Berichte und Dokumentationen.
- **Suche und Filter** für eine erweiterte Datenbankabfrage.
- **Benutzerverwaltung** für eine differenzierte Zugriffssteuerung.
- **Echtzeit-Anzeigen** des Patch-Status, um bei Problemen schnell reagieren zu können.

## Beitragen

Falls du oder deine Azubis zum Projekt beitragen möchten, sind folgende Schritte notwendig:

1. **Forke das Repository** und klone es lokal.
2. Erstelle einen neuen Branch für deine Änderungen:
   ```bash
   git checkout -b feature/neue-funktion
   ```
3. Committe deine Änderungen und pushe den Branch:
   ```bash
   git push origin feature/neue-funktion
   ```
4. Erstelle einen Pull Request, um die Änderungen zu überprüfen und zusammenzuführen.

## Lizenz

Da das Projekt zurzeit intern genutzt wird, ist es vorerst nicht öffentlich lizenziert. Eine spätere Entscheidung zur Lizenzierung und Veröffentlichung kann je nach Bedarf erfolgen.

---

**Hinweis**: Dieses Projekt wurde entwickelt für den Einsatz in einer Unternehmensumgebung und sollte nicht ohne entsprechende Anpassungen in anderen Umgebungen genutzt werden.

---


