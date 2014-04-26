# -*- coding: UTF-8 -*-
from pypinyin import pinyin
import pypinyin
from PyQt4 import QtCore, QtGui


def isset(v):
    try:
        type (eval(v))
    except:
        return 0
    else:
        return 1

def xiezuo(hans):
    print(hans)
    oo_list = list(hans)
    return oo_list

def duzuo(hans):
    xx_list = pinyin(hans, heteronym=True, style=pypinyin.NORMAL)
    return xx_list

def result(self, str_xiezuo, str_duzuo):
    oo_list = xiezuo(str_xiezuo)
    xx_list = duzuo(str_duzuo)
    ooxx = [0] * (len(oo_list) + len(xx_list))
    str_ooxx = ''
    for i in range(12):
        eval('self.l_ooxx_%02d' % i).setText('')
    if len(oo_list) == len(xx_list):
        for i in range(len(oo_list)):
            num = 2*i
            ooxx[num] = oo_list[i]
            num += 1
            ooxx[num] = '(' + ''.join(xx_list[i][0]) + ')'
    elif len(oo_list) > len(xx_list):
        for i in range(len(xx_list)):
            num = 2*i
            ooxx[num] = oo_list[i]
            num += 1
            ooxx[num] = '(' + ''.join(xx_list[i][0]) + ')'
        for i in range(len(xx_list), len(oo_list)):
            num = i + len(xx_list)
            ooxx[num] = oo_list[i]
    else:
        for i in range(len(oo_list)):
            num = 2*i
            ooxx[num] = oo_list[i]
            num += 1
            ooxx[num] = '(' + ''.join(xx_list[i][0]) + ')'
        for i in range(len(oo_list), len(xx_list)):
            num = i + len(oo_list)
            ooxx[num] = '(' + ''.join(xx_list[i][0]) + ')'
    for i in range(len(ooxx)):
        eval('self.l_ooxx_%02d' % i).setText(ooxx[i])
        str_ooxx = str_ooxx + ''.join(ooxx[i])
    # print(str_ooxx)
    self.le_ooxx.setText(str_ooxx)
