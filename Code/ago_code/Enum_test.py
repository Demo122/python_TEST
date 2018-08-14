#！/usr/bin/env python
# _*_ coding:utf-8 _*_
from enum import Enum,unique
#@unique
# class Gender(Enum):
#     Male = 0
#     Female = 1
Gender = Enum('Gender', ('Male', 'Female'))

class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender



#测试
bart = Student('Bart',Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过！')
else:
    print('测试失败！')
print(111111111111111)
print(bart.gender)
