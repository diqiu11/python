#!/usr/bin/env python
# coding=utf-8
#启动子进程subprocess
import subprocess
print('# nslookup www.lindiqiu.top')
r = subprocess.call(['nslookup','www.lindiqiu.top'])
#print('exit code:',r)
