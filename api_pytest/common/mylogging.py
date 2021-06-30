#-*-coding:utf-8-*-
__author__ = 'zz'
#encoding=utf-8
import logging
from api_pytest.common import  config_file

class Log:
    def __init__(self,log_name,file_name):
        self.log_name=log_name
        self.file_name=file_name

    def logger(self,level,msg):
        #日志收集器
        my_log=logging.getLogger(self.log_name)
        my_log.setLevel('DEBUG')

        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')

        fh=logging.FileHandler(self.file_name,encoding="utf-8")
        fh.setFormatter(formatter)
        fh.setLevel('DEBUG')

        my_log.addHandler(fh)

        if level.upper()=='DEBUG':
            my_log.debug(msg)
        elif level.upper()=='INFO':
            my_log.info(msg)
        elif level.upper()=='WARNING':
            my_log.warning(msg)
        elif level.upper()=='ERROR':
            my_log.error(msg)
        elif level.upper()=='critical':
            my_log.critical(msg)
        else:
            my_log.exception(msg)

        my_log.removeHandler(fh)

    def debug(self,msg):
        self.logger('debug',msg)

    def info(self,msg):
        self.logger('info',msg)

    def warning(self,msg):
        self.logger('warning',msg)

    def error(self,msg):
        self.logger('error',msg)

    def critical(self,msg):
        self.logger('critical',msg)

    def exception(self,msg):
        self.logger('exception', msg)


if __name__=='__main__':
    logger=Log("xigua",config_file.testlogging_catalog+"/python.txt")
    logger.info("我终于写完成了一个日志")