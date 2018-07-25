#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/7/25 14:14
"""


def lines(file):
    for line in file: yield line
    yield '\n'


def Blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []
