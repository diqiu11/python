#!/usr/bin/env python
# coding=utf-8
def ge(max):
    n,a,b = 0,0,1
    while n<max:
        yield b
        a,b = b,a+b
        n+=1
       
    return 'done'
    
g=ge(6)
print(g)
