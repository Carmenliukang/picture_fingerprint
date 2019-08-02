# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 10:01
# @Author  : liukang
# @FileName: run.py

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

import sys

sys.path.append('../')
import requests
import imagehash
import contextlib
from PIL import Image
from io import BytesIO  # 用于将URL 返回结果全部转换成字节流方式去处理


class PictureFingerprint(object):
    ''' 封装的一个用于计算图片相似度的基类，使用的是 dhash 方式进行说明 '''

    def __init__(self):
        self.headers = {
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36"
        }

    def request_get(self, url):
        '''
        获取 图片 字节流
        :param url:
        :return:
        '''
        try:
            with contextlib.closing(requests.get(url=url, headers=self.headers, stream=True)) as req:
                content = req.content
            return "succ", content
        except Exception as e:
            print(e)
            return "fail", ''

    def get_res(self, original_image_hash, contrast_image_hash):
        '''
        获取汉明距离
        :param original_image_hash:原图hash数值
        :param contrast_image_hash:对比图hash数值
        :return:
        '''
        num = 0
        if len(original_image_hash) != len(contrast_image_hash):
            return len(original_image_hash)
        else:
            for i, k in zip(original_image_hash, contrast_image_hash):
                if i != k:
                    num += 1
        return num

    def get_phash(self, image):
        '''
        获取图片的 dhash 数值
        :param image: PIL 势力
        :return: string 图片 dhash 结果
        '''
        phash_res = str(imagehash.dhash(image))
        return phash_res

    def get_image_by_url(self, image_url):
        '''
        获取 图片
        :param image_url: 图片链接
        :return: status succ|fail Image class
        '''
        status, content = self.request_get(image_url)
        if status == "succ":
            byte_stream = BytesIO(content)
            image = Image.open(byte_stream)
            image = image.resize((32, 32), Image.BILINEAR)
            return "succ", image
        else:
            return "fail", ""

    def get_image_by_filename(self, image_name):
        '''
        :param image_name: 图片路径
        :return: status succ|fail Image class
        '''
        try:
            image = Image.open(image_name)
            image = image.resize((32, 32), Image.BILINEAR)
            return "succ", image
        except Exception as e:
            print(e)
            return "fail", ""

    def image_check_res(self, original_image_url, contrast_image_url):
        try:
            original_status, original_image = self.get_image_by_url(original_image_url)
            contrast_status, contrast_image = self.get_image_by_url(contrast_image_url)
            if original_status != "succ" or contrast_status != "succ":
                print("fail")
                return 16
            else:
                original_image_hash = self.get_phash(original_image)
                contrast_image_hash = self.get_phash(contrast_image)
                return self.get_res(original_image_hash, contrast_image_hash)
        except Exception as e:
            print(e)
            return 16

    def image_check_res_by_filename(self, original_image_name, contrast_image_name):
        '''
        获取 图片相似度的结果
        :param original_image_name: 原始图
        :param contrast_image_name: 对比图
        :return:
        '''
        try:
            original_status, original_image = self.get_image_by_filename(original_image_name)
            contrast_status, contrast_image = self.get_image_by_filename(contrast_image_name)
            if original_status != "succ" or contrast_status != "succ":
                print("fail")
                return 16
            else:
                original_image_hash = self.get_phash(original_image)
                contrast_image_hash = self.get_phash(contrast_image)
                return self.get_res(original_image_hash, contrast_image_hash)
        except Exception as e:
            print(e)
            return 16
