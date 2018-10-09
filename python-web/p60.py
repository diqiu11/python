#!/usr/bin/env python
# coding=utf-8
#@closing 

from contextlib import closing, contextmanager
from urllib.request import urlopen

@contextmanager
def closing(url):
    try:
        yield url
    finally:
        url.close()


with closing(urlopen('http://www.lindiqiu.top')) as page:
    for line in page:
        print(line)
