#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'多进程'
__author__ = 'ycn'
import os
from multiprocessing import Process

# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。
# 子进程永远返回0，而父进程返回子进程的ID。这样做的理由是，一个父进程可以fork出很多子进程，
# 所以，父进程要记下每个子进程的ID，而子进程只需要调用getPid()就可以拿到父进程的ID。
print('Process (%s) start...' % os.getpid())


# Python的os模块封装了常见的系统调用，其中就包括fork，可以在Python程序中轻松创建子进程
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
# 由于Windows没有fork调用，os.fork()只能运行在Linux、Mac上
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。

# multiprocessing模块就是跨平台版本的多进程模块。
# multiprocessing模块提供了一个Process类来代表一个进程对象
# 子进程要执行的代码
def runProc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动。
    p = Process(target=runProc, args=('test',))
    print('Child process will start.')
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print('Child process end.')
