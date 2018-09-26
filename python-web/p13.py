#!/usr/bin/env python
# coding=utf-8
#map/reduce
from functools import reduce
def f(x):
    return x*x
r = map(f,[1,2,3,4])
print(list(r))
print(list(map(str,[1,2,3])))


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def char2num(s):
    return DIGITS[s]
def str2int(s):
    return reduce(lambda x,y:x*10+y,map(char2num, s))

print(str2int('1359'))
