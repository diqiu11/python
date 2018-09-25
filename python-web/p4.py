#!/usr/bin/env python
# coding=utf-8
import math
def my_abs(x):
   # if not isinstance(x,(int, float)):
       # raise TypeError('bad opeeand type')
    if x >= 0:
        return x
    else:
        return -x

def move(x,y,step,angle=0):
    nx = x+step*math.cos(angle)
    ny = y-step*math.sin(angle)
    return nx,ny

r = move(100,100,60,math.pi/6)
print(r)#返回的是一个tuple

def quadratic(a,b,c):
    s = b*b-4*a*c
    if s>=0:
        x1 = (-b+s)/2*a
        x2 = (-b-s)/2*a
        print(x1,x2)
    if s<0:
        print('无解')


quadratic(1,6,4)
