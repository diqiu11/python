#!/usr/bin/env python
# coding=utf-8
from functools import reduce
L = ['adam', 'LISA', 'barT']
def normalize(L):
    for s in L:
        s.lower()
        

L1 = list(map(normalize, L))
print(L1)


L2 = [3,5,7,9]
def prod(x,y):
    return x*y
print(reduce(prod, L2))

s = '123.456'
def str2float(x,y):
    return 
def string2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digit[s]
R = reduce(str2float, map(string2num,s))
print(R)



