import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()  # Wywołuje konstruktor klasy bazowej QWidget
        self.time_label = QLabel(self)  # Tworzy etykietę do wyświetlania czasu
        self.timer = QTimer(self)  # Tworzy timer, który będzie aktualizował zegar
        self.initUI()  # Wywołuje metodę odpowiedzialną za inicjalizację UI

    def initUI(self):
        self.setWindowTitle("Digital Clock")  # Ustawia tytuł okna
        self.setGeometry(600, 400, 300, 100)  # Ustawia rozmiar i pozycję okna (pozycja: 600x400, rozmiar: 300x100)

        vbox = QVBoxLayout()  # Tworzy layout pionowy
        vbox.addWidget(self.time_label)  # Dodaje etykietę do layoutu
        self.setLayout(vbox)  # Ustawia layout w głównym oknie

        self.time_label.setAlignment(Qt.AlignCenter)  # Ustawia wyrównanie tekstu w etykiecie na środek
        self.time_label.setStyleSheet("font-size: 150px;"  # Ustawia rozmiar czcionki na 150px
                                      "color: #5be629;"  # Ustawia kolor tekstu na zielony
                                      "background-color: black;")  # Ustawia tło na czarne

        # Ładowanie niestandardowej czcionki DS-DIGIT.TTF
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]  # Pobiera nazwę rodziny czcionki
        my_font = QFont(font_family, 150)  # Ustawia czcionkę z załadowanej rodziny i rozmiar 150
        self.time_label.setFont(my_font)  # Przypisuje tę czcionkę do etykiety

        self.timer.timeout.connect(self.update_time)  # Łączy sygnał timeout timera z metodą update_time
        self.timer.start(1000)  # Ustawia timer na wywoływanie update_time co 1000 ms (1 sekunda)

        self.update_time()  # Wywołuje metodę update_time, aby natychmiast zaktualizować czas przy uruchomieniu

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")  # Pobiera bieżący czas w formacie hh:mm:ss
        self.time_label.setText(current_time)  # Ustawia tekst etykiety na aktualny czas

if __name__ == "__main__":
    app = QApplication(sys.argv)  # Tworzy instancję aplikacji PyQt5
    clock = DigitalClock()  # Tworzy instancję klasy DigitalClock
    clock.show()  # Wyświetla okno zegara
    sys.exit(app.exec_())  # Uruchamia główną pętlę aplikacji (event loop)
