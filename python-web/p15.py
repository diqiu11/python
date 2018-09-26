#!/usr/bin/env python
# coding=utf-8
#筛选函数
def is_odd(n):
    return n%2 == 0
R = list(filter(is_odd,[n for n in range(100)]))
print(R)
