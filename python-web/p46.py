#!/usr/bin/env python
# coding=utf-8
#Lock进程包含了线程，当两者调用同一个变量的时候有可能冲突，解决办法就是加一把锁
import time, threading
balance = 0
lock = threading.Lock() #一个线程持有一个锁，不会造成冲突
def change_it(n):
    global balance
    balance+=n
    balance-=n

def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()
        
t1 = threading.Thread(target=run_thread,args=(5,))
t2 = threading.Thread(target=run_thread,args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)

