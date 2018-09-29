#!/usr/bin/env python
# coding=utf-8
#多重继承and定制类

class Student(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return 'student is %s' % self.name
    __repr__=__str__
class homework(object):
    def __init__(self,score):
        self.__score = score
    def set_atrr(self,score):
        self.__score = score
    def get_atrr(self):
        return  self.__score

class teacher(Student,homework):
    s1 = Student('diqiu11')
    print(s1)
    s2 = homework()
    s2.set_atrr(60)
    s2.get_atrr()

teacher()



