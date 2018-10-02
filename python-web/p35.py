#!/usr/bin/env python
# coding=utf-8
#I/O
with open('/opt/repo/python-web/test.txt','r') as f:
    print(f.read())
    
    for line in f.readlines():
        print(list.strip())
