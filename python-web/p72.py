#!/usr/bin/env python
# coding=utf-8
#asyncio 封装进异步I/O
import threading
import asyncio
@asyncio.coroutine
def event():
    print('hello (%s)'%threading.currentThread())
    yield from asyncio.sleep(1)
    print('again (%s)'%threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [event(),event()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
