# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_PicPong.ui'
#
# Created: Tue Sep  4 15:25:18 2018
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_picPong(object):
    def setupUi(self, picPong):
        picPong.setObjectName("picPong")
        picPong.resize(592, 360)
        self.widgetSide = QtWidgets.QWidget(picPong)
        self.widgetSide.setGeometry(QtCore.QRect(0, 0, 61, 361))
        self.widgetSide.setMinimumSize(QtCore.QSize(40, 361))
        self.widgetSide.setMaximumSize(QtCore.QSize(71, 2000))
        self.widgetSide.setObjectName("widgetSide")
        self.pushButtonCut = QtWidgets.QPushButton(self.widgetSide)
        self.pushButtonCut.setGeometry(QtCore.QRect(5, 10, 50, 50))
        self.pushButtonCut.setObjectName("pushButtonCut")
        self.pushButtonView = QtWidgets.QPushButton(self.widgetSide)
        self.pushButtonView.setGeometry(QtCore.QRect(5, 74, 50, 50))
        self.pushButtonView.setObjectName("pushButtonView")
        self.pushButtonSet = QtWidgets.QPushButton(self.widgetSide)
        self.pushButtonSet.setGeometry(QtCore.QRect(5, 140, 50, 50))
        self.pushButtonSet.setObjectName("pushButtonSet")
        self.pushButtonConfig = QtWidgets.QPushButton(self.widgetSide)
        self.pushButtonConfig.setGeometry(QtCore.QRect(5, 300, 50, 50))
        self.pushButtonConfig.setObjectName("pushButtonConfig")
        self.widgetView = QtWidgets.QWidget(picPong)
        self.widgetView.setGeometry(QtCore.QRect(62, -1, 531, 361))
        self.widgetView.setMinimumSize(QtCore.QSize(491, 361))
        self.widgetView.setMaximumSize(QtCore.QSize(2000, 2000))
        self.widgetView.setObjectName("widgetView")
        self.pushButtonUpload = QtWidgets.QPushButton(self.widgetView)
        self.pushButtonUpload.setGeometry(QtCore.QRect(30, 10, 471, 311))
        self.pushButtonUpload.setObjectName("pushButtonUpload")
        self.lineEdit = QtWidgets.QLineEdit(self.widgetView)
        self.lineEdit.setGeometry(QtCore.QRect(0, 325, 521, 31))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(picPong)
        QtCore.QMetaObject.connectSlotsByName(picPong)

    def retranslateUi(self, picPong):
        _translate = QtCore.QCoreApplication.translate
        picPong.setWindowTitle(_translate("picPong", "Form"))
        self.pushButtonCut.setText(_translate("picPong", "1"))
        self.pushButtonView.setText(_translate("picPong", "2"))
        self.pushButtonSet.setText(_translate("picPong", "3"))
        self.pushButtonConfig.setText(_translate("picPong", "c"))
        self.pushButtonUpload.setText(_translate("picPong", "Upload"))

