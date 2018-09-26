#!/usr/bin/env python
# coding=utf-8
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(L):
    return L[0]
R = sorted(L,key=by_name)
print(R)

def by_score(L):
    return L[1]
R1 = sorted(L,key=by_score,reverse=True)
print(R1)
