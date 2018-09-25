#!/usr/bin/env python
# coding=utf-8
def Iterable(void):
    for i,value in enumerate(['a','b','c']):
        print(i,value)


def findMinAndMax(L):
    max=0
    min=10
    for i in L:
        if i>=max:
            max = i
        if i<min:
            min = i
    print(max,min)

findMinAndMax([(1),(2),(3)])
