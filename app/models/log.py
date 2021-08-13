#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import time

import logzero
from logzero import logger
import config


class Logzero(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = object.__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        self.logfile = os.path.join(config.logPath, '%s.log'%time.strftime('%Y-%m-%d'))
        self.logger = logger
        # console控制台输入日志格式 - 带颜色
        self.console_format = '%(color)s' \
                              '[%(asctime)s]-[%(levelname)1.1s]-[%(filename)s]-[%(funcName)s:%(lineno)d] 日志信息: %(message)s ' \
                              '%(end_color)s '
        # 创建一个Formatter对象
        self.formatter = logzero.LogFormatter(fmt=self.console_format)
        # 将formatter提供给setup_default_logger方法的formatter参数
        logzero.setup_default_logger(formatter=self.formatter)
        # 设置日志文件输出格式
        self.formater = logging.Formatter(
            '[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[%(funcName)s:%(lineno)d] 日志信息: %(message)s')
        # 设置日志文件等级
        logzero.loglevel(logging.DEBUG)
        # 输出日志文件路径和格式
        logzero.logfile(self.logfile, formatter=self.formater)

    def debug(self, msg):
        self.logger.debug(msg=msg)

    def info(self, msg):
        self.logger.info(msg=msg)

    def warning(self, msg):
        self.logger.warning(msg=msg)

    def error(self, msg):
        self.logger.error(msg=msg)

    def exception(self, msg):
        self.logger.exception(msg=msg)


log = Logzero()
if __name__ == '__main__':
    log.debug("debug")
    log.info("info")
    log.warning("warning")
    log.error("error")
    a = 5
    b = 0
    try:
        c = a / b
    except Exception as e:
        log.exception("Exception occurred")