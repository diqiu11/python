#!/usr/bin/env python
# coding=utf-8
#base64
import base64
by = base64.b64decode('abcd')
by1 = base64.b64encode(b'binary\x00string')
by2 = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print(by)
print(by1)
print(by2)

def safe_base64_decode(s):
    u = len(s)%4
    while(u):
        s = s+b'='
        u-=1
    return base64.b64decode(s)

assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
