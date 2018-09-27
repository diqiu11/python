#!/usr/bin/env python
# coding=utf-8
#函数封装和调用，public和private的使用
__author__='diqiu11'
from functools import reduce
def _private1(n):
    return n+1
def _private2(x,y):
    return x+y
def greeting():
    print(list(map(_private1,[1,2,3])))
    print(reduce(_private2,[1,2,3,4]))    #reduce 返回的数不能用list保存，
    print(list(filter(lambda n:n%2==1,range(1,200))))

if __name__=='__main__':
    greeting()
