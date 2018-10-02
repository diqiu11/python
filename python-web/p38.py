#!/usr/bin/env python
# coding=utf-8
import os
def seach(filename,path=os.curdir):
    for n in os.listdir(path):
        nPath = os.path.join(path,n)
        if os.path.isdir(nPath):
            seach(filename,nPath)
        elif n.find(filename) != -1:
            print('found:%s' %os.path.relpath(nPath))

seach('test')
