#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/6/29 21:40
"""

import random
def conflict(state, nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0, nextY - i): #若下一个皇后和前面的皇后列相同或者在一条对角线上，则冲突
            return True
    return False


def queen(num=8, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            if len(state) == num - 1: #若是最后一个皇后，则返回该位置
                yield (pos,)
            else: #若是最后一个皇后，则返回该位置
                for result in queen(num, state + (pos,)):  #生成器迭代返回一个元祖
                    yield (pos,) + result

def prettyprint(solution):
    def line(pos,length=len(solution)):
        return '~'*(pos)+'X'+'~'*(length-pos-1)
    for pos in solution:
        print(line(pos))

if __name__ == "__main__":
    solution=random.choice(list(queen()))
    print(solution)
    prettyprint(solution)
