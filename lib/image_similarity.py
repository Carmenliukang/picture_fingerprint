# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-05-29 10:01
# @Author  : liukang
# @FileName: run.py


from io import BytesIO

import imagehash
from PIL import Image


class ImageHash(object):
    ''' 用于计算相关的 cookie 存放设置'''

    def __init__(self):
        pass

    def get_phash(self, img):
        '''
        获取图片的 dhash 数值
        :param image: PIL 势力
        :return: string 图片 dhash 结果
        '''
        try:
            image = Image.open(img)
            phash_res = str(imagehash.dhash(image))
            return phash_res
        except Exception as e:
            print(e)
            return ""


class PictureFingerprint(ImageHash):
    ''' 封装的一个用于计算图片相似度的基类，使用的是 dhash 方式进行说明 '''

    def __init__(self):
        super(PictureFingerprint, self).__init__()

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

    def image_check_res(self, original_image, contrast_image):
        '''
        计算两张图片的相似度
        :param original_image: 图片1  image file name or byte
        :param contrast_image: 图片2  image file name or byte
        :return: int 对比的结果。 1-5 相似 6-10 有一定的差别 11-16 完全不相同
        '''
        try:
            original_image_hash = self.get_phash(original_image)
            contrast_image_hash = self.get_phash(contrast_image)
            return self.get_res(original_image_hash, contrast_image_hash)
        except Exception as e:
            print(e)
            return 16


if __name__ == '__main__':
    with open("../image/图片1.jpeg", "rb") as f:
        image_1 = f.read()
        image_1 = BytesIO(image_1)

    with open("../image/图片2.jpeg", "rb") as f:
        image_2 = f.read()
        image_2 = BytesIO(image_2)

    picture_fingerprint = PictureFingerprint()
    res = picture_fingerprint.image_check_res(image_1, image_2)
    print(res)
