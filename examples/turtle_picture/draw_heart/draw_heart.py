#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/1 20:05
"""

from turtle import *
def curvemove():
    for i in range(200):
        right(1)
        forward(1)
color('red','pink')
begin_fill()
for i in range(2):
    left(140)
    forward(111.65)
    curvemove()
    left(120)
    curvemove()
    forward(111.65)
    goto(40,0)
    left(140)
end_fill()
goto(270,0)
left(160)
forward(550)

done()