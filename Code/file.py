#!/usr/bin/env python
# _*_ coding:utf-8 _*

# f=open("F:\python-code\\file_test\\纸短情长.txt",'r')
# print(f.read())
# f.close()

# try:
#     f=open("F:\python-code\\file_test\\纸短情长.txt",'r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

#python 引入with 语句来自动帮我们调用close()方法
# with open("F:\python-code\\file_test\\纸短情长.txt",'r') as f:
#     print(f.read())


# with open("F:\python-code\\file_test\\纸短情长.txt",'a') as f2:
#     f2.write("\n我爱你")
#
# # 如果要配置文件，用readlines()最方便
# f=open('F:\python-code\\file_test\\纸短情长.txt','r')
# for line in f.readlines():
#     print(line.strip()) #把末尾的‘\n’去掉
# f.close()

# with open("F:\python-code\\file_test\\test.jpg",'rb') as f1:
#     print(f1.read())


#  StringIO 和 BytesIO 是再内存中操作 str 和 bytes 的方法，使得和读写文件具有一致的接口

from io import StringIO
f = StringIO()
print(f.write('hello!')) #6
print(f.write(' '))      #1
print(f.write('world!')) #6
print(f.getvalue())  #getvalue用于获得写入后的str



from io import StringIO
f=StringIO('Hello!\nHi!\nI love you!')
while True:
    s=f.readline()
    if s=='':
        break
    print(s.strip())

#如果操作二进制数据，就需要使用BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())