import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,  QInputDialog, QLineEdit, QLabel, QGridLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt

class App(QWidget):
     
    def __init__(self):
        super().__init__()
        self.title = 'Kalkulator'
        self.left = 30
        self.top = 30
        self.width = 800
        self.height = 600
        self.interfejs()

    def interfejs(self):
        etykieta1 = QLabel("Liczba 1:", self)
        etykieta2 = QLabel("Liczba 2:", self)
        etykieta3 = QLabel("Wynik: ", self)

        ukladT = QGridLayout()
        ukladT.addWidget(etykieta1, 0, 0)
        ukladT.addWidget(etykieta2, 0, 1)
        ukladT.addWidget(etykieta3, 0, 2)

        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True
        self.wynikEdt.setToolTip('Wpisz <b>liczby</b> i wybierz działanie...')

        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)

        #Przyciski
        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        mnozBtn = QPushButton("&Mnóż", self)
        dzielBtn = QPushButton("&Dziel", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(mnozBtn)
        ukladH.addWidget(dzielBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)
        
        self.setLayout(ukladT)

        koniecBtn.clicked.connect(self.koniec)

        dodajBtn.clicked.connect(self.dzialanie)
        odejmijBtn.clicked.connect(self.dzialanie)
        mnozBtn.clicked.connect(self.dzialanie)
        dzielBtn.clicked.connect(self.dzialanie)


        self.show()
    
    def koniec(self):
        self.close()

    def closeEvent(self, event):
        odp = QMessageBox.question(
            self, 'Kominukat',
            "Czy na pewno chcesz zamknac program?",
            QMessageBox.Yes | QMessageBox.No)

        if odp == QMessageBox.Yes:
            event.accept()
        else: 
            event.ignore()
    
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    
    def dzialanie(self):
        
        nadawca = self.sender()

        try:
            liczba1 = float(self.liczba1Edt.text())
            liczba2 = float(self.liczba2Edt.text())
            wynik = ""

            if nadawca.text() == "&Dodaj":
                wynik = liczba1 + liczba2
            if nadawca.text() == "&Odejmij":
                wynik = liczba1 - liczba2
            if nadawca.text() == "&Mnóż":
                wynik = liczba1 * liczba2
            else: #dzielenie
                try:
                    wynik = round(liczba1 / liczba2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Błąd", "Nie można dzielić przez zero!")
                    return

            self.wynikEdt.setText(str(wynik))

        except ValueError:
            QMessageBox.warning(self, "Błąd", "Błędne dane", QMessageBox.Ok)

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())