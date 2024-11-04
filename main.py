"""
Projekt: PatchControl - Anwendung zur Verwaltung von Netzwerk- und Telefondosen
Autor: [feuervogt]
Version: 0.1.0-alpha
Datum: [04.11.2024]
Beschreibung:
    PatchControl ist eine Anwendung zur Verwaltung der Netzwerk- und Telefondosen im Unternehmen. 
    Die Anwendung speichert die Lage der Dosen, deren Typ (Netzwerk oder Telefon), 
    sowie spezifische Verbindungsinformationen (z.B. IP-Adresse, Telefonnummer) in einer Datenbank.
    Mit der Anwendung können neue Dosen hinzugefügt, vorhandene Dosen bearbeitet und gelöscht werden.
    Die GUI ist mit PyQt erstellt und ermöglicht eine benutzerfreundliche Verwaltung der Dosen-Daten.

Namenskonventionen:
    - `snake_case` für Variablen und Funktionen:
        * Beispiel: location_building, assigned_number_or_ip, add_outlet()
    - `CamelCase` für Klassen:
        * Beispiel: OutletManager, DatabaseConnection
    - Präfixe für spezielle Typen:
        * `form_` für Formular-Elemente (z.B. form_outlet_data)
        * `button_` für Schaltflächen (z.B. button_add_outlet)
        * `dropdown_` für Dropdown-Menüs (z.B. dropdown_location)
    - Konsistenz:
        * Variablenbezeichnungen sollen verständlich und spezifisch für die Anwendung sein.
        * Benennungen wie `outlet_label` oder `patch_panel_position` beschreiben präzise ihre Bedeutung.

Datenbank-Tabellen und Felder:
    - Tabelle: outlets
    - Felder: location_building, location_floor, location_room, location_position, outlet_label,
              outlet_type, connection_type, assigned_number_or_ip, patch_panel_position, lsa_position

Funktionen:
    - `add_outlet()`: Fügt eine neue Dose zur Datenbank hinzu.
    - `update_outlet()`: Aktualisiert die Daten einer bestehenden Dose.
    - `delete_outlet()`: Löscht eine Dose aus der Datenbank.
    - `get_outlet_data()`: Ruft die Informationen einer Dose aus der Datenbank ab.
    - `display_outlet_path()`: Zeigt den Verlauf des Kabels für eine spezifische Dose an (optional).

Hinweis:
    Diese Datei ist Teil des Projekts PatchControl. Änderungen an der Namenskonvention 
    sollten durch Anpassung dieses Headers dokumentiert werden.
"""
"""Ab hier startet der Programmcode"""

import sys
from PyQt5.QtWidgets import QApplication
from gui import PatchControlGUI                #importiert die GUI Klasse
from database import Database

def main():
    app = QApplication(sys.argv)   # Erstelle die QApplication-Instanz
    window = PatchControlGUI()               # Erstelle die Instanz der GUI
    window.show()                  # Zeige das Hauptfenster
    sys.exit(app.exec_())          # Starte das Event-Loop von PyQt

if __name__ == "__main__":
    main()

# Erstelle eine Datenbankinstanz und initialisiere die Tabelle
db = Database("patchcontrol.db")
db.create_table()  # Tabelle erstellen, falls sie noch nicht existiert

# Beispiel: Eine neue Dose hinzufügen
db.add_dose("Gebäude A", "1", "101", 1, "A-1-1", "Netzwerk", "Patchpanel 1", "Patchpanel")

# Beispiel: Alle Dosen aus der Datenbank abrufen und anzeigen
dosen = db.get_all_dosen()
for dose in dosen:
    print(dose)

# Beispiel: Eine Dose aktualisieren
db.update_dose(1, raum="102", position=2)  # Ändert Raum und Position der Dose mit ID 1

# Beispiel: Eine Dose löschen
db.delete_dose(1)  # Löscht die Dose mit der ID 1
