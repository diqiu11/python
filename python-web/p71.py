#!/usr/bin/env python
# coding=utf-8
#协程解决死锁问题

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return 
        print('consumer, %s'%n)
        r = '200 OK'
def produce(c):
    c.send(None)
    n = 0
    while n<3:
        n+=1
        print('procing %s' %n)
        r = c.send(n)
        print('consumer return: %s'%r)
    c.close()

c = consumer()
produce(c)
