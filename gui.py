import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QGroupBox, QPushButton, QLineEdit, QTextEdit, QLabel, QSizePolicy, QFrame
)
from PyQt5.QtCore import Qt

class PatchControlGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PatchControl")
        self.setGeometry(100, 100, 800, 600)  # Standardgröße des Fensters festlegen
        self.initUI()

    def initUI(self):
        # Funktion zur Erstellung eines rechtsbündigen Eingabefeldes mit einheitlicher Breite
        def create_right_aligned_input_field():
            line_edit = QLineEdit()
            line_edit.setFixedWidth(120)  # Einheitliche Breite für alle Eingabefelder setzen
            line_edit.setAlignment(Qt.AlignRight)  # Rechtsbündig ausrichten
            return line_edit

        # Linke Spalte mit Anschlussdose, TK-Anlage und Hauptverteiler
        left_column_layout = QVBoxLayout()
        left_column_layout.setSpacing(10)

        # Anschlussdose-Gruppe
        anschlussdose_group = QGroupBox("Anschlussdose")
        anschlussdose_layout = QFormLayout()
        anschlussdose_layout.setLabelAlignment(Qt.AlignLeft)
        anschlussdose_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
        anschlussdose_layout.addRow("Gebäude:", create_right_aligned_input_field())
        anschlussdose_layout.addRow("Etage:", create_right_aligned_input_field())
        anschlussdose_layout.addRow("Raum:", create_right_aligned_input_field())
        anschlussdose_layout.addRow("Dose:", create_right_aligned_input_field())
        anschlussdose_layout.addRow("Test:", create_right_aligned_input_field())
        anschlussdose_group.setLayout(anschlussdose_layout)
        left_column_layout.addWidget(anschlussdose_group)

        # TK-Anlage-Gruppe
        tkanlage_group = QGroupBox("TK-Anlage")
        tkanlage_layout = QFormLayout()
        tkanlage_layout.setLabelAlignment(Qt.AlignLeft)
        tkanlage_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
        tkanlage_layout.addRow("Verteilung:", create_right_aligned_input_field())
        tkanlage_layout.addRow("Bucht:", create_right_aligned_input_field())
        tkanlage_layout.addRow("Leiste:", create_right_aligned_input_field())
        tkanlage_layout.addRow("Stift:", create_right_aligned_input_field())
        tkanlage_layout.addRow("Knoten:", create_right_aligned_input_field())
        tkanlage_layout.addRow("Baugruppe:", create_right_aligned_input_field())
        tkanlage_layout.addRow("Leiterplatte:", create_right_aligned_input_field())
        tkanlage_layout.addRow("Geräteadresse:", create_right_aligned_input_field())
        tkanlage_group.setLayout(tkanlage_layout)
        left_column_layout.addWidget(tkanlage_group)

        # Hauptverteiler-Gruppe
        hauptverteiler_group = QGroupBox("Hauptverteiler")
        hauptverteiler_layout = QFormLayout()
        hauptverteiler_layout.setLabelAlignment(Qt.AlignLeft)
        hauptverteiler_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
        hauptverteiler_layout.addRow("Verteilung:", create_right_aligned_input_field())
        hauptverteiler_layout.addRow("Bucht:", create_right_aligned_input_field())
        hauptverteiler_layout.addRow("Leiste:", create_right_aligned_input_field())
        hauptverteiler_layout.addRow("Stift:", create_right_aligned_input_field())
        hauptverteiler_group.setLayout(hauptverteiler_layout)
        left_column_layout.addWidget(hauptverteiler_group)

        # Mittlere und rechte Spalte bleiben unverändert
        # Mittlere Spalte mit Anschlussinformation und Unterverteiler
        middle_column_layout = QVBoxLayout()
        middle_column_layout.setSpacing(10)

        anschlussinformation_group = QGroupBox("Anschlussinformation")
        anschlussinformation_layout = QFormLayout()
        anschlussinformation_layout.setLabelAlignment(Qt.AlignLeft)
        anschlussinformation_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
        anschlussinformation_layout.addRow("Aktiv:", create_right_aligned_input_field())
        anschlussinformation_layout.addRow("Aktuelle Durchwahl:", create_right_aligned_input_field())
        anschlussinformation_group.setLayout(anschlussinformation_layout)
        middle_column_layout.addWidget(anschlussinformation_group)

        unterverteiler_group = QGroupBox("Unterverteiler")
        unterverteiler_layout = QVBoxLayout()
        for _ in range(4):
            row_layout = QFormLayout()
            row_layout.setLabelAlignment(Qt.AlignLeft)
            row_layout.setFormAlignment(Qt.AlignLeft | Qt.AlignTop)
            row_layout.addRow("Verteilung:", create_right_aligned_input_field())
            row_layout.addRow("Bucht:", create_right_aligned_input_field())
            row_layout.addRow("Leiste:", create_right_aligned_input_field())
            row_layout.addRow("Stift:", create_right_aligned_input_field())
            unterverteiler_layout.addLayout(row_layout)

            line = QFrame()
            line.setFrameShape(QFrame.HLine)
            line.setFrameShadow(QFrame.Sunken)
            unterverteiler_layout.addWidget(line)

        unterverteiler_group.setLayout(unterverteiler_layout)
        middle_column_layout.addWidget(unterverteiler_group)

        # Rechte Spalte mit Platzhalter, Abfragen und Aktionen
        button_layout = QVBoxLayout()
        button_layout.setSpacing(10)

        placeholder_group = QGroupBox("Platzhalter")
        placeholder_layout = QVBoxLayout()
        description_field = QTextEdit()
        description_field.setPlaceholderText("Beschreibung eingeben...")
        description_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        placeholder_layout.addWidget(description_field)

        explanation_label = QLabel("ankommend = Anschluss kommt vom Verteiler oder von der TK-Anlage\n"
                                   "abgehend = Anschluss geht zum nächsten Verteiler oder zur Dose")
        explanation_label.setWordWrap(True)
        placeholder_layout.addWidget(explanation_label)
        placeholder_group.setLayout(placeholder_layout)
        button_layout.addWidget(placeholder_group)

        query_buttons = QGroupBox("Abfragen")
        query_layout = QVBoxLayout()
        query_layout.setSpacing(3)
        query_layout.addWidget(QPushButton("Abfrage Dose"))
        query_layout.addWidget(QPushButton("Abfrage TK-Anlage"))
        query_layout.addWidget(QPushButton("Abfrage Unterverteilung"))
        query_layout.addWidget(QPushButton("Abfrage Rufnummer"))
        query_layout.addWidget(QPushButton("Historie Dose"))
        query_buttons.setLayout(query_layout)
        button_layout.addWidget(query_buttons)

        action_buttons = QGroupBox("Aktionen")
        action_layout = QVBoxLayout()
        action_layout.setSpacing(3)

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
        action_layout.addWidget(save_button)
        action_buttons.setLayout(action_layout)
        button_layout.addWidget(action_buttons)

        # Hauptlayout für das Fenster
        overall_layout = QHBoxLayout()
        overall_layout.addLayout(left_column_layout)
        overall_layout.addLayout(middle_column_layout)
        overall_layout.addLayout(button_layout)

        self.setLayout(overall_layout)

# Hauptfunktion zum Ausführen der App
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PatchControlGUI()
    window.show()
    sys.exit(app.exec_())
