#!/usr/bin/env python
# coding=utf-8
#函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数
#变量可以指向函数
f = abs
print(f(-11))
def add(x,y,z):
    return z(x)+z(y)
print(add(-1,-10,abs))
