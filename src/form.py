# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created: Wed Apr 23 16:06:33 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(403, 240)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("微软雅黑"))
        font.setPointSize(18)
        Form.setFont(font)
        self.xie = QtGui.QTextEdit(Form)
        self.xie.setGeometry(QtCore.QRect(10, 40, 111, 41))
        self.xie.setObjectName(_fromUtf8("xie"))
        self.du = QtGui.QTextEdit(Form)
        self.du.setGeometry(QtCore.QRect(150, 40, 111, 41))
        self.du.setObjectName(_fromUtf8("du"))
        self.ooxx = QtGui.QTextEdit(Form)
        self.ooxx.setGeometry(QtCore.QRect(10, 110, 251, 71))
        self.ooxx.setObjectName(_fromUtf8("ooxx"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(290, 80, 91, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "写作oo读作xx", None))
        self.pushButton.setText(_translate("Form", "开始", None))

