#!/usr/bin/env python
# _*_ coding:utf-8 _*

#在linux/unix/mac上运行，windows没有fork这个接口
# import os
# print('Process (%s) start.... ' % os.getpid())
# #Only works on Unix/Linux/Mac
# pid = os.fork()
# if pid ==0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(),os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(),pid))

#multiprocessing模块提供了一个process类来代表一个进程对象
from multiprocessing import Process
import os

#子进程要执行的代码
def run_proc(name):
    print('Run child process %s(%s)....'%(name,os.getpid()))

if __name__=='__main__':
    print('Parent process %s.'%os.getpid())
    p=Process(target=run_proc,args=('test',))
    print('Child process will start.')
    p.start()
    p.join() #join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')

