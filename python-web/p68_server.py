#!/usr/bin/env python
# coding=utf-8
#sochet的服务器端
import threading
import socket
import time
def tcplink(sock, addr):
    print('from %s:%s'%addr)
    sock.send(b'hello')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('hello, %s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('close %s'%addr)
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)#5是等待连接的最大数
print('waiting for connecting')
while True:
    sock, addr = s.accept()
    t = threading.Thread(target = tcplink, args = (sock, addr))
    t.start()

