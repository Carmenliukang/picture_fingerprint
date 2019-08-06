#!/usr/bin/env python
# encoding: utf-8
'''
@author: liukang
@file: func_txy.py
@time: 2019-08-06 17:11
@desc:
'''

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import sys

sys.path.append('../')
import requests
import contextlib
from io import BytesIO  # 用于将URL 返回结果全部转换成字节流方式去处理


def get_headers():
    headers = {
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
    }
    return headers


def request_get(url, headers={}):
    '''
    获取 图片 字节流
    :param url:
    :return:
    '''
    headers = headers or get_headers()
    try:
        with contextlib.closing(requests.get(url=url, headers=headers, stream=True)) as req:
            content = req.content
        return "succ", content
    except Exception as e:
        print(e)
        return "fail", ''


def get_image_by_url(image_url):
    '''
    获取 图片 字节流
    :param image_url: 图片链接
    :return: status succ|fail Image class
    '''
    status, content = request_get(image_url)
    if status == "succ":
        byte_stream = BytesIO(content)
        print(byte_stream)
        return "succ", byte_stream
    else:
        return "fail", ""
