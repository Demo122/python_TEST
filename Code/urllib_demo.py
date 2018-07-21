#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/18 17:58
"""
import re
from urllib.request import urlopen,urlretrieve


webpage = urlopen('http://www.python.org')
text = webpage.read()
m=re.search(b'<a href="([^"]+)".*?>about</a>',text,re.IGNORECASE)
print(m.group(0))
print(m.group(1))


#如果要让urllib替你下载文件并将其副本存储再一个本地文件中，可使用函数urlretrieve，这个函数返回一个格式为（filename，headers)的元祖
#其中filename是本地文件名，headers包含一些有关远程文件的信息，要给下载的副本指定文件名，可通过第二个参数来提供
urlretrieve('http://www.python.org','E:\python_code\python_TEST\Code\python_webpage.html')