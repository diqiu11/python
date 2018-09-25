#!/usr/bin/env python
# coding=utf-8
#将迭代对象变成迭代器
#迭代器是惰性的
from collections import Iterator
isinstance(iter([]),Iterator)
