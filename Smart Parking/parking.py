from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
import sqlite3

class CustomDialog5(QDialog):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setGeometry(500, 220, 480, 320)
        self.setWindowTitle('Parking')
        self.setWindowIcon(QIcon('parking.ico'))
        self.setStyleSheet("background-color: rgb(205, 206, 255);")

        self.pixmap = QPixmap('parking1.png').scaled(480, 280)
        self.label = QLabel(self)
        self.label.resize(480, 280)
        self.label.setPixmap(self.pixmap)

        self.label1 = QLabel('   10',self)
        self.label1.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color:rgb(0, 170, 0);\n"
                                           "border-radius: 8px;\n"
                                           "font - family: Georgia, serif;\n"
                                           "text-align: center;")
        self.label1.setGeometry(43,15,60,40)
        self.label2 = QLabel('   9', self)
        self.label2.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label2.setGeometry(130,15,60,40)
        self.label3 = QLabel('   8', self)
        self.label3.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label3.setGeometry(217,15,60,40)
        self.label4 = QLabel('   7', self)
        self.label4.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label4.setGeometry(304, 15, 60, 40)
        self.label5 = QLabel('   6', self)
        self.label5.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label5.setGeometry(388, 15, 60, 40)
        self.label6 = QLabel('   1', self)
        self.label6.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label6.setGeometry(43,80 , 60, 40)
        self.label7 = QLabel('   2', self)
        self.label7.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label7.setGeometry(130, 80, 60, 40)
        self.label8 = QLabel('   3', self)
        self.label8.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label8.setGeometry(217, 80,60, 40)
        self.label9 = QLabel('   4', self)
        self.label9.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label9.setGeometry(304, 80, 60, 40)
        self.label10 = QLabel('   5', self)
        self.label10.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label10.setGeometry(388, 80, 60, 40)
        self.label11 = QLabel('   1', self)
        self.label11.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label11.setGeometry(43, 160, 60, 40)
        self.label12 = QLabel('   2', self)
        self.label12.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label12.setGeometry(130, 160, 60, 40)
        self.label13 = QLabel('   3', self)
        self.label13.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label13.setGeometry(217, 160, 60, 40)
        self.label14 = QLabel('   4', self)
        self.label14.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                           "color: rgb(255, 255, 255);\n"
                                           "background-color:rgb(0, 170, 0);\n"
                                           "border-radius: 8px;\n"
                                           "font - family: Georgia, serif;\n"
                                           "text-align: center;")
        self.label14.setGeometry(304, 160, 60, 40)
        self.label15 = QLabel('   5', self)
        self.label15.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label15.setGeometry(388, 160, 60, 40)
        self.label16 = QLabel('   10', self)
        self.label16.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label16.setGeometry(43, 222, 60, 40)
        self.label17 = QLabel('   9', self)
        self.label17.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label17.setGeometry(130, 222, 60, 40)
        self.label18 = QLabel('   8', self)
        self.label18.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label18.setGeometry(217, 222, 60, 40)
        self.label19 = QLabel('   7', self)
        self.label19.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label19.setGeometry(304, 222, 60, 40)
        self.label20 = QLabel('   6', self)
        self.label20.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "font - family: Georgia, serif;\n"
                                  "text-align: center;")
        self.label20.setGeometry(388, 222, 60, 40)

        self.pixmap1 = QPixmap('parking3.png').scaled(32, 110)
        self.label_1 = QLabel(self)
        self.label_1.setGeometry(-5,15,32, 110)
        self.label_1.setPixmap(self.pixmap1)

        self.pixmap2 = QPixmap('parking2.png').scaled(32, 110)
        self.label_2 = QLabel(self)
        self.label_2.setGeometry(-5,160,32, 110)
        self.label_2.setPixmap(self.pixmap2)

        self.QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(self.QBtn)
        self.buttonBox.setStyleSheet("font: 20 20pt 'MS Shell Dlg 2';\n"
                                     "color: rgb(255, 255, 255);\n"
                                     "background-color:black;\n"
                                     "border-radius: 8px;\n"
                                     "font - family: Georgia, serif;\n"
                                     "vertical - align: middle;")

        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.flèche = QCommandLinkButton('',self)
        self.flèche.move(10,120)
        self.flèche = QCommandLinkButton('', self)
        self.flèche.move(120, 120)
        self.flèche = QCommandLinkButton('', self)
        self.flèche.move(230, 120)
        self.flèche = QCommandLinkButton('', self)
        self.flèche.move(340, 120)
        self.flèche = QCommandLinkButton('', self)
        self.flèche.move(410, 120)

        self.pixmap3 = QPixmap('flèche1.png').scaled(20, 30)
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(465, 30, 20, 30)
        self.label_3.setPixmap(self.pixmap3)

        self.pixmap4 = QPixmap('flèche1.png').scaled(20, 30)
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(465, 110, 20, 30)
        self.label_4.setPixmap(self.pixmap4)

        self.pixmap3 = QPixmap('flèche2.png').scaled(20, 30)
        self.label_3 = QLabel(self)
        self.label_3.setGeometry(455, 150, 20, 30)
        self.label_3.setPixmap(self.pixmap3)

        self.pixmap4 = QPixmap('flèche2.png').scaled(20, 30)
        self.label_4 = QLabel(self)
        self.label_4.setGeometry(455, 230, 20, 30)
        self.label_4.setPixmap(self.pixmap4)


        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 270, 480, 50))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout.addWidget(self.buttonBox)

        self.label_reserved = QLabel('  RESERVED', self)
        self.label_reserved.setGeometry(135, 280, 60, 20)
        self.label_reserved.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color:rgb(85, 85, 255);\n"
                                      "border-radius: 8px;\n"
                                      "text-align: center;")
        self.label_occupied = QLabel(' OCCUPIED', self)
        self.label_occupied.setGeometry(70, 280, 60, 20)
        self.label_occupied.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "background-color:rgb(255, 0, 0);\n"
                                      "border-radius: 8px;\n"
                                      "text-align: center;")
        self.label_free = QLabel('      FREE', self)
        self.label_free.setGeometry(5, 280, 60, 20)
        self.label_free.setStyleSheet("color: rgb(255, 255, 255);\n"
                                  "background-color:rgb(0, 170, 0);\n"
                                  "border-radius: 8px;\n"
                                  "text-align: center;")

        self.Tab_Little_Cars = [self.label1,self.label2,self.label3,self.label4,self.label5,self.label6,self.label7,self.label8,self.label9,self.label10]
        self.Tab_Big_Cars = [self.label11,self.label12,self.label13,self.label14,self.label15,self.label16,self.label17,self.label18,self.label19,self.label20]

        conn = sqlite3.connect('little.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT fplace,fexists FROM Parking""")
        for i in range(10):
            for row in cursor.fetchall():
                if row[0] == int(self.Tab_Little_Cars[i].text()):
                    if row[1] == 1 :
                        self.Tab_Little_Cars[i].setStyleSheet("background-color:rgb(255, 0, 0);"
                                                              "font: 20 20pt 'MS Shell Dlg 2';\n"
                                                        "color: rgb(255, 255, 255);\n"
                                                        "border-radius: 8px;\n"
                                                        "font - family: Georgia, serif;\n"
                                                        "text-align: center;")
                    else :
                        self.Tab_Little_Cars[i].setStyleSheet("background-color:rgb(85, 85, 255);"
                                                              "font: 20 20pt 'MS Shell Dlg 2';\n"
                                                              "color: rgb(255, 255, 255);\n"
                                                              "border-radius: 8px;\n"
                                                              "font - family: Georgia, serif;\n"
                                                              "text-align: center;")

            cursor.execute("""SELECT fplace,fexists FROM Parking""")
        conn.commit()
        cursor.close()
        conn.close()
        conn = sqlite3.connect('big.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT fplace,fexists FROM Parking""")
        for i in range(10):
            for row in cursor.fetchall():
                if row[0] == int(self.Tab_Big_Cars[i].text()):
                    if row[1] == 1 :
                        self.Tab_Big_Cars[i].setStyleSheet("background-color:rgb(255, 0, 0);"
                                                              "font: 20 20pt 'MS Shell Dlg 2';\n"
                                                        "color: rgb(255, 255, 255);\n"
                                                        "border-radius: 8px;\n"
                                                        "font - family: Georgia, serif;\n"
                                                        "text-align: center;")
                    else :
                        self.Tab_Big_Cars[i].setStyleSheet("background-color:rgb(85, 85, 255);"
                                                              "font: 20 20pt 'MS Shell Dlg 2';\n"
                                                              "color: rgb(255, 255, 255);\n"
                                                              "border-radius: 8px;\n"
                                                              "font - family: Georgia, serif;\n"
                                                              "text-align: center;")
            cursor.execute("""SELECT fplace,fexists FROM Parking""")
        conn.commit()
        cursor.close()
        conn.close()

