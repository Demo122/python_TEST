#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/7 23:15
"""
#设置字符串的格式
#方法一
format = "Hello,%s. %s enough for ya?"
values = ('world','Hot')
str = format % values
print(str) # Hello,world. Hot enough for ya?

#方法二
from string import Template
tmp1 = Template("Hello,$who! $what enough for ya?")
str2 = tmp1.substitute(who="Mars",what="Dusty")
print(str2) # Hello,Mars! Dusty enough for ya?

#方法三
str3 = "{}, {} and {}".format("first","second","third")
print(str3) #first, second and third

#可以这样使用索引
str4 = "{3} {0} {2} {1} {3} {0} ".format("be","not","or","to")
print(str4) # to be or not to be

from math import pi
# 关键字参数的排列顺序无关紧要
str5 = "{name} is approximately {value:.2f}.".format(value=pi,name="Π")
print(str5) # Π is approximately 3.14.

#如果变量与替换字段同名，可使用f字符串--在字符串前面加上f
from math import e
str6 = f"Euler's constant is roughly {e}"
print(str6) #Euler's constant is roughly 2.718281828459045
# 船舰最终字符串时，将把替换字段e替换为变量e的值，与下面等价
str7 = "Euler's constant is roughly {e}.".format(e=e)
print(str7) # Euler's constant is roughly 2.718281828459045.