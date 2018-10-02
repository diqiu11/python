#!/usr/bin/env python
# coding=utf-8

import os
R = os.path.split('/opt/repo/python-web/test.txt')
print(R)
P = os.path.splitext('/opt/repo/python-web/test.txt')
print(P)
print([x for x in os.listdir('.') if os.path.isdir(x)])


print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])
