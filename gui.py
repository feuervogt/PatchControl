from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QTableWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QWidget, QAbstractItemView, QLabel, QGridLayout
)
from PyQt5.QtGui import QColor, QPalette, QLinearGradient
from PyQt5.QtCore import Qt

class PatchControlGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PatchControl")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        # Hauptwidget und Layout
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(15, 5, 15, 15)

        # Hintergrund mit Farbverlauf
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#d35400"))
        gradient.setColorAt(0.6, QColor("#004d40"))
        palette.setBrush(QPalette.Window, gradient)
        self.setPalette(palette)

        # Überschrift
        title = QLabel("PatchControl - Verwaltung der Netzwerk- und Telefondosen")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 20px; font-weight: bold; color: white;")
        main_layout.addWidget(title)

        # Kachelbereich
        tile_layout = QGridLayout()
        tile_layout.setSpacing(10)

        # Kacheln von 1 bis 10
        for i in range(1, 11):
            tile_button = QPushButton(f"Kachel {i}")
            tile_button.setStyleSheet("""
                QPushButton {
                    background-color: #004d40;
                    color: white;
                    border-radius: 10px;
                    padding: 20px;
                    font-size: 16px;
                }
                QPushButton:hover {
                    background-color: #00796b;
                }
            """)
            tile_button.clicked.connect(lambda _, x=i: self.tile_clicked(x))
            tile_layout.addWidget(tile_button, (i - 1) // 5, (i - 1) % 5)

        main_layout.addLayout(tile_layout)

        # Tabelle zur Anzeige der Dosen
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["Gebäude/Etage/Raum", "Bezeichnung", "Typ", "Telefon/IP"])
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        main_layout.addWidget(self.table)

        # Buttons für Aktionen
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("Neue Dose hinzufügen")
        self.edit_button = QPushButton("Dose bearbeiten")
        self.delete_button = QPushButton("Dose löschen")
        self.close_button = QPushButton("Schließen")

        # Styling für Buttons
        for button in [self.add_button, self.edit_button, self.delete_button, self.close_button]:
            button.setStyleSheet("""
                QPushButton {
                    background-color: #004d40;
                    color: white;
                    border-radius: 5px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #00796b;
                }
            """)
            button_layout.addWidget(button)

        main_layout.addLayout(button_layout)

        # Signalverbindungen (Platzhalter für zukünftige Funktionen)
        self.add_button.clicked.connect(self.add_dose)
        self.edit_button.clicked.connect(self.edit_dose)
        self.delete_button.clicked.connect(self.delete_dose)
        self.close_button.clicked.connect(self.close)

    # Platzhaltermethoden für die Button-Funktionen
    def add_dose(self):
        print("Neue Dose hinzufügen")

    def edit_dose(self):
        print("Dose bearbeiten")

    def delete_dose(self):
        print("Dose löschen")

    def tile_clicked(self, tile_number):
        print(f"Kachel {tile_number} geklickt!")

# Anwendung starten
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = PatchControlGUI()
    window.show()
    sys.exit(app.exec_())
