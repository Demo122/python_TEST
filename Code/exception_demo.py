#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@auther:DQ
@time:2018/6/27 15:30
"""


# try:
#     x=int(input("enter the first number:"))
#     y=int(input("enter the second number:"))
#     print(x/y)
# except ZeroDivisionError:
#     print("the second number can't be zero!")

class MuffledCalculator:
    muffled = False

    def calc(self, expr):
        try:
            return eval(expr)
        except (ZeroDivisionError, TypeError, NameError):
            # 如果要使用一个except子句捕获多种异常，可在一个元组中指定这些异常
            if self.muffled:
                print('Division by zero is illegal!')
            else:
                raise


if __name__ == "__main__":
    calculator = MuffledCalculator()
    # print(calculator.calc('10/0')) # 关闭了抑制功能
    # calculator.muffled = True  # 开启了抑制功能
    # print(calculator.calc('10/0'))

    # try:
    #     1 / 0
    # except ZeroDivisionError:  # 在处理上诉异常时，引发了另一个异常
    #     # raise ValueError
    #     raise ValueError from None
    #     # 可使用raise。。from。。来提自己的异常上下文，也可使用None来禁用上下文

    # while True:
    #     try:
    #         x1 = int(input("enter the first number:"))
    #         y1 = int(input("enter the second number:"))
    #         value = x1 / y1
    #         print('x/y is', value)
    #     except:
    #         print('Invalid input.please try again.')
    #     else:
    #         break

    #上面代码的改进，使用except Exception as e打印更有用的错误消息
    while True:
        try:
            x1 = int(input("enter the first number:"))
            y1 = int(input("enter the second number:"))
            value = x1 / y1
            print('x/y is', value)
        except Exception as e:
            print('Invalid input:',e)
            print('please try again.')
        else:
            break
