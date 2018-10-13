#!/usr/bin/env python
# coding=utf-8
#wsgi的模拟
from wsgiref.simple_server import make_server
import application
httpd = make_server('', 8888, application)
print('HTTP starting')
httpd.serve_forever()
