#!/usr/bin/env python
# coding=utf-8
#数据封装
class Student(object):
    def __init__(self,num):
        self.num = num
        
    def getname(self):
        for i in range(3):
            if i==self.num:
                n = i

            else:
                continue
            
        L = ['a','b','c']
        print('In %d department,names %s' %(n,L[n]))
    
a = Student(0)
a.num
a.getname()
