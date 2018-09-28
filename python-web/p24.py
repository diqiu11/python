#!/usr/bin/env python
# coding=utf-8

class c(object):
    def chance(self,s):
        L = ('int','str')
        for n in L:
            if isinstance(s,n) == True:
                print('n')

class S(c):
    pass

son = S()
son.chance(1)
