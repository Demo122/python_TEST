#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/7 16:47
"""
#序列成员资格示例

#检查用户名和PIN码
database = [
    ['albert','1234'],
    ['dilbert', '4567'],
    ['smith', '7891'],
    ['jones', '123456789'],

]
username = input("User name: ")
pin = input("PIN code: ")

if [username,pin] in database:
    print("Access granted")