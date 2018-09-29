#!/usr/bin/env python
# coding=utf-8
#__getitem__() __setitem__() __delitem__()
class fIb(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b = 1,1
            for x in range(n):
                a,b = b ,a+b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start == None:
                start = 0
            a,b = 1,1
            L=[]
            for x in range(stop):
                if x>=start:
                    L.append(a)
                a,b = b,a+b
            return L

fun = fIb()
print(fun[0,15])

