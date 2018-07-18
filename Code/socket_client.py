#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/17 16:40
"""
import socket

s = socket.socket()
#host = socket.gethostname()
port = 9999
s.connect(('74.120.172.167', port))
print(s.recv(1024).decode('utf-8'))
message=input("what message you want send to server? :")
s.send(message.encode('utf-8'))
print(s.recv(1024).decode('utf-8'))
