# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'backup_gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(699, 447)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 308, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser_3.setGeometry(QtCore.QRect(80, 400, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(520, 410, 150, 22))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(20, 100, 491, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 160, 491, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser = QtWidgets.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(20, 220, 661, 171))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 201, 41))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(160, 40, 308, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(550, 50, 111, 111))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 70, 308, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 410, 91, 21))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 308, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "需要备份的位置"))
        self.label_4.setText(_translate("Dialog", "@author: Gao-zl"))
        self.label_6.setText(_translate("Dialog", "照片备份"))
        self.label_7.setText(_translate("Dialog", "按照月份分类，建议先执行照片重命名"))
        self.pushButton.setText(_translate("Dialog", "Start"))
        self.label.setText(_translate("Dialog", "原始的照片地址"))
        self.label_5.setText(_translate("Dialog", "程序耗时"))
        self.label_3.setText(_translate("Dialog", "项目运行输出"))