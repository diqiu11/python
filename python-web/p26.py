#!/usr/bin/env python
# coding=utf-8
#使用__slots__限制

class father(object):
    __slots__ = ('momney','house')

class son(father):
    __slots__ = ('car')

s1 = father()
s1.momney = 99
print(s1.momney)
s1 = son()
s1.car = 'ben'   #父类可以定义子类中的__slots__
print(s1.car)

