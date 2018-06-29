#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/6/29 23:33
"""


def triangle(num=10):
    L, counter = [1], 0
    while counter < num:
        yield L
        L = [(L + [0])[i] + ([0] + L)[i] for i in range(len(L) + 1)]
        counter += 1


if __name__ == "__main__":
    for n in triangle():
        print(n)
