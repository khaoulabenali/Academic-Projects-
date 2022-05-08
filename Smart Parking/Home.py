import sys
import sqlite3
import random
import time
import string
from add import *
from take import *
from reserve import *
from reservedplace import *
from parking import *
from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5 import QtMultimedia as M

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.setGeometry(380, 220, 600, 320)
        self.setWindowTitle('Parking')
        self.setWindowIcon(QIcon('parking.ico'))
        self.setStyleSheet("background-color: rgb(205, 206, 255);")

        self.btn_add = QPushButton('PARK', self)
        self.btn_add.resize(120, 80)
        self.btn_add.setStyleSheet("background-color: rgb(255, 48, 207);\n"
                              "color: rgb(255, 255, 255);\n"
                              "font: 75 20pt 'MS Shell Dlg 2';")
        self.btn_add.clicked.connect(self.appeldialogue1)

        self.btn_take = QPushButton('GET MY \nCAR', self)
        self.btn_take.resize(120, 80)
        self.btn_take.move(0, 80)
        self.btn_take.setStyleSheet("background-color: rgb(0,255,0);\n"
                               "color: rgb(255, 255, 255);\n"
                               "font:  20pt 'MS Shell Dlg 2';")
        self.btn_take.clicked.connect(self.appeldialogue2)

        self.btn_Reserve = QPushButton('RESERVE', self)
        self.btn_Reserve.resize(120, 80)
        self.btn_Reserve.move(0, 160)
        self.btn_Reserve.setStyleSheet("background-color: rgb(170, 0, 255);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "font: 20pt 'MS Shell Dlg 2';")
        self.btn_Reserve.clicked.connect(self.appeldialogue3)

        self.btn_Reservedplace = QPushButton(' RESERVED \n  PLACE ', self)
        self.btn_Reservedplace.resize(120, 80)
        self.btn_Reservedplace.move(0, 240)
        self.btn_Reservedplace.setStyleSheet("background-color: rgb(241, 241, 120);\n"
                                        "color: rgb(255, 255, 255);\n"
                                        "font: 16pt 'MS Shell Dlg 2';")
        self.btn_Reservedplace.clicked.connect(self.appeldialogue4)

        self.pixmap1 = QPixmap('parking.jpg').scaled(480, 320)
        self.label1 = QLabel(self)
        self.label1.move(120, 0)
        self.label1.resize(480,320)
        self.label1.setPixmap(self.pixmap1)

        self.label = QLabel(self, text="WELCOME TO MANNOUBA PARKING")
        self.label.resize(390, 50)
        self.label.move(165, 120)
        self.label.setStyleSheet("font: 75 18pt 'MS Shell Dlg 2';\n"
                            "color: rgb(0, 0, 0);\n"
                            "background-color:rgb(255, 255, 255);\n"
                            "  border-radius: 8px;\n"
                            "font - family: Georgia, serif;\n"
                            "vertical - align: middle;")

        self.btn_parking = QPushButton('Take \n A Look',self )
        self.btn_parking.setGeometry(300, 200,100,60)
        self.btn_parking.setStyleSheet("font: 75 18pt 'MS Shell Dlg 2';\n"
                            "color: rgb(0,0,0);\n"
                            "background-color:rgb(10, 2, 255);\n"
                            "  border-radius: 8px;\n"
                            "font - family: Georgia, serif;\n"
                            "vertical - align: middle;")
        self.btn_parking.clicked.connect(self.appeldialogue5)

        self.url = QtCore.QUrl.fromLocalFile('music.mp3')
        self.content = M.QMediaContent(self.url)
        self.player = M.QMediaPlayer()
        self.player.setMedia(self.content)
        self.player.play()

    def appeldialogue1(self):
        dialogue1 = CustomDialog1(self)
        if dialogue1.exec_():
            print('')
        else :
            self.txt_marque = dialogue1.txt_mark.text()
            self.txt_number = dialogue1.txt_number.text()
            conn = sqlite3.connect('little.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT fmark,fnumber FROM Parking""")
            cursor.execute('DELETE FROM Parking WHERE fmark = ? AND fnumber = ? ', (self.txt_marque, self.txt_number))
            conn.commit()
            cursor.close()
            conn.close()
            conn = sqlite3.connect('big.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT fmark,fnumber FROM Parking""")
            cursor.execute('DELETE FROM Parking WHERE fmark = ? AND fnumber = ? ', (self.txt_marque, self.txt_number))
            conn.commit()
            cursor.close()
            conn.close()

    def appeldialogue2(self):
        dialogue2 = CustomDialog2(self)
        if dialogue2.exec_():
            print('')
        else:
            print('')
    def appeldialogue3(self):
        dialogue3 = CustomDialog3(self)
        if dialogue3.exec_():
            print('')
        else:
            self.txt_marque = dialogue3.txt_mark.text()
            self.txt_number = dialogue3.txt_number.text()
            conn = sqlite3.connect('little.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT fmark,fnumber FROM Parking""")
            cursor.execute('DELETE FROM Parking WHERE fmark = ? AND fnumber = ? ', (self.txt_marque, self.txt_number))
            conn.commit()
            cursor.close()
            conn.close()
            conn = sqlite3.connect('big.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT fmark,fnumber FROM Parking""")
            cursor.execute('DELETE FROM Parking WHERE fmark = ? AND fnumber = ? ', (self.txt_marque, self.txt_number))
            conn.commit()
            cursor.close()
            conn.close()

    def appeldialogue4(self):
        dialogue4 = CustomDialog4(self)
        if dialogue4.exec_():
            print('')
        else:
            self.txt_pass = dialogue4.txt_password.text()
            self.txt_number = dialogue4.txt_number.text()
            conn = sqlite3.connect('little.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT fmdp,fnumber FROM Parking""")
            cursor.execute("""UPDATE Parking SET fexists = ? WHERE fmdp = ? AND fnumber = ? """,(0, self.txt_pass, self.txt_number))
            conn.commit()
            cursor.close()
            conn.close()
            conn = sqlite3.connect('big.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT fmdp,fnumber FROM Parking""")
            cursor.execute("""UPDATE Parking SET fexists = ? WHERE fmdp = ? AND fnumber = ? """,(0, self.txt_pass, self.txt_number))
            conn.commit()
            cursor.close()
            conn.close()

    def appeldialogue5(self):
        dialogue5 = CustomDialog5(self)
        if dialogue5.exec_():
            print('')
        else:
            print('')


app = QApplication(sys.argv)
fen = MainWindow()
fen.show()
sys.exit(app.exec_())