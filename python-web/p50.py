#!/usr/bin/env python
# coding=utf-8
#正则
import re
test = '010-123456'

if re.match(r'^\d{3}\-\d{3,8}$',test):
    print('True')
else:
    print('False')

S = re.split(r'[\s\,\;]','a,b  c;d')
print(S)

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
m.group()
print(m.group(0))
print(m.group(1))
