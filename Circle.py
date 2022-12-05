# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Circle.ui'
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
        MainWindow.setStyleSheet("QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.689, y1:0.233, x2:0.578, y2:0.136273, stop:0.0945274 rgba(83, 79, 20, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Circle_Shape = QtWidgets.QPushButton(self.centralwidget)
        self.Circle_Shape.setGeometry(QtCore.QRect(90, 80, 201, 211))
        self.Circle_Shape.setStyleSheet("border-radius : 100; \n"
"background-color: rgb(0, 255, 72);\n"
"                              border : 2px solid black")
        self.Circle_Shape.setInputMethodHints(QtCore.Qt.ImhNone)
        self.Circle_Shape.setText("")
        self.Circle_Shape.setObjectName("Circle_Shape")
        self.Circle_Radius = QtWidgets.QLineEdit(self.centralwidget)
        self.Circle_Radius.setGeometry(QtCore.QRect(230, 170, 31, 22))
        self.Circle_Radius.setObjectName("Circle_Radius")
        self.Circle_Label = QtWidgets.QLabel(self.centralwidget)
        self.Circle_Label.setGeometry(QtCore.QRect(160, 290, 281, 41))
        self.Circle_Label.setStyleSheet("font: 15pt \"Comic Sans MS\";\n"
"color: rgb(255, 255, 255);")
        self.Circle_Label.setObjectName("Circle_Label")
        self.Circle_Submit = QtWidgets.QPushButton(self.centralwidget)
        self.Circle_Submit.setGeometry(QtCore.QRect(210, 370, 141, 51))
        self.Circle_Submit.setStyleSheet("font: 10pt \"Comic Sans MS\";\n"
"border-radius : 15; \n"
"background-color: rgb(255, 233, 188);\n"
"                              border : 2px solid black\n"
"")
        self.Circle_Submit.setObjectName("Circle_Submit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Circle_Label.setText(_translate("MainWindow", "Enter radius"))
        self.Circle_Submit.setText(_translate("MainWindow", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
