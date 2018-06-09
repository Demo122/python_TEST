#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/9 20:24
"""

#clear删除索引的字典项
d = {}
d['name'] = 'Gumby'
d['age'] = 42
print(d)
print(d.clear())


#copy方法返回一个新字典，这个执行的浅复制，因为值本身是原件而非副本
x = {'username':'admin','machines':['foo','bar','baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y) #{'username': 'mlh', 'machines': ['foo', 'baz']}
print(x) #{'username': 'admin', 'machines': ['foo', 'baz']}
#替换副本的值是，原件不受影响，修改副本时，原件也将发生变化，因为原件和副本指向一样

#使用模板copy中的函数deepcopy进行深拷贝可以避免这种问题
from copy import deepcopy
x1 = {'machines':['foo','bar','baz']}
y1 = x1.copy()
z1 = deepcopy(x1)
x1['machines'].pop(0) # foo
print(y1) #{'machines': ['bar', 'baz']}
print(z1) #{'username':'admin','machines':['foo','bar','baz']}

#fromkeys创建一个新字典，其中包含指定的键，每个键默认值为None
a = dict.fromkeys(['name','age','sex'])
print(a) # {'name': None, 'age': None, 'sex': None}
#也可以使用特定的值
b = dict.fromkeys(['name','age','sex'],'unknown')
print(b)

#get访问不存在的键是不引发异常，返回None,也可以指定返回值替换None
x3 = {}
print(x3.get('name')) #None
print(x3.get('name','不存在name')) #不存在name

#items返回一个包含所有字典项的列表，每个元素都为(key,value)的形式，字典项在列表中排序不确定
d = {'title':'Python Web Site','url':'http：//www.python.org','spam':0}
print(d.items()) # dict_items([('title', 'Python Web Site'), ('url', 'http：//www.python.org'), ('spam', 0)])
#返回值属于一种字典视图，可以确定其长度和进行成员资格检查
it = d.items()
print(len(it)) #3
it1 = ('spam',0) in it
print(it1) #True
#视图的一个优点是，它不是复制
d['spam'] = 1
it1 = ('spam',0) in it
print(it1) #False

#keys返回一个字典视图,其中只包含键
print(d.keys()) # dict_keys(['title', 'url', 'spam'])

#pop可用于获取与指定键相关联的值，并将该键--值从字典中删除
dd = {'x':1,'y':2,'z':3}
print(dd.pop('x')) # 1
print(dd) # {'y': 2, 'z': 3}

# popitem随机弹出字典中的一个字典项
print(dd.popitem()) #('z', 3)
print(dd) # {'y': 2}

#setdefault指定键存在是返回其值，否则返回指定的值并相应的更新字典
ddd = {}
print(ddd.setdefault('name','N/A')) # N/A
print(ddd) # {'name': 'N/A'}
#如果不指定值，默认是None
print(ddd.setdefault('age')) #None

#update
ddd.update(d)
print(ddd) # {'name': 'N/A', 'age': None, 'title': 'Python Web Site', 'url': 'http：//www.python.org', 'spam': 1}


#values返回字典的值视图，包含重复的值
d2 = {'x':0,'q':1,'e':2,'r':1}
print(d2.values()) # dict_values([0, 1, 2, 1])


