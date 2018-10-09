#!/usr/bin/env python
# coding=utf-8
#contextlib
from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print('%s'%self.name)
@contextmanager#decorate 装饰器
def create_query(name):
    print('开始')
    q = Query(name)
    yield q#分界
    print('结束')



with create_query('diqiu11') as q:#with先执行yield前面的代码，然后在执行yield后面的
    q.query()
