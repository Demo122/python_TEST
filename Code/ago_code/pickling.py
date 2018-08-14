#!/usr/bin/env python
# _*_ coding:utf-8 _*

#把变量从内存中变成可存储或传输的过程称之为序列化，在python中叫pickling
import pickle
d=dict(name='Bob',age=20,score=88)
d1=pickle.dumps(d)      #序列化为bytes
f=open('F:\python-code\\file_test\\pickling_test','wb')
f.write(d1)
f.close()


f1=open('F:\python-code\\file_test\\pickling_test','rb')

d2=f1.read()
print(pickle.loads(d2))  #反序列化

f1.close()


print('分割线-----------------------------------------------------------')

#使用pickle.dump()直接把对象序列化后写入一个file-like Object
f2=open('F:\python-code\\file_test\\pickle_test2','wb')
pickle.dump(d,f2)
f2.close()
#使用pickle.load()方法从一个file-like Object 中直接反序列化出对象
f3=open('F:\python-code\\file_test\\pickle_test2','rb')
d3=pickle.load(f3)
f3.close()
print(d3)


print('分割线---------用JSON序列化class对象-------')
import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

#dumps()方法不知道如何将Student实例变为一个JSOJN的{}对象，
#可选参数default是把任意一个对象变成一个可实例化为JSON的对象
# 所以我们需要为Student写一个转换函数
def student_dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score,
    }

s=Student('Bob',20,88)
#print(json.dumps(s,default=student_dict))
#可以偷懒使用每个实例都有的__dict__属性，除了定义了__slots__的class
print(json.dumps(s,default=lambda obj:obj.__dict__))

#同样的，要把json反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象
#然后传入 object_hook参数负啧把dict转换为Student实例
def dict_student(d):
    return Student(d['name'],d['age'],d['score'])
json_str='{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(json_str,object_hook=dict_student))