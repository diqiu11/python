#!/usr/bin/env python
# coding=utf-8
#回数
def is_palindrom(n):
    if n<10:
        return n
    elif n<100 and n>10:
        while n%10 == int(n/10):
            return n
    elif n>100 and n<1000:
        while n%100 == int(n/100):
            return n
    else:
        print('error')
R = list(filter(is_palindrom,range(200)))
print(R)
