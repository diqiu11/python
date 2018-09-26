#!/usr/bin/env python
# coding=utf-8
# 错误的
a = int(9.9)
print(a)

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(n):
    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    for name_list in L:
        for (name, num) in name_list:
            n = name.lower
            return n
S = sorted(L,key=by_name)
print(S)

