#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/7 15:45
"""
#从类似于http://www.something.com的URL中提取域名

'''
url = input('Please enter the URL: ')
domain = url[11:-4]
print("Domain name: "+domain)
'''

#在位于屏幕中央且宽带合适的方框内打印一个句子

sentence = input("Sentence: ")

screen_width = 80
text_width = len(sentence)
box_width = text_width+6
left_margin = (screen_width-box_width)//2

print()
print(' '*left_margin + '+' + '-'*(box_width-2) + '+')
print(' '*left_margin + '|' + ' '*(box_width-2) + '|')
print(' '*left_margin + '|' + ' '*2 + sentence +' '*2 + '|')
print(' '*left_margin + '|' + ' '*(box_width-2) + '|')
print(' '*left_margin + '+' + '-'*(box_width-2) + '+')
print()