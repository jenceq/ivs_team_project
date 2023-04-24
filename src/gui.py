""" @package gui
    @author: Jan Lipenský (xlipen02)
    @brief Grafické prostředí pro knihovnu math_lib
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import QUrl
# Import knihovny math_lib
from math_lib import math_lib
m_lib=math_lib()


class Ui_Kalcoolacka(object):
    def setupUi(self, Kalcoolacka):
        Kalcoolacka.setObjectName("Kalcoolacka")
        Kalcoolacka.resize(511, 675)
        Kalcoolacka.setMaximumSize(QtCore.QSize(511,675))
        Kalcoolacka.setMinimumSize(QtCore.QSize(511,675))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        Kalcoolacka.setFont(font)
        Kalcoolacka.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        Kalcoolacka.setAutoFillBackground(False)
        Kalcoolacka.setStyleSheet("background-color: rgb(80, 92, 104);")
        Kalcoolacka.setTabShape(QtWidgets.QTabWidget.Rounded)
        Kalcoolacka.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.centralwidget = QtWidgets.QWidget(Kalcoolacka)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("1"))
        self.button1.setGeometry(QtCore.QRect(0, 450, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button1.setFont(font)
        self.button1.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button1.setObjectName("button1")
        self.buttonGroup = QtWidgets.QButtonGroup(Kalcoolacka)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.button1)
        self.button2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("2"))
        self.button2.setGeometry(QtCore.QRect(100, 450, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button2.setFont(font)
        self.button2.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button2.setObjectName("button2")
        self.buttonGroup.addButton(self.button2)
        self.button3 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("3"))
        self.button3.setGeometry(QtCore.QRect(200, 450, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button3.setFont(font)
        self.button3.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button3.setObjectName("button3")
        self.buttonGroup.addButton(self.button3)
        self.button4 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("4"))
        self.button4.setGeometry(QtCore.QRect(0, 350, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button4.setFont(font)
        self.button4.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button4.setObjectName("button4")
        self.buttonGroup.addButton(self.button4)
        self.button5 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("5"))
        self.button5.setGeometry(QtCore.QRect(100, 350, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button5.setFont(font)
        self.button5.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button5.setObjectName("button5")
        self.buttonGroup.addButton(self.button5)
        self.button6 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("6"))
        self.button6.setGeometry(QtCore.QRect(200, 350, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button6.setFont(font)
        self.button6.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button6.setObjectName("button6")
        self.buttonGroup.addButton(self.button6)
        self.button7 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("7"))
        self.button7.setGeometry(QtCore.QRect(0, 250, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button7.setFont(font)
        self.button7.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button7.setObjectName("button7")
        self.buttonGroup.addButton(self.button7)
        self.button8 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("8"))
        self.button8.setGeometry(QtCore.QRect(100, 250, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button8.setFont(font)
        self.button8.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button8.setObjectName("button8")
        self.buttonGroup.addButton(self.button8)
        self.button9 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("9"))
        self.button9.setGeometry(QtCore.QRect(200, 250, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button9.setFont(font)
        self.button9.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button9.setObjectName("button9")
        self.buttonGroup.addButton(self.button9)

        self.button0 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("0"))
        self.button0.setGeometry(QtCore.QRect(100, 550, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.button0.setFont(font)
        self.button0.setStyleSheet("background-color: rgb(91, 106, 125);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.button0.setObjectName("button0")
        self.buttonGroup.addButton(self.button0)
        self.buttoncomma = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress(","))
        self.buttoncomma.setGeometry(QtCore.QRect(0, 550, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.buttoncomma.setFont(font)
        self.buttoncomma.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(55, 67, 83);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttoncomma.setObjectName("buttoncomma")
        self.buttonGroup.addButton(self.buttoncomma)
        self.buttonEquals = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("="))
        self.buttonEquals.setGeometry(QtCore.QRect(201, 550, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.buttonEquals.setFont(font)
        self.buttonEquals.setStyleSheet("background-color: rgb(32, 203, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 32, 174, 255), stop:1 rgba(255, 100, 63, 255));border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonEquals.setObjectName("buttonEquals")
        self.buttonGroup_2 = QtWidgets.QButtonGroup(Kalcoolacka)
        self.buttonGroup_2.setObjectName("buttonGroup_2")
        self.buttonGroup_2.addButton(self.buttonEquals)
        self.buttonPrime = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("P"))
        self.buttonPrime.setGeometry(QtCore.QRect(400, 150, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonPrime.setFont(font)
        self.buttonPrime.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonPrime.setObjectName("buttonPrime")
        self.buttonGroup_2.addButton(self.buttonPrime)
        self.buttonPlus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("+"))
        self.buttonPlus.setGeometry(QtCore.QRect(300, 450, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonPlus.setFont(font)
        self.buttonPlus.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonPlus.setObjectName("buttonPlus")
        self.buttonGroup_2.addButton(self.buttonPlus)
        self.buttonMinus = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("-"))
        self.buttonMinus.setGeometry(QtCore.QRect(300, 350, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonMinus.setFont(font)
        self.buttonMinus.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonMinus.setObjectName("buttonMinus")
        self.buttonGroup_2.addButton(self.buttonMinus)
        self.buttonMultiply = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("*"))
        self.buttonMultiply.setGeometry(QtCore.QRect(300, 250, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonMultiply.setFont(font)
        self.buttonMultiply.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonMultiply.setObjectName("buttonMultiply")
        self.buttonGroup_2.addButton(self.buttonMultiply)
        self.buttonDivide = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("/"))
        self.buttonDivide.setGeometry(QtCore.QRect(300, 150, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonDivide.setFont(font)
        self.buttonDivide.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonDivide.setObjectName("buttonDivide")
        self.buttonGroup_2.addButton(self.buttonDivide)
        self.buttonClear = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("C"))
        self.buttonClear.setGeometry(QtCore.QRect(0, 150, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Light")
        font.setPointSize(20)
        font.setItalic(True)
        font.setUnderline(False)
        self.buttonClear.setFont(font)
        self.buttonClear.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonClear.setObjectName("buttonClear")
        self.buttonGroup_3 = QtWidgets.QButtonGroup(Kalcoolacka)
        self.buttonGroup_3.setObjectName("buttonGroup_3")
        self.buttonGroup_3.addButton(self.buttonClear)
        self.buttonRoot = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("√"))
        self.buttonRoot.setGeometry(QtCore.QRect(400, 450, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonRoot.setFont(font)
        self.buttonRoot.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonRoot.setObjectName("buttonRoot")
        self.buttonGroup_2.addButton(self.buttonRoot)
        self.buttonFact = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("!"))
        self.buttonFact.setGeometry(QtCore.QRect(400, 350, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonFact.setFont(font)
        self.buttonFact.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonFact.setObjectName("buttonFact")
        self.buttonGroup_2.addButton(self.buttonFact)
        self.buttonPower2 = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("^2"))
        self.buttonPower2.setGeometry(QtCore.QRect(400, 550, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonPower2.setFont(font)
        self.buttonPower2.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonPower2.setObjectName("buttonPower2")
        self.buttonGroup_2.addButton(self.buttonPower2)
        self.buttonPowerOf = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("^"))
        self.buttonPowerOf.setGeometry(QtCore.QRect(400, 250, 111, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Semibold")
        font.setPointSize(18)
        self.buttonPowerOf.setFont(font)
        self.buttonPowerOf.setStyleSheet("background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170);")
        self.buttonPowerOf.setObjectName("buttonPowerOf")
        self.buttonGroup_2.addButton(self.buttonPowerOf)
        self.buttonDel = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.buttonPress("DEL"))
        self.buttonDel.setGeometry(QtCore.QRect(200, 150, 101, 101))
        font = QtGui.QFont()
        font.setFamily("Lato Light")
        font.setPointSize(20)
        font.setItalic(True)
        font.setUnderline(False)
        self.buttonDel.setFont(font)
        self.buttonDel.setStyleSheet("\n"
"background-color: rgb(55, 67, 83);\n"
"color: rgb(255, 255, 255);border-style: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(124, 145, 170,);")
        self.buttonDel.setObjectName("buttonDel")
        self.vysledek_bar = QtWidgets.QLineEdit(self.centralwidget)
        self.vysledek_bar.setGeometry(QtCore.QRect(0, -10, 511, 161))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(24)
        self.vysledek_bar.setFont(font)
        self.vysledek_bar.setStyleSheet("background-color: rgb(80, 92, 104);\n"
"color: rgb(255, 255, 255);\n"
"padding-bottom: 25px;\n"
"border-style: solid;\n"
"border-width: 3px;\n"
"border-color: rgb(124, 145, 170);")
        self.vysledek_bar.setInputMask("")
        self.vysledek_bar.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing)
        self.vysledek_bar.setClearButtonEnabled(False)
        regex = QtCore.QRegExp("[0-9+-/*,!^√\\s]*")
        self.vysledek_bar.setValidator(QtGui.QRegExpValidator(regex))
        self.vysledek_bar.setObjectName("vysledek_bar")
        self.pocitani = QtWidgets.QLineEdit(self.centralwidget)
        self.pocitani.setGeometry(QtCore.QRect(10, 10, 491, 71))
        font = QtGui.QFont()
        font.setFamily("Montserrat Medium")
        font.setPointSize(24)
        self.pocitani.setFont(font)
        self.pocitani.setStyleSheet("background-color: rgb(80, 92, 104);\n"
                                    "color: rgb(255, 255, 255);\n"
                                    "padding-bottom: 25px;\n"
                                    "border-style: none;\n")
        self.pocitani.setInputMask("")
        self.pocitani.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing)
        self.pocitani.setClearButtonEnabled(False)
        self.pocitani.setValidator(QtGui.QRegExpValidator(regex))
        self.pocitani.setObjectName("pocitani")
        self.buttonHelp = QtWidgets.QPushButton(self.centralwidget)
        self.buttonHelp.clicked.connect(self.openHelp)
        self.buttonHelp.setGeometry(QtCore.QRect(10, 10, 30, 30))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(17)
        self.buttonHelp.setFont(font)
        self.buttonHelp.setStyleSheet("background-color: rgb(91, 106, 125);\n"
                                      "color: rgb(255, 255, 255);border-style: solid;\n"
                                      "border-width: 1px;\n"
                                      "border-color: rgb(124, 145, 170);")
        self.buttonHelp.setObjectName("buttonHelp")
        Kalcoolacka.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Kalcoolacka)
        self.statusbar.setObjectName("statusbar")
        Kalcoolacka.setStatusBar(self.statusbar)

        self.retranslateUi(Kalcoolacka)
        QtCore.QMetaObject.connectSlotsByName(Kalcoolacka)

    def retranslateUi(self, Kalcoolacka):
        _translate = QtCore.QCoreApplication.translate
        Kalcoolacka.setWindowTitle(_translate("Kalcoolacka", "Kalcoolacka"))
        Kalcoolacka.setWindowIcon(QtGui.QIcon("D:/Documents/GitHub/ivs_team_project/src/images.png"))
        self.button1.setText(_translate("Kalcoolacka", "1"))
        self.button2.setText(_translate("Kalcoolacka", "2"))
        self.button3.setText(_translate("Kalcoolacka", "3"))
        self.button4.setText(_translate("Kalcoolacka", "4"))
        self.button5.setText(_translate("Kalcoolacka", "5"))
        self.button6.setText(_translate("Kalcoolacka", "6"))
        self.button7.setText(_translate("Kalcoolacka", "7"))
        self.button8.setText(_translate("Kalcoolacka", "8"))
        self.button9.setText(_translate("Kalcoolacka", "9"))
        self.buttonHelp.setText(_translate("Kalcoolacka", "?"))
        self.button0.setText(_translate("Kalcoolacka", "0"))
        self.buttoncomma.setText(_translate("Kalcoolacka", ","))
        self.buttonEquals.setText(_translate("Kalcoolacka", "="))
        self.buttonPrime.setText(_translate("Kalcoolacka", "P"))
        self.buttonPlus.setText(_translate("Kalcoolacka", "+"))
        self.buttonMinus.setText(_translate("Kalcoolacka", "-"))
        self.buttonMultiply.setText(_translate("Kalcoolacka", "×"))
        self.buttonDivide.setText(_translate("Kalcoolacka", "÷"))
        self.buttonClear.setText(_translate("Kalcoolacka", "C"))
        self.buttonRoot.setText(_translate("Kalcoolacka", "√ "))
        self.buttonFact.setText(_translate("Kalcoolacka", "!"))
        self.buttonPower2.setText(_translate("Kalcoolacka", "x²"))
        self.buttonPowerOf.setText(_translate("Kalcoolacka", "^"))
        self.buttonDel.setText(_translate("Kalcoolacka", "DEL"))
        self.vysledek_bar.setText(_translate("Kalcoolacka", ""))
        self.pocitani.setText(_translate("Kalcoolacka", ""))





    def __init__(self):
        self.vysledek_flag = 0


    """
    @brief Metody zajišťující funkčnost kalkulačky
    @param self 
    @param pressed Zmáčknutý button
    """

    def buttonPress(self, pressed):
        # Pokud je výsledek vypočítán a zmáčknuto nějaké tlačítko, zresetuj kalkulačku
        if self.vysledek_flag == 1:
            self.vysledek_bar.setText("")
            self.pocitani.setText("")
            self.vysledek_flag = 0
        # Pokud je zmáčknuto C, zresetuj kalkulačku
        if pressed == "C":
            self.vysledek_bar.setText("")
            self.pocitani.setText("")
        else:
            # Pokud byl použit Prime Checker, poté co je zmáčknuto nějaké tlačítko, smaž zprávu o výsledku
            if self.vysledek_bar.text() == "is Prime." or self.vysledek_bar.text() == "is NOT Prime." or self.vysledek_bar.text() == "Not a natural number.":
                self.pocitani.setText("")
                self.vysledek_bar.setText("")
            # Psaní stringu do kalkulačky
            self.pocitani.setText(f'{self.pocitani.text()}{pressed}')
        # Pokud je zmáčknut DEL, smaž 4 poslední znaky - xDEL
        if pressed == "DEL":
            self.pocitani.setText(self.pocitani.text()[:-4])
        # Pokud je zmáčknuto =, zadaný string je vypočítán pomocí math_lib funkce solve
        if pressed == "=":
            vysledek = self.pocitani.text()
            vysledek = vysledek[:-1]

            try:
                vysledek = m_lib.solve(vysledek)
            except ZeroDivisionError:
                self.pocitani.setText(self.pocitani.text()[:-1])
                self.vysledek_bar.setText("You cant divide by zero.")
                return
            except ValueError as errorMes:
                if str(errorMes) == "Math Error":
                    self.pocitani.setText(self.pocitani.text()[:-1])
                    self.vysledek_bar.setText("Math Error.")
                    return
                if str(errorMes) == "Syntax Error":
                    self.pocitani.setText(self.pocitani.text()[:-1])
                    self.vysledek_bar.setText("Syntax Error")
                    return
                if str(errorMes) == "Invalid Character":
                    self.pocitani.setText(self.pocitani.text()[:-1])
                    self.vysledek_bar.setText("Invalid Character")
                    return
                if str(errorMes) == "Max limit exceeded":
                    self.pocitani.setText(self.pocitani.text()[:-1])
                    self.vysledek_bar.setText("Max limit exceeded")
                    return

            vysledek = str(vysledek)
            self.pocitani.setText(self.pocitani.text()[:-1])
            self.vysledek_bar.setText(vysledek)
            self.vysledek_flag = 1
        # Pokud je zmáčknuto P, kalkulačka zkontroluje, zda je číslo prvočíslo, v případě vstupu, který
        # není celočíselná hodnota, vypíše chybu.
        if pressed == "P":
            prime_flag = 1
            vysledek = self.pocitani.text()
            vysledek = vysledek[:-1]
            digit_check = vysledek
            digit_check = digit_check.isdigit()
            if digit_check == True:
                vysledek = int(vysledek)
                vysledek = m_lib.prime_check(vysledek)
                if vysledek == 1:
                    self.pocitani.setText("")
                    self.vysledek_bar.setText("is Prime.")
                else:
                    self.pocitani.setText("")
                    self.vysledek_bar.setText("is NOT Prime.")
            else:
                self.pocitani.setText("")
                self.vysledek_bar.setText("Not a natural number.")
        if self.pocitani.text() == "5318008":
            self.vysledek_bar.setText("Haha. Nice.")

    def openHelp(self):
        QDesktopServices.openUrl(QUrl("manual.txt"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Kalcoolacka = QtWidgets.QMainWindow()
    ui = Ui_Kalcoolacka()
    ui.setupUi(Kalcoolacka)
    Kalcoolacka.show()
    sys.exit(app.exec_())
