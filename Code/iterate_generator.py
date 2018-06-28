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


if __name__ == "__main__":
    fibs = Fibs()
    for f in fibs:
        if f > 1000:
            print(f)
            break

    # 通过对可迭代对象调用内置函数iter,可获得一个迭代器
    it = iter([1,2,3,4])
    print(next(it))
    print(next(it))

