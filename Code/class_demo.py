#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author:DQ
@time:2018/6/28 14:09
"""


class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print('Aaaahh')
            self.hungry = False
        else:
            print('No,thanks!')


class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)  #调用未关联的超类构造函数
        super().__init__()  # 使用函数super,在python3中使用可不提供参数
        self.sound = 'Squawk'

    def sing(self):
        print(self.sound)


if __name__ == "__main__":
    sb = SongBird()
    sb.sing()
    sb.eat()
    sb.eat()
