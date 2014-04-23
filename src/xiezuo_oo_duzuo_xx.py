# -*- coding: UTF-8 -*-
from pypinyin import pinyin
import pypinyin
from PyQt4 import QtGui, QtCore
from form import Ui_Form


class Widget(QtGui.QWidget, Ui_Form):
    """QtGui.QWidget和界面设计时选择的类型一致"""
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self) # Ui_Form.setupUi
        self.pushButton.clicked.connect(self.result)

    # @QtCore.pyqtSignature("")
    def xiezuo(self):
        hans = self.xie.toPlainText()
        oo_list = list(hans)
        return oo_list

    # @QtCore.pyqtSignature("")
    def duzuo(self):
        hans = self.du.toPlainText()
        xx_list = pinyin(hans, heteronym=True)
        return xx_list

    # @QtCore.pyqtSignature("")
    def result(self):
        oo_list = self.xiezuo()
        xx_list = self.duzuo()
        ooxx = [0] * len(oo_list)
        str_ooxx = ''
        for i in range(0, len(oo_list)):
            ooxx[i] = ''.join(oo_list[i]) + '(' + ''.join(xx_list[i][0]) + ')'
            str_ooxx =  str_ooxx + ''.join(ooxx[i])
        print(str_ooxx)
        self.ooxx.setText(str_ooxx)

    #
    # xiezuo_hans = input('Enter oo:')
    # duzuo_hans = input('Enter xx:')
    # print(duzuo(duzuo_hans))
    # result()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec_())