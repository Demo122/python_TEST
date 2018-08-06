#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/18 15:34
"""
import socket
s=socket.socket()
s.connect(('74.120.172.167', 1234))
print(s.recv(1024).decode('utf-8'))
for str in [b'Michael', b'Tracy', b'Sarah']:
    s.send(str)
    print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()