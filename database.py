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

    def create_table(self):
        """Erstellt die Tabelle für Netzwerk- und Telefondosen."""
        create_table_query = """
        CREATE TABLE IF NOT EXISTS dose (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            gebaeude TEXT NOT NULL,
            etage TEXT NOT NULL,
            raum TEXT NOT NULL,
            position INTEGER NOT NULL,
            bezeichnung TEXT NOT NULL UNIQUE,
            anschluss_typ TEXT CHECK(anschluss_typ IN ('Netzwerk', 'Telefonnetz')) NOT NULL,
            ziel TEXT NOT NULL,
            ziel_typ TEXT CHECK(ziel_typ IN ('Patchpanel', 'LSA-Leiste')) NOT NULL
        );
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(create_table_query)
            self.connection.commit()
            print("Tabelle 'dose' erfolgreich erstellt.")
        except Error as e:
            print(f"Fehler beim Erstellen der Tabelle: {e}")

    def add_dose(self, gebaeude, etage, raum, position, bezeichnung, anschluss_typ, ziel, ziel_typ):
        """Fügt eine neue Dose zur Tabelle hinzu."""
        insert_query = """
        INSERT INTO dose (gebaeude, etage, raum, position, bezeichnung, anschluss_typ, ziel, ziel_typ)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
        """
        try:
            cursor = self.connection.cursor()
            cursor.execute(insert_query, (gebaeude, etage, raum, position, bezeichnung, anschluss_typ, ziel, ziel_typ))
            self.connection.commit()
            print("Dose erfolgreich hinzugefügt.")
        except Error as e:
            print(f"Fehler beim Hinzufügen der Dose: {e}")

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

    def update_dose(self, dose_id, **kwargs):
        """Aktualisiert die Informationen einer Dose."""
        update_query = "UPDATE dose SET "
        update_query += ", ".join([f"{key} = ?" for key in kwargs.keys()])
        update_query += " WHERE id = ?;"
        params = list(kwargs.values()) + [dose_id]

        try:
            cursor = self.connection.cursor()
            cursor.execute(update_query, params)
            self.connection.commit()
            print("Dose erfolgreich aktualisiert.")
        except Error as e:
            print(f"Fehler beim Aktualisieren der Dose: {e}")

    def delete_dose(self, dose_id):
        """Löscht eine Dose anhand der ID."""
        delete_query = "DELETE FROM dose WHERE id = ?;"
        try:
            cursor = self.connection.cursor()
            cursor.execute(delete_query, (dose_id,))
            self.connection.commit()
            print("Dose erfolgreich gelöscht.")
        except Error as e:
            print(f"Fehler beim Löschen der Dose: {e}")

    def __del__(self):
        """Schließt die Datenbankverbindung beim Löschen des Objekts."""
        if self.connection:
            self.connection.close()
            print("Verbindung zur SQLite-Datenbank geschlossen.")

"""Der folgende Block sorgt dafür, dass der Code zu Testzwecken 
   nur ausgeführt wird, wenn die databse.py direkt als Skript gestartet wird."""

"""if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    db = Database("patchcontrol.db")
    sys.exit(app.exec_())
"""

