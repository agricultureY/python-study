#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"文档测试"
__author__ = 'ycn'

import doctest


class Dict(dict):
    """
    Simple dict but also support access as x.y style.
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    """

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % item)

    def __setattr__(self, key, value):
        self[key] = value


if __name__ == '__main__':
    # doctest.testmod是测试模块，verbose默认是False,意思是出错才用提示；True，对错都有执行结果
    doctest.testmod(verbose=True)
