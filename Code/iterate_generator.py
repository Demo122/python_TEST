#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/6/28 17:43
"""


# 实现了方法__iter__的对象是可迭代的，而实现了方法__next__的对象是迭代器

class Fibs:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a

    def __iter__(self):
        return self


class TestIterator:
    value = 0

    def __next__(self):
        self.value += 1
        if self.value > 10: raise StopIteration
        return self.value

    def __iter__(self):
        return self


# 生成器
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element


# 改进
def flatten2(nested2):
    try:
        for sublist in nested2:
            for element in flatten2(sublist):
                yield element
    except TypeError:
        yield nested2


# 再次改进
def flatten3(nested3):
    try:
        # 不迭代类似于字符串的对象
        try:
            nested3 + ''
        except TypeError:
            pass
        else:
            raise TypeError
        for sublist in nested3:
            for element in flatten3(sublist):
                yield element
    except TypeError:
        yield nested3


if __name__ == "__main__":
    # fibs = Fibs()
    # for f in fibs:
    #     if f > 1000:
    #         print(f)
    #         break

    # 通过对可迭代对象调用内置函数iter,可获得一个迭代器
    # it = iter([1, 2, 3, 4])
    # print(next(it))
    # print(next(it))
    # 从迭代器创建序列
    # it = list(TestIterator())
    # print(it)

    # 迭代生成器
    # nested = [[1, 2, 3], [4, 5], [6]]
    # for num in flatten(nested):
    #     print(num)
    nested2 = [9, [8, 7, 6], [5, 4], 3, 2, 1, 0]
    print(list(flatten2(nested2)))

    nested3 = [[['mike'], 'jone'], 'june']
    print(list(flatten3(nested3)))

    # 简单生成器
    # g = ((i + 2) ** 2 for i in range(2, 27))
    # print(next(g))
    # a = sum(i ** 2 for i in range(10))
    # print(a)
