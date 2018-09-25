#!/usr/bin/env python
# coding=utf-8
def trim(s):
    if s[0]==' ' and  s[-1]==' ':
        print(s[1:-1])
    else:
        print('error')

trim(' ABC ')
