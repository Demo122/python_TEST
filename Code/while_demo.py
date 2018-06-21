#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/17 16:15
"""
name = ''
while not name or name.isspace():
    name = input("please enter your name: ")
print('hello,{}!'.format(name))