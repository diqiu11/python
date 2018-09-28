#!/usr/bin/env python
# coding=utf-8
#访问控制
class Student(object):
    def __init__(self,name,num):
        self.__name = name
        self.__num = num
    def getname(self):
        return self.__name
    def setname(self,name):
        self.name = name

a = Student('diqiu11',11)
#a.__name
print(a.getname())
print(a.__name)#限制访问
print(a.getname())
