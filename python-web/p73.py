#!/usr/bin/env python
# coding=utf-8
#async/await python3.5版本后的 it can achive 并发IO操作 在单线程中
import asyncio
async def hei():
    print('hello,world!')
    r = await asyncio.sleep(1)
    print('hei')

loop = asyncio.get_event_loop()
loop.run_until_complete(hei())
loop.close()
