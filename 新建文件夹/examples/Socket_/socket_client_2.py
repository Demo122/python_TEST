#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/18 15:39
"""
import socket

s=socket.socket()
s.connect(('74.120.172.167', 1234))
print(s.recv(1024).decode('utf-8')+'is client_2')
s.send(b"I'm client_2")
print(s.recv(1024).decode('utf-8'))