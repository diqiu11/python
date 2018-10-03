#!/usr/bin/env python
# coding=utf-8
import os
print('Process (%s) start..'%os.getpid())

pid = os.fork()
if pid == 0:
    print('child process (%s),parent process (%s)'%(os.getpid(),os.getppid))
else:
    print('(%s) make a child process (%s)'%(os.getpid,pid))
