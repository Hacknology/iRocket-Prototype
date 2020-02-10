# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iRocket.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import time,os,livegraph
from random import randrange

class Ui_Form(object):
    def opengraph(self):
        livegraph.run()



    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(665, 608)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(420, 50, 68, 19))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(420, 70, 111, 19))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(420, 90, 68, 19))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(420, 110, 111, 19))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 50, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 520, 591, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(500, 50, 68, 19))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(520, 70, 68, 19))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(490, 90, 68, 19))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(530, 110, 68, 19))
        self.label_8.setObjectName("label_8")
        
        self.pushButton.clicked.connect(self.opengraph)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Height:"))
        self.label_2.setText(_translate("Form", "Acceleration:"))
        self.label_3.setText(_translate("Form", "Velocity:"))
        self.label_4.setText(_translate("Form", "Temperature:"))
        self.pushButton.setText(_translate("Form", "LiveGraph"))
        self.pushButton_2.setText(_translate("Form", "GPS"))
        #timer = QtCore.QTimer()
        #timer.timeout.connect(self.update_label)
        #timer.start(300)
        #self.label_5.setText(_translate("Form", str(randrange(20))))
        #self.label_6.setText(_translate("Form", str(randrange(20))))
        #self.label_7.setText(_translate("Form", str(randrange(20))))
        #self.label_8.setText(_translate("Form", str(randrange(20))))
	


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    #Yüzün anımsatır günlerimizi Tanrı Dağları'nda
    #Ne cihanda var bu kusursuzluk
    #Ne de gökten indiği sanılan kitaplarda!
    def updateme():

        ui.label_5.setText(str(randrange(20)))
        ui.label_6.setText(str(randrange(20)))
        ui.label_7.setText(str(randrange(20)))
        ui.label_8.setText(str(randrange(20)))
    timer = QtCore.QTimer()
    timer.timeout.connect(updateme)
    timer.start(3000)  
    sys.exit(app.exec_())
