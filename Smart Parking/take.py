from PyQt5.QtWidgets import *
import PyQt5
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import time
import datetime
import sqlite3

class CustomDialog2(QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(500, 220, 480, 320)
        self.setWindowTitle('Parking')
        self.setWindowIcon(QIcon('parking.ico'))
        self.setStyleSheet("background-color: rgb(205, 206, 255);")

        self.txt_number = QtWidgets.QLineEdit()
        self.txt_number.setObjectName("txt_number")
        self.txt_number.setStyleSheet("color: rgb(0, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      " border-radius: 8px;\n"
                                      " font-size: 20px;\n"
                                      "font-family: Georgia, serif;")
        self.txt_number.setPlaceholderText("SERIAL NUMBER")

        self.txt_password = QtWidgets.QLineEdit()
        self.txt_password.setObjectName("txt_password")
        self.txt_password.setStyleSheet("color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);\n"
                                        " border-radius: 8px;\n"
                                        " font-size: 20px;\n"
                                        "font-family: Georgia, serif;")
        self.txt_password.setPlaceholderText("PASSWORD")
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)

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

        self.btn_submit = QtWidgets.QPushButton()
        self.btn_submit.setStyleSheet("font: 75 20pt 'MS Shell Dlg 2';\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(85, 170, 255);\n"
                                      "  border-radius: 8px;\n"
                                      "font - family: Georgia, serif;\n"
                                      "vertical - align: middle;")
        self.btn_submit.setText("GET MY CAR")
        self.btn_submit.setObjectName("btn_submit")
        self.btn_submit.clicked.connect(self.database)

        self.btn_mdp = QtWidgets.QPushButton()
        self.btn_mdp.setStyleSheet("font: 75 20pt 'MS Shell Dlg 2';\n"
                                      "color: rgb(255, 255, 255);\n"
                                      "background-color: rgb(84, 92, 255);\n"
                                      "  border-radius: 8px;\n"
                                      "font - family: Georgia, serif;\n"
                                      "vertical - align: middle;")
        self.btn_mdp.setText("PASSWORD FORGOTTEN ")
        self.btn_mdp.setObjectName("btn_submit")
        self.btn_mdp.clicked.connect(self.password)


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
        self.layout.addWidget(self.txt_number)
        self.layout.addWidget(self.txt_password)
        self.layout.addWidget(self.__littlecar)
        self.layout.addWidget(self.__bigcar)
        self.layout.addWidget(self.btn_submit)
        self.layout.addWidget(self.btn_mdp)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

    def password (self):
        self.pop_message("PLEASE GO TO THE ADMINISTRATION  \n TO RESOLVE THIS PROBLEM ")

    def translate (self,text):
        if text == "Jan":
            return(1)
        elif text == "Feb":
            return(2)
        elif text == "Mar":
            return(3)
        elif text == "Apr":
            return(4)
        elif text == "May":
            return(5)
        elif text == "Jun":
            return(6)
        elif text == "Jul":
            return(7)
        elif text == "Aug":
            return(8)
        elif text == "Sep":
            return(9)
        elif text == "Oct":
            return(10)
        elif text == "Nov":
            return(11)
        else:
            return(12)


    def pop_message(self, text):
        msg = PyQt5.QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.setWindowTitle('Parking')
        msg.setStyleSheet("background-color: rgb(205, 206, 255);")
        msg.setWindowIcon(QIcon('parking.ico'))
        msg.exec_()

    def database(self):
        little = self.__littlecar.isChecked()
        big = self.__bigcar.isChecked()
        txt_number = self.txt_number.text()
        txt_password = self.txt_password.text()
        if little:
            res = False
            conn = sqlite3.connect('little.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT fnumber,fmdp,ftime FROM Parking""")
            for row in cursor.fetchall():
                if (row[0] == txt_number) and (row[1] == txt_password) :
                    cursor.execute('DELETE FROM Parking WHERE fnumber = ? AND fmdp = ? ', (txt_number,txt_password))
                    time_Add = str(row[2])
                    conn.commit()
                    res = True
            if res :
                time_take = str(time.asctime())
                m1=self.translate(time_Add[4:7])
                m2 = self.translate(time_take[4:7])
                start = datetime.datetime(year=int(time_Add[20:24]), month=m1, day=int(time_Add[8:10]), hour=int(time_Add[11:13]))
                end = datetime.datetime(year=int(time_take[20:24]), month=m2, day=int(time_take[8:10]), hour=int(time_take[11:13]))
                diff = str(end - start)
                if len(diff) == 16 :
                    Payment = ((int(diff[0:2]) * 24) + (int(diff[9])))*2
                else:
                    Payment = (int(diff[0])+1)*2
                text = "WELCOME, YOU CAN TAKE YOUR CAR !\n BUT FIRST YOU HAVE TO PAY "+str(Payment)+" Dinars"
                self.pop_message(text)
            else :
                self.pop_message("ENTER VALID DATA !")
        elif big:
            res = False
            conn = sqlite3.connect('big.db')
            cursor = conn.cursor()
            cursor.execute("""SELECT fnumber,fmdp,ftime FROM Parking""")
            for row in cursor.fetchall():
                if (row[0] == txt_number) and (row[1] == txt_password) :
                    cursor.execute('DELETE FROM Parking WHERE fnumber = ? AND fmdp = ?', (txt_number,txt_password))
                    time_Add = row[2]
                    conn.commit()
                    res = True
            if res :
                time_take = str(time.asctime())
                m1 = self.translate(time_Add[4:7])
                m2 = self.translate(time_take[4:7])
                start = datetime.datetime(year=int(time_Add[20:24]), month=m1, day=int(time_Add[8:10]),
                                          hour=int(time_Add[11:13]))
                end = datetime.datetime(year=int(time_take[20:24]), month=m2, day=int(time_take[8:10]),
                                        hour=int(time_take[11:13]))
                diff = str(end - start)
                if len(diff) == 16:
                    Payment = ((int(diff[0:2]) * 24) + (int(diff[9]))) * 2
                else:
                    Payment = (int(diff[0]) + 1) * 2
                text = "WELCOME, YOU CAN TAKE YOUR CAR !\n BUT FIRST YOU HAVE TO PAY " + str(Payment) + " Dinars"
                self.pop_message(text)
            else:
                self.pop_message("ENTER VALID DATA !")
        else:
            self.pop_message("ENTER VALID DATA !")
