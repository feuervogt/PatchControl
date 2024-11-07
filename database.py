import sqlite3
from sqlite3 import Error
from PyQt5.QtWidgets import QApplication, QMessageBox, QInputDialog


class Database:
    def __init__(self, db_file):
        """Stellt eine Verbindung zur SQLite-Datenbank her."""
        self.connection = None
        try:
            self.connection = sqlite3.connect(db_file)
            print("Verbindung zur SQLite-Datenbank hergestellt.")
        except Error as e:
            print(f"Fehler beim Verbinden zur SQLite-Datenbank: {e}")

    def create_tables(self):
        """Erstellt die Tabellen für Dosen, TK-Anlage und Verteilerschränke."""
        
        # Tabelle für Netzwerk- und Telefondosen
        create_dose_table = """
        CREATE TABLE IF NOT EXISTS dose (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gebaeude TEXT NOT NULL,
            etage TEXT NOT NULL,
            raum TEXT NOT NULL,
            position INTEGER NOT NULL,
            bezeichnung TEXT NOT NULL UNIQUE,
            anschluss_typ TEXT CHECK(anschluss_typ IN ('Netzwerk', 'Telefonnetz')) NOT NULL,
            ziel TEXT NOT NULL,
            ziel_typ TEXT CHECK(ziel_typ IN ('Patchpanel', 'LSA-Leiste')) NOT NULL,
            durchwahl TEXT,  -- Neue Spalte für Durchwahl
            nutzer TEXT      -- Neue Spalte für den Nutzer
        );
        """
        
        # Tabelle für die TK-Anlage
        create_tk_anlage_table = """
        CREATE TABLE IF NOT EXISTS tk_anlage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            lokalisationsknoten TEXT NOT NULL,
            baugruppentraeger TEXT NOT NULL,
            leiterplatte TEXT NOT NULL,
            geraeteadresse TEXT NOT NULL
        );
        """
        
        # Tabelle für die Verteilerschränke
        create_verteilerschrank_table = """
        CREATE TABLE IF NOT EXISTS verteilerschrank (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ort_gebaeude TEXT NOT NULL,
            ort_etage TEXT NOT NULL,
            ort_raum TEXT NOT NULL,
            bucht TEXT NOT NULL,
            leiste TEXT NOT NULL,
            stift TEXT NOT NULL,
            ankommend TEXT NOT NULL,
            abgehend TEXT NOT NULL
        );
        """
        
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_dose_table)
            cursor.execute(create_tk_anlage_table)
            cursor.execute(create_verteilerschrank_table)
            self.connection.commit()
            print("Tabellen erfolgreich erstellt.")
        except Error as e:
            print(f"Fehler beim Erstellen der Tabellen: {e}")

    def add_dose(self, gebaeude, etage, raum, position, bezeichnung, anschluss_typ, ziel, ziel_typ, durchwahl=None, nutzer=None):
        """Fügt eine neue Dose zur Tabelle hinzu."""
        insert_query = """
        INSERT INTO dose (gebaeude, etage, raum, position, bezeichnung, anschluss_typ, ziel, ziel_typ, durchwahl, nutzer)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (gebaeude, etage, raum, position, bezeichnung, anschluss_typ, ziel, ziel_typ, durchwahl, nutzer))
            self.connection.commit()
            print("Dose erfolgreich hinzugefügt.")
        except Error as e:
            print(f"Fehler beim Hinzufügen der Dose: {e}")

    def add_tk_anlage(self, lokalisationsknoten, baugruppentraeger, leiterplatte, geraeteadresse):
        """Fügt eine neue TK-Anlage zur Tabelle hinzu."""
        insert_query = """
        INSERT INTO tk_anlage (lokalisationsknoten, baugruppentraeger, leiterplatte, geraeteadresse)
        VALUES (?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (lokalisationsknoten, baugruppentraeger, leiterplatte, geraeteadresse))
            self.connection.commit()
            print("TK-Anlage erfolgreich hinzugefügt.")
        except Error as e:
            print(f"Fehler beim Hinzufügen der TK-Anlage: {e}")

    def add_verteilerschrank(self, ort_gebaeude, ort_etage, ort_raum, bucht, leiste, stift, ankommend, abgehend):
        """Fügt einen neuen Verteilerschrank zur Tabelle hinzu."""
        insert_query = """
        INSERT INTO verteilerschrank (ort_gebaeude, ort_etage, ort_raum, bucht, leiste, stift, ankommend, abgehend)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (ort_gebaeude, ort_etage, ort_raum, bucht, leiste, stift, ankommend, abgehend))
            self.connection.commit()
            print("Verteilerschrank erfolgreich hinzugefügt.")
        except Error as e:
            print(f"Fehler beim Hinzufügen des Verteilerschranks: {e}")

    def get_all_dosen(self):
        """Gibt alle Dosen aus der Tabelle zurück."""
        select_query = "SELECT * FROM dose;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(select_query)
            rows = cursor.fetchall()
            return rows
        except Error as e:
            print(f"Fehler beim Abrufen der Dosen: {e}")
            return None

    def __del__(self):
        """Schließt die Datenbankverbindung beim Löschen des Objekts."""
        if self.connection:
            self.connection.close()
            print("Verbindung zur SQLite-Datenbank geschlossen.")

# Testblock
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    db = Database("patchcontrol.db")
    db.create_tables()
    sys.exit(app.exec_())
