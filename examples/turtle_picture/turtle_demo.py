#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/1 18:04
"""

import turtle

def draw_triangle(length=50,num=5,degree=120):   #length每个小三角新的边长 ，num 层数0
    n=num
    turtle.setup(width=800, height=800, startx=None, starty=None)
    turtle.goto(-(length*num/2), 0)  #设置画笔起点坐标，使图像位于正中
    turtle.forward(length * num)  # 先画底边
    for i in range(num):
        turtle.left(degree)  # 左转120
        for j in range(2*n-1):
            turtle.forward(length)
            turtle.left(degree)
            degree= -degree
        n-=1
        turtle.right(degree)
        degree = -degree
        turtle.forward(length * n)  #
    turtle.right(degree)
    turtle.forward(length * num)

if __name__=="__main__":

    draw_triangle()


    turtle.done()
