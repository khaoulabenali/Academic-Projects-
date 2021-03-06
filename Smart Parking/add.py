from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import sqlite3
import random
import time
import string

class CustomDialog1(QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(500, 220, 480, 320)
        self.setWindowTitle('Parking')
        self.setWindowIcon(QIcon('parking.ico'))
        self.setStyleSheet("background-color: rgb(205, 206, 255);")

        self.txt_mark = QtWidgets.QLineEdit()
        self.txt_mark.setObjectName("txt_username")
        self.txt_mark.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    " border-radius: 8px;\n"
                                    " font-size: 20px;\n"
                                    "font-family: Georgia, serif;")
        self.txt_mark.setPlaceholderText("VEHICLE MARK")

        self.txt_number = QtWidgets.QLineEdit()
        self.txt_number.setObjectName("txt_number")
        self.txt_number.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      " border-radius: 8px;\n"
                                      " font-size: 20px;\n"
                                      "font-family: Georgia, serif;")
        self.txt_number.setPlaceholderText("SERIAL NUMBER")

        self.__littlecar = QtWidgets.QRadioButton("Little Car")
        self.__bigcar = QtWidgets.QRadioButton("Big Car")

        self.__littlecar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                       " border-radius: 8px;\n"
                                       " font-size: 20px;\n"
                                       "font-family: Georgia, serif;")
        self.__bigcar.setStyleSheet("color: rgb(0, 0, 0);\n"
                                    " border-radius: 8px;\n"
                                    " font-size: 20px;\n"
                                    "font-family: Georgia, serif;")

        self.btn_Add = QPushButton('ADD VEHICLE')
        self.btn_Add.setStyleSheet("font: 75 20pt 'MS Shell Dlg 2';\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color:rgb(85, 170, 255);\n"
                                    "border-radius: 8px;\n"
                                    "font - family: Georgia, serif;\n"
                                    "vertical - align: middle;")

        self.btn_Add.clicked.connect(self.database)

        self.QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(self.QBtn)
        self.buttonBox.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "background-color:rgb(10, 2, 255);\n"
                                    "border-radius: 8px;\n"
                                    "font - family: Georgia, serif;\n"
                                    "vertical - align: middle;")

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_mark)
        self.layout.addWidget(self.txt_number)
        self.layout.addWidget(self.__littlecar)
        self.layout.addWidget(self.__bigcar)
        self.layout.addWidget(self.btn_Add)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def pop_message(self, text):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle('Parking')
        msg.setWindowIcon(QIcon('parking.ico'))
        msg.setStyleSheet("background-color: rgb(205, 206, 255);")
        msg.setText("{}".format(text))
        msg.exec_()

    def database(self):
        little = self.__littlecar.isChecked()
        big = self.__bigcar.isChecked()
        txt_mark = self.txt_mark.text()
        txt_number = self.txt_number.text()
        res = True
        L = len(txt_number)
        for i in range(L):
            if not(txt_number[i].isdigit()):
                res = False
        if (little) and ( len(txt_mark) >= 1 ) and ( 1<= L < 5) and (res):
            self.__littlecar = "little"
            conn = sqlite3.connect('little.db')
            cursor = conn.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS Parking
                               (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                               fmark TEXT,
                               fnumber INTEGER,
                               flittle TEXT,
                               fmdp TEXT
                              fexists NUMERIC
                              ftime TEXT
                              fplace INTEGER)""")
            cursor.execute("""SELECT * FROM Parking""")
            if len(cursor.fetchall()) <= 9 :
                cursor.execute("""SELECT fplace FROM Parking""")
                place = 10
                Tab = [1,2,3,4,5,6,7,8,9,10]
                res = False
                k = 9
                for row in cursor.fetchall() :
                    if res :
                        k = k-1
                    for i in range(k) :
                        if Tab[i] == row[0]:
                            Tab.pop(i)
                            res = True

                for i in range(k):
                    if Tab[i] < place :
                        place = Tab[i]

                liste_char = string.ascii_letters + string.digits
                time_Add = time.asctime()
                passwd = ""
                for i in range(6):
                    passwd += liste_char[random.randint(0, len(liste_char) - 1)]
                cursor.execute(""" INSERT INTO Parking(fmark,fnumber,flittle,fmdp,fexists,ftime,fplace)
                                VALUES (?,?,?,?,?,?,?) """,
                                (txt_mark, txt_number, self.__littlecar, passwd, 1, time_Add, place))
                text = "WELCOME , YOU CAN PARK NOW IN PLACE N??" + str(place)+ "\n WOULD YOU PLEASE TAKE YOUR PASSWORD "
                self.pop_message(text)
                self.pop_message(passwd)
                conn.commit()
                cursor.close()
                conn.close()
            else:
                self.pop_message("SORRY OUR PARKING IS FULL")
        elif (big) and ( len(txt_mark) >= 1 ) and ( 1<= L < 5) and (res) :
            self.__bigcar = "big"
            conn = sqlite3.connect('big.db')
            cursor = conn.cursor()
            cursor.execute(""" CREATE TABLE IF NOT EXISTS Parking 
                               (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                               fmark TEXT,
                               fnumber INTEGER,
                               flittle TEXT,
                               fmdp TEXT
                               fexists NUMERIC
                               ftime TEXT
                               fplace INTEGER)""")
            cursor.execute("""SELECT * FROM Parking""")
            if len(cursor.fetchall()) <= 9:
                cursor.execute("""SELECT fplace FROM Parking""")
                place = 10
                Tab = [1, 2, 3, 4, 5, 6,7,8,9,10]
                res = False
                k = 9
                for row in cursor.fetchall():
                    if res:
                        k = k - 1
                    for i in range(k):
                        if Tab[i] == row[0]:
                            Tab.pop(i)
                            res = True

                for i in range(k):
                    if Tab[i] < place:
                        place = Tab[i]

                liste_char = string.ascii_letters + string.digits
                time_Add = time.asctime()
                passwd = ""
                for i in range(6):
                    passwd += liste_char[random.randint(0, len(liste_char) - 1)]
                cursor.execute(""" INSERT INTO Parking(fmark,fnumber,flittle,fmdp,fexists,ftime,fplace)
                                            VALUES (?,?,?,?,?,?,?) """,
                           (txt_mark, txt_number, self.__bigcar, passwd, 1, time_Add, place))
                text = "WELCOME , YOU CAN PARK NOW IN PLACE N??" + str(place) + "\n WOULD YOU PLEASE TAKE YOUR PASSWORD "
                self.pop_message(text)
                self.pop_message(passwd)
                conn.commit()
                cursor.close()
                conn.close()
            else:
                self.pop_message("SORRY ! OUR PARKING IS FULL")
        else:
            self.pop_message("ENTER VALID DATA!")

