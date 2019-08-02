#!/usr/bin/env python
# encoding: utf-8
'''
@author: liukang
@file: log.py
@time: 2019-08-02 14:42
@desc:
'''

import datetime
import logging.handlers


class Log(object):
    def __init__(self, specified_name="mysqlogger", lever="DEBUG"):
        self.specified_name = specified_name
        self.lever = lever
        self._init()

    def _init(self):
        self.logger = logging.getLogger(self.specified_name)
        self.logger.setLevel(self.lever)

    def all_log(self, all_file):
        self.rf_handler = logging.handlers.TimedRotatingFileHandler(filename=all_file, when='midnight', interval=1,
                                                                    backupCount=7,
                                                                    atTime=datetime.time(0, 0, 0, 0), encoding="utf-8")
        self.rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

        self.logger.addHandler(self.rf_handler)

    def err_log(self, err_file):
        self.f_handler = logging.FileHandler(err_file, encoding="utf-8")
        self.f_handler.setLevel(logging.ERROR)
        self.f_handler.setFormatter(
            logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

        self.logger.addHandler(self.f_handler)


if __name__ == '__main__':
    log = Log()
    log.all_log(all_file="../log/all.log")
    log.err_log(err_file="../log/err.log")
    logger = log.logger

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warning message')
    logger.error('error message')
    logger.critical('critical message')
