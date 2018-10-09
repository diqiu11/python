#!/usr/bin/env python
# coding=utf-8
#itertools   返回的值是一个iterator 需要使用for迭代才能算出
import itertools

def iter_1():
    natual = itertools.count(1)#count
    for n in natual:
        print(n)
def iter_2():
    cs = itertools.cycle('123')#cycle
    for n in cs:
        print(n)
def iter_3():
    ns = itertools.repeat('A',2)#repeat  for会造成无限的循环
    for n in ns:
        print(n)
def iter_stop():
    natual = itertools.count(1)
    ns = itertools.takewhile(lambda n:n<3, natual)#takewhile 利用匿名函数来控制迭代的停止
    print(list(ns))
def iter_chain():
    chain = itertools.chain('abc', 'def')
    for n in chain:
        print(n)
def iter_groupby():
    groupby = itertools.groupby('AaaBbb', lambda x:x.upper())
    for key, group in groupby:
        print(key, tuple(group))

#f1 = iter_1()
f = iter_stop()
#assert iter_chain()
assert iter_groupby()
