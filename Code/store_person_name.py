#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:danqing
@time:2018/6/21 22:39
"""
def init(data):
    data['first'] = {}
    data['middle'] = {}
    data['last'] = {}

def lookup(data,label,name):
    return data[label].get(name)

def store(data,full_name):
    names = full_name.split()
    if len(names) == 2: names.insert(1,'')
    labels = 'first','middle','last'

    for label,name in zip(labels,names):
        people = lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name] = [full_name]

def store2(data,*full_names):
    #改进后，可以接受存储多个名字
    for full_name in full_names:
        names = full_name.split()
        if len(names) == 2: names.insert(1, '')
        labels = 'first', 'middle', 'last'

        for label, name in zip(labels, names):
            people = lookup(data, label, name)
            if people:
                people.append(full_name)
            else:
                data[label][name] = [full_name]

def print_params(**params):
    #**用于收集关键字参数
    print(params)


if __name__ == '__main__':
    storage = {}
    init(storage)
    store(storage,'A B C')
    people = lookup(storage, 'middle', 'B')
    print(people)


    # name = ''
    # while not name or name.isspace():
    #     name = input('please enter you want store name: ')
    # store(storage,name)
    # people2 = lookup(storage,'middle','')
    # print(people2)
    # print(storage)

    d={}
    init(d)
    store2(d,'Luck Skywalker','Anakin Skywalker')
    people3 = lookup(d,'last','Skywalker')
    print(people3)

    #测试 ** ,收集关键字参数放在一个字典
    print_params(name='jack',age='18')
    # {'name': 'jack', 'age': '18'}



