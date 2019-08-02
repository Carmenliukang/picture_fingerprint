#!/usr/bin/env python
# encoding: utf-8
'''
@author: liukang
@file: run.py
@time: 2019-08-02 14:00
@desc: 用于校验
'''

from lib.image_similarity import PictureFingerprint
from lib.log import Log

if __name__ == '__main__':
    log = Log()
    log.all_log(all_file="log/all.log")
    log.err_log(err_file="log/err.log")
    logger = log.logger

    logger.info("开始运行")
    pic_url = 'https://sf6-ttcdn-tos.pstatp.com/obj/temai/Fl8I389Bn_jDByCjmCV9bs_GO4SN.JPG'
    image_url = 'https://sf6-ttcdn-tos.pstatp.com/obj/temai/Fq3KhSPbczC6A0yAV4MEb0oNSiG-www800-800'
    picture_fingerprint = PictureFingerprint()
    res = picture_fingerprint.image_check_res(pic_url, image_url)
    logger.info("图片对比结果:{}\n图片1:{}\n图片2:{}".format(res, pic_url, image_url))

    pic_file = "image/图片1.jpeg"
    image_file = "image/图片2.jpeg"
    res = picture_fingerprint.image_check_res_by_filename(pic_file, image_file)
    logger.info("图片对比结果:{}\n图片1:{}\n图片2:{}".format(res, pic_file, image_file))
    logger.info("结束运行")
