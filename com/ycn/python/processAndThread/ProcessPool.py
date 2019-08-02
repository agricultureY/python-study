#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'进程池'
__author__ = 'ycn'

import os
import random
import time
from multiprocessing import Pool


# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程
# 定义进程运行时间方法
def longTimeTask(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # 创建进程池
    p = Pool(4)
    for i in range(5):
        p.apply_async(longTimeTask, args=(i,))
    print('Waiting for all sub processes done...')
    # 关闭进程池
    p.close()
    # 等待所有子进程执行完毕,调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了
    p.join()
    print('All sub processes done.')
