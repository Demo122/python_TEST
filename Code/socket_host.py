#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/17 16:36
"""

import socket

s = socket.socket()
host = socket.gethostname()
port = 1234
s.bind((host, port))

s.listen(5)

while True:
    c, addr = s.accept()
    print('Got connection from', addr)
    msg = '欢迎访问菜鸟教程！'
    c.send(msg.encode('utf-8'))
    c.close()
