#!/usr/bin/env python
# encoding: utf-8
'''
@author: liukang
@file: run.py
@time: 2019-08-02 14:00
@desc: 用于校验
'''

# 备注：这里需要优先导入猴子补丁才可以
from lib.gevent_run import Concurrent
from lib.func_txy import get_image_by_url
from lib.image_similarity import PictureFingerprint
from lib.log import Log

if __name__ == '__main__':
    logger = Log().logger
    concurrent = Concurrent()

    logger.info("开始运行")
    pic_url = 'https://sf6-ttcdn-tos.pstatp.com/obj/temai/Fl8I389Bn_jDByCjmCV9bs_GO4SN.JPG'
    image_url = 'https://sf6-ttcdn-tos.pstatp.com/obj/temai/Fq3KhSPbczC6A0yAV4MEb0oNSiG-www800-800'
    picture_fingerprint = PictureFingerprint()

    concurrent.add(get_image_by_url, pic_url)
    concurrent.add(get_image_by_url, image_url)

    res = concurrent.run()
    pic_byte = res[0][1]
    image_byte = res[1][1]

    res = picture_fingerprint.image_check_res(pic_byte, image_byte)
    logger.info("图片对比结果:{}\n图片1:{}\n图片2:{}".format(res, pic_url, image_url))
    print(res)

    pic_file = "image/图片1.jpeg"
    image_file = "image/图片2.jpeg"
    res = picture_fingerprint.image_check_res(pic_file, image_file)
    logger.info("图片对比结果:{}\n图片1:{}\n图片2:{}".format(res, pic_file, image_file))
    logger.info("结束运行")
    print(res)
