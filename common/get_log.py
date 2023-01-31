# _*_ coding:utf-8 _*_
import logging
from logging.handlers import RotatingFileHandler
import os
from python_study.pytest_demo.common import common_util
log_path = common_util.log_path

def get_log(logname):

    logger = logging.getLogger(logname)
    logger.setLevel('INFO')
    fmt = '%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(message)s '
    log_formate = logging.Formatter(fmt)
    #日志写入路径
    file_name = os.path.join(log_path,logname)
    file_handler = RotatingFileHandler(file_name,maxBytes=20*1024*1024,backupCount=10,encoding='UTF-8')

    #显示日志
    stream_handler = logging.StreamHandler()
    #控制台输出日志的级别设置
    stream_handler.setLevel('DEBUG')
    #指定日志格式
    stream_handler.setFormatter(log_formate)


    #日志文件日志级别
    file_handler.setLevel('INFO')
    #指定日志格式
    file_handler.setFormatter(log_formate)
    logger.addHandler(file_handler)

    return logger



