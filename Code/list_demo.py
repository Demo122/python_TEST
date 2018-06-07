#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/7 16:58
"""
#使用字符串来创建列表
print(list('hello'))  # ['h', 'e', 'l', 'l', 'o']

#使用切片赋值还可以在不替换原有元素的情况下插入新元素
numbers = [1,5]
numbers[1:1] = [2,3,4]
print(numbers)  #[1, 2, 3, 4, 5]

#append方法，将一个对象附加到列表的末尾
lst = [1,12,3]
lst.append(4)
print(lst) #[1, 12, 3, 4]

#clear方法就地清空列表的内容
lst.clear()
print(lst) #[]

#copy,常规复制只是将一个名称关联到列表，要让a,b指向不同的列表，就必须将b关联到a的副本
a=[9,8,7]
b = a.copy()  #这类似于使用a[:],list(a),它们也都是复制a
b[1]=0
print(a) #[9, 8, 7]

#count方法计算指定的元素在列表中出现了多少次
num = ['to','ce','sd','to','qw','to'].count('to')
print(num) #3
x = [[1,2],1,1,[2,1,[1,2]]]
print(x.count(1))  #2
print(x.count([1,2])) #1

#extend同时将多个值附加到列表末尾，用一个列表来扩展另一个列表
q = [1,2,3]
p = [4,5,6]
q.extend(p)
print(q) # [1, 2, 3, 4, 5, 6]

#index在列表中查找指定值第一次出现的索引
knights = ['We','are','the','knights','who','say','in']
knights.index('who') #4

#insert用于将一个对象插入列表
scores = [60,70,90,100]
scores.insert(2,80)
print(scores) #[60, 70, 80, 90, 100]

#pop从列表中删除一个元素（末尾最后一个元素），并返回这一元素
num_list = [1,2,3]
print(num_list.pop()) #3
print(num_list.pop(0)) #1

#remove用于删除第一个为指定值的元素
m = ['to','ce','sd','to','qw','to']
m.remove('to')   #修改且不返回值
print(m) #['ce', 'sd', 'to', 'qw', 'to']

#reverse按相反的顺序排列列表中的元素
db = [1,2,3,4,5,6,7,8,9]
db.reverse()
print(db) #[9, 8, 7, 6, 5, 4, 3, 2, 1]
db.reverse()
print(db) #[1, 2, 3, 4, 5, 6, 7, 8, 9]

#sort用于对列表就地排序，sort修改列表但不返回值
x1 = [4,6,2,1,7,9]
y1 = x1.copy()
y1.sort()
print(y1)

y2 = sorted(x1)
print(x1) #原列表不变
print(y1)

'''
高级排序
sort接受两个可选参数：key和reverse
  参数key：将其设置为一个用于排序的函数
  参数reverse:只需将其指定为一个真值（True或False)以是否要按相反顺序排列
  sorted同样接受参数key和reverse
'''
x3 = ['abcdefg','miaker','queen','june','February']
x3.sort(key=len)
print(x3) #['june', 'queen', 'miaker', 'abcdefg', 'February']
x3.sort(key=len,reverse=True)
print(x3) #['February', 'abcdefg', 'miaker', 'queen', 'june']