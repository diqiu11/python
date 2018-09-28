#!/usr/bin/env python
# coding=utf-8
#实例属性和类属性

class Student(object):
    count = 0
    def __init__(self,name):
        self.name = name
        
        Student.count+=1

bart = Student('Bart')
lisa = Student('Lisa')
print(Student.count)
