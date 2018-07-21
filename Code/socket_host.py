#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/17 16:36
"""

# import socket,threading
#
# def do_send_recv(c,addr):
#     print("connection from %s: %s",addr)
#     c.send("欢迎连接第一个服务器".encode('utf-8'))
#     data=c.recv(1024)
#     c.send(("Hello, %s!"%data.decode('utf-8')).encode('utf-8'))
#
# s = socket.socket()
# #host = socket.gethostname()
# port = 9999
# s.bind(('74.120.172.167', port))
#
# s.listen(5)
#
# while True:
#     c, addr = s.accept()
#     t=threading.Thread(target=do_send_recv,args=(c,addr))
#     t.start()

from socketserver import TCPServer,StreamRequestHandler

class Handler(StreamRequestHandler):
    def handle(self):
        addr=self.request.getpeername()
        print("Got connection from",addr)
        self.wfile.write(b'Thank you for connecting')

server = TCPServer(('DESKTOP-FRIPQFS',9999),Handler)
server.serve_forever()