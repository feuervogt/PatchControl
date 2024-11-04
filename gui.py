import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox, QPushButton, QLineEdit, QTextEdit, QSpacerItem, QSizePolicy, QGridLayout
)
from PyQt5.QtCore import Qt

class PatchControlGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PatchControl")
        self.setGeometry(100, 100, 800, 600)  # Standardgröße des Fensters festlegen
        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout()

        # Funktion zur Erstellung eines einheitlichen Eingabefeldes
        def create_input_field():
            line_edit = QLineEdit()
            line_edit.setFixedWidth(120)  # Eingabefeld auf eine feste Breite setzen
            return line_edit

        # Grid-Layout für die linke Spalte (um den freien Platz zu entfernen)
        left_column_layout = QGridLayout()
        left_column_layout.setContentsMargins(0, 0, 0, 0)  # Ränder auf 0 setzen
        left_column_layout.setSpacing(5)  # Abstand zwischen den Zellen reduzieren

        # Anschlussdose-Gruppe (oben links)
        anschlussdose_group = QGroupBox("Anschlussdose")
        anschlussdose_layout = QFormLayout()
        anschlussdose_layout.addRow("Gebäude:", create_input_field())
        anschlussdose_layout.addRow("Etage:", create_input_field())
        anschlussdose_layout.addRow("Raum:", create_input_field())
        anschlussdose_layout.addRow("Dose:", create_input_field())
        testfield_field = create_input_field()
        testfield_field.setAlignment(Qt.AlignRight)
        anschlussdose_layout.addRow("Test:", testfield_field)
        anschlussdose_group.setLayout(anschlussdose_layout)
        left_column_layout.addWidget(anschlussdose_group, 0, 0)  # Positioniert in der oberen linken Ecke

        # Anschlussinformation-Gruppe (oben rechts)
        anschlussinformation_group = QGroupBox("Anschlussinformation")
        anschlussinformation_layout = QFormLayout()
        anschlussinformation_layout.addRow("Aktiv:", create_input_field())
        anschlussinformation_layout.addRow("Aktuelle Durchwahl:", create_input_field())
        anschlussinformation_group.setLayout(anschlussinformation_layout)
        left_column_layout.addWidget(anschlussinformation_group, 0, 1)  # Positioniert in der oberen rechten Ecke

        # TK-Anlage-Gruppe (unten links)
        tkanlage_group = QGroupBox("TK-Anlage")
        tkanlage_layout = QFormLayout()
        tkanlage_layout.addRow("Verteilung:", create_input_field())
        tkanlage_layout.addRow("Bucht:", create_input_field())
        tkanlage_layout.addRow("Leiste:", create_input_field())
        tkanlage_layout.addRow("Stift:", create_input_field())
        tkanlage_layout.addRow("Knoten:", create_input_field())
        tkanlage_layout.addRow("Baugruppe:", create_input_field())
        tkanlage_layout.addRow("Leiterplatte:", create_input_field())
        tkanlage_layout.addRow("Geräteadresse:", create_input_field())
        tkanlage_group.setLayout(tkanlage_layout)
        left_column_layout.addWidget(tkanlage_group, 1, 0)  # Positioniert in der unteren linken Ecke

        # Unterverteiler-Gruppe (unten rechts)
        unterverteiler_group = QGroupBox("Unterverteiler")
        unterverteiler_layout = QVBoxLayout()
        for _ in range(4):  # Mehrere Reihen von Unterverteilern
            row_layout = QFormLayout()
            row_layout.addRow("Verteilung:", create_input_field())
            row_layout.addRow("Bucht:", create_input_field())
            row_layout.addRow("Leiste:", create_input_field())
            row_layout.addRow("Stift:", create_input_field())
            unterverteiler_layout.addLayout(row_layout)
        unterverteiler_group.setLayout(unterverteiler_layout)
        left_column_layout.addWidget(unterverteiler_group, 1, 1)  # Positioniert in der unteren rechten Ecke

        # Layout für die rechte Spalte (Buttons in zwei Spalten: Abfragen und Aktionen)
        button_layout = QVBoxLayout()  # Vertikales Layout, um den neuen Block "Platzhalter" oben einzufügen

        # Neuer Platzhalter-Block mit einem Beschreibungsfeld
        placeholder_group = QGroupBox("Platzhalter")
        placeholder_layout = QVBoxLayout()
        description_field = QTextEdit()
        description_field.setPlaceholderText("Beschreibung eingeben...")
        placeholder_layout.addWidget(description_field)  # Fügt das Beschreibungsfeld hinzu
        placeholder_group.setLayout(placeholder_layout)
        button_layout.addWidget(placeholder_group)  # Platzhalter füllt den oberen Raum aus

        # Horizontales Layout für "Abfragen" und "Aktionen"
        horizontal_buttons_layout = QHBoxLayout()

        # Abfrage-Buttons (Gruppe "Abfragen")
        query_buttons = QGroupBox("Abfragen")
        query_layout = QVBoxLayout()
        query_layout.setSpacing(3)  # Sehr geringer Abstand zwischen den Buttons
        query_layout.addWidget(QPushButton("Abfrage Dose"))
        query_layout.addWidget(QPushButton("Abfrage TK-Anlage"))
        query_layout.addWidget(QPushButton("Abfrage Unterverteilung"))
        query_layout.addWidget(QPushButton("Abfrage Rufnummer"))
        query_layout.addWidget(QPushButton("Historie Dose"))  # Der letzte Button bleibt am unteren Rand
        query_buttons.setLayout(query_layout)
        query_buttons.setFixedHeight(200)  # Reduzierte Höhe für Abfragen
        horizontal_buttons_layout.addWidget(query_buttons)

        # Aktions-Buttons (Gruppe "Aktionen")
        action_buttons = QGroupBox("Aktionen")
        action_layout = QVBoxLayout()
        action_layout.setSpacing(3)  # Sehr geringer Abstand zwischen den Buttons
        
        save_button = QPushButton("Speichern & Schließen")
        save_button.setFixedHeight(40)
        save_button.setStyleSheet("background-color: red; color: white;")

        insert_button = QPushButton("Informationen eintragen")
        insert_button.setFixedHeight(40)
        insert_button.setStyleSheet("background-color: green; color: white;")

        update_button = QPushButton("Informationen ändern")
        update_button.setFixedHeight(40)
        update_button.setStyleSheet("background-color: green; color: white;")

        edit_button = QPushButton("Tabellen bearbeiten")
        edit_button.setFixedHeight(40)
        edit_button.setStyleSheet("background-color: orange; color: white;")

        action_layout.addWidget(insert_button)
        action_layout.addWidget(update_button)
        action_layout.addWidget(edit_button)
        action_layout.addWidget(save_button)  # Der letzte Button bleibt am unteren Rand
        action_buttons.setLayout(action_layout)
        action_buttons.setFixedHeight(200)  # Reduzierte Höhe für Aktionen
        horizontal_buttons_layout.addWidget(action_buttons)  # Aktionen rechts neben Abfragen hinzufügen

        # Füge das horizontale Layout mit "Abfragen" und "Aktionen" dem button_layout hinzu
        button_layout.addLayout(horizontal_buttons_layout)

        # Hinzufügen aller Layouts zum Hauptlayout
        overall_layout = QHBoxLayout()
        overall_layout.addLayout(left_column_layout)  # Linkes Layout für die Felder
        overall_layout.addLayout(button_layout)       # Button-Spalte mit Platzhalter, Abfragen und Aktionen

        # Setzt das gesamte Layout für das Fenster
        self.setLayout(overall_layout)

# Hauptfunktion zum Ausführen der App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PatchControlGUI()
    window.show()
    sys.exit(app.exec_())
