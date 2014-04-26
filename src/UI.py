# -*- coding: UTF-8 -*-
import unittest.result
from PyQt4 import QtCore, QtGui
from xiezuo_oo_duzuo_xx import *
import src.xiezuo_oo_duzuo_xx


class UI_Form(QtGui.QWidget):
    def __init__(self,parent = None):
        QtGui.QWidget.__init__(self,parent)

        self.font = QtGui.QFont()
        self.font.setFamily(u"Microsoft JhengHei")
        self.font.setPointSize(16)
        self.setFont(self.font)

        self.setWindowTitle(u'写作oo读作xx')
        self.setFixedSize(600, 240)
        self.setStyleSheet('background-color:#333333;color: #ffffff;')

        self.l_xiezuo = QtGui.QLabel(self)
        self.l_xiezuo.setText(u'写作')

        self.l_duzuo = QtGui.QLabel(self)
        self.l_duzuo.setText(u'读作')

        self.le_xiezuo = QtGui.QLineEdit(self)
        self.le_xiezuo.setPlaceholderText(u'xx')
        self.le_xiezuo.setStyleSheet("border-style:flat;background-color:transparent;font: 16pt 'Microsoft JhengHei';color: #78B5DB")

        self.le_duzuo = QtGui.QLineEdit(self)
        self.le_duzuo.setPlaceholderText(u'oo')
        self.le_duzuo.setStyleSheet("border-style:flat;background-color:transparent;font: 16pt 'Microsoft JhengHei';color: #78B5DB")

        self.le_ooxx = QtGui.QLineEdit(self)
        self.le_ooxx.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.le_ooxx.setFocusPolicy(QtCore.Qt.NoFocus)
        self.le_ooxx.setStyleSheet("border-style:flat;background-color:transparent;font: 10pt 'Microsoft JhengHei';color: #78B5DB")

        clipboard = QtGui.QApplication.clipboard()

        for i in range(12):
            setattr(self.__class__, 'l_ooxx_%02d' % i, staticmethod(QtGui.QLabel(self)))
            eval('self.l_ooxx_%02d' % i).setStyleSheet("border-style:flat;background-color:transparent;font: 16pt 'Microsoft JhengHei';color: #FAF5E3")

        self.pb_clean = QtGui.QPushButton(u'清除', self)
        self.pb_clean.setMinimumWidth(80)
        self.pb_clean.setStyleSheet('background-color:#666666;color:#ffffff;font: 16pt "Microsoft JhengHei";border-radius:10px;')
        self.pb_copy = QtGui.QPushButton(u'复制', self)
        self.pb_copy.setStyleSheet('background-color:#666666;color:#ffffff;font: 16pt "Microsoft JhengHei";border-radius:10px;')

        self.connect(self.le_xiezuo, QtCore.SIGNAL(u'returnPressed()'), self.le_duzuo.setFocus)
        self.le_duzuo.returnPressed.connect(lambda:result(self, self.le_xiezuo.text(), self.le_duzuo.text()))
        # self.le_duzuo.returnPressed.connect(self.pb_copy.setFocus)
        self.pb_clean.clicked.connect(self.le_xiezuo.clear)
        self.pb_clean.clicked.connect(self.le_duzuo.clear)
        self.pb_clean.clicked.connect(lambda:result(self, self.le_xiezuo.text(), self.le_duzuo.text()))
        self.pb_copy.clicked.connect(lambda:clipboard.setText(self.le_ooxx.text()))


        grid = QtGui.QGridLayout()
        grid.setContentsMargins(50, 50, 50, 50)
        grid.setSpacing(10)
        grid.setRowMinimumHeight(2, 50)


        grid.addWidget(self.l_xiezuo, 0, 0)
        grid.addWidget(self.le_xiezuo, 0, 1)

        grid.addWidget(self.l_duzuo, 1, 0)
        grid.addWidget(self.le_duzuo, 1, 1)

        grid.addWidget(self.pb_clean, 0, 2, 2, 1)
        grid.addWidget(self.pb_copy, 3, 2, 2, 1)

        self.horizontalLayout = QtGui.QHBoxLayout()
        for i in range(12):
            self.horizontalLayout.addWidget(eval('self.l_ooxx_%02d' % i))
        self.spacerItem1 = QtGui.QSpacerItem(10, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(self.spacerItem1)
        grid.addLayout(self.horizontalLayout, 3, 1)

        grid.addWidget(self.le_ooxx, 4, 1)
        # self.spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        # grid.addItem(self.spacerItem2, 4, 2)

        self.setLayout(grid)
        self.setTabOrder(self.pb_clean, self.le_duzuo)
        self.setTabOrder(self.le_duzuo, self.le_xiezuo)
        self.setTabOrder(self.le_xiezuo, self.le_duzuo)

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = UI_Form()
    widget.show()
    sys.exit(app.exec_())
