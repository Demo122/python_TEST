#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/8 15:42
"""
#center通过在两边添加填充字符（默认空格）让字符串居中
str1 = "The Middle by Jimmy Eat World".center(39)
print('_'+str1+'_')  #_     The Middle by Jimmy Eat World     _

#find在字符串中查找子串，如果找到就返回子串的第一个字符的索引，否则返回-1
str2 = "With a moo-oom here,and a moo-oom there ".find('moo')
print(str2) # 7
#还可以指定搜索的起点和终点
subject = '$$$ Get rich now!!! $$$'
print(subject.find('$$$')) # 0
print(subject.find('$$$',1)) # 指定了起点  # 20
print(subject.find('$$$',0,16)) #同时指定了起点和终点 # 0
# 注意，起点和终点（第二个参数和第三个参数）指定的搜索范围包含起点，但不包含终点

#join是一个非常重要的字符串方法，作用与split相反，用于合并序列的元素
seq = [1,2,3,4,5]
sep = '+'
# 所合并的序列元素必须是字符串
# sep.join(seq) #TypeError: sequence item 0: expected str instance, int found
ss = ['1','2','3','4','5'] #字符串列表
print(sep.join(ss)) # 1+2+3+4+5
dirs = '','usr','bin','env'
str3 = '/'.join(dirs)
print(str3)  # /usr/bin/env

#lower返回字符串的小写版本
str4 = "ABCDEFG"
print(str4.lower())  #abcdefg
#title将字符串转换为词首大写，即所有单词的首字母大写
str5 = "a boy can do everything for girl"
print(str5.title())  # A Boy Can Do Everything For Girl

#replace将指定的子串都替换为另一个字符串，并返回替换后的结果
str6 = "this is a test".replace("is","eez")
print(str6)  # theez eez a test

#split作用与join相反，用于将字符串拆分为序列
str7 = "/usr/bin/env".split('/')
print(str7) # ['', 'usr', 'bin', 'env']
#如果没有指定分隔符，将默认在单个或者多个连续的空白符处进行拆分
print("if you want to be a rich-man".split()) #['if', 'you', 'want', 'to', 'be', 'a', 'rich-man']

#strip将字符串开头和末尾的空白（但不包括中间的空白）删除，并返回删除后的结果
str8 = "    internal whitespace is kept      ".strip()
print(str8) # internal whitespace is kept
#还可以在参数中指定要删除哪些字符
str9 = "*！**！！***SPM * FOR * EVERYONE！！！********".strip('*！')
print(str9)  # SPM * FOR * EVERYONE

#translate只能进行单字符替换，具体使用参考python基础教程第三版page52