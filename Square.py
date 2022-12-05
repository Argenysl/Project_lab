# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Square.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(368, 434)
        MainWindow.setMinimumSize(QtCore.QSize(368, 434))
        MainWindow.setMaximumSize(QtCore.QSize(368, 434))
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.689, y1:0.233, x2:0.578, y2:0.136273, stop:0.0945274 rgba(83, 79, 20, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Square_Shape = QtWidgets.QPushButton(self.centralwidget)
        self.Square_Shape.setGeometry(QtCore.QRect(80, 90, 201, 171))
        self.Square_Shape.setStyleSheet("\n"
"background-color: rgb(174, 149, 255);\n"
"                              border : 2px solid black\n"
"")
        self.Square_Shape.setText("")
        self.Square_Shape.setObjectName("Square_Shape")
        self.Square_Side = QtWidgets.QLineEdit(self.centralwidget)
        self.Square_Side.setGeometry(QtCore.QRect(300, 160, 21, 22))
        self.Square_Side.setObjectName("Square_Side")
        self.Square_Label = QtWidgets.QLabel(self.centralwidget)
        self.Square_Label.setGeometry(QtCore.QRect(90, 310, 261, 41))
        self.Square_Label.setStyleSheet("font: 15pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.Square_Label.setObjectName("Square_Label")
        self.Square_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Square_Submit.setGeometry(QtCore.QRect(210, 360, 141, 51))
        self.Square_Submit.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"border-radius : 15; \n"
"background-color: rgb(255, 233, 188);\n"
"                              border : 2px solid black\n"
"")
        self.Square_Submit.setObjectName("Square_Submit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Square_Label.setText(_translate("MainWindow", "Enter  side of square"))
        self.Square_Submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())