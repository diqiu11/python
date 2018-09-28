#!/usr/bin/env python
# coding=utf-8
#继承多态

class father(object):
    def momney(self):#第一个方法必须有self，像__init__
        print('1000$')

class son1(father):
    pass
class son2(father):
    pass

S = son1()
S.momney()
