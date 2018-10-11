#!/usr/bin/env python
# coding=utf-8
#网络编程socket

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connet(('www.lindiqiu.top', 80))
