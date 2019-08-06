#!/usr/bin/env python
# encoding: utf-8
'''
@author: liukang
@file: gevent_run.py
@time: 2019-08-02 15:33
@desc: 用于降低系统耦合的情况下实现并发请求
'''

from gevent import monkey

# 关闭 thread 重载的原因是因为 多进程的并发
monkey.patch_all(dns=False, thread=False)

import gevent

import ssl

ssl._create_default_https_context = ssl._create_unverified_context


class Concurrent(object):
    ''' 使用协程实现并发 '''

    def __init__(self):
        self.init()

    def add(self, func, *args, **kwargs):
        self.gevent_spawn.append(gevent.spawn(func, *args, **kwargs))

    def run(self):
        ''' 使用 协程方式 '''
        gevent.joinall(self.gevent_spawn)
        result = [t.value for t in self.gevent_spawn]
        return result

    def init(self):
        ''' 初始化队列 '''
        self.gevent_spawn = []


def func(num):
    gevent.sleep(num)
    return num, list


if __name__ == '__main__':
    concurrent = Concurrent()
    for i in range(3):
        concurrent.add(func, i)

    result = concurrent.run()
    print(result)
