#!/usr/bin/env python
# coding=utf-8
#IO
from io import StringIO,BytesIO
f = StringIO()
f.write('hei\n')
print(f.getvalue())
s = f.readline()
if s=='':
    pass
print(s.strip())
b = BytesIO()
b.write('嘿'.encode('utf-8'))
print(b.getvalue())

