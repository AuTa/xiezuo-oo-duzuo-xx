# -*- coding: UTF-8 -*-
from pypinyin import pinyin
import pypinyin

def xiezuo(hans):
    oo_list = list(hans)
    return oo_list

def duzuo(hans):
    xx_list = pinyin(hans, heteronym=True)
    return xx_list

def result():
    oo_list = xiezuo(xiezuo_hans)
    xx_list = duzuo(duzuo_hans)
    ooxx = [0] * len(oo_list)
    str_ooxx = ''
    for i in range(0, len(oo_list)):
        ooxx[i] = ''.join(oo_list[i]) + '(' + ''.join(xx_list[i][0]) + ')'
        str_ooxx =  str_ooxx + ''.join(ooxx[i])
    print(str_ooxx)


xiezuo_hans = input('Enter oo:')
duzuo_hans = input('Enter xx:')
print(duzuo(duzuo_hans))
result()
# print(pinyin(u'中心'))