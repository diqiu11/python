#!/usr/bin/env python
# coding=utf-8
#urllib get

from urllib import request
from urllib.request import urlopen
with request.urlopen('http://www.lindiqiu.top') as page:
    data = page.read()
    print('status:', page.status, page.reason)
    for k,v in page.getheaders():
        print('%s %s'%(k,v))
    print('Data:', data.decode('utf-8'))

