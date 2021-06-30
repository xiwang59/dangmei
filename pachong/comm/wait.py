#coding=gbk
from selenium import webdriver
from selenium.webdriver import ChromeOptions  # ��Ҫ�������
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from pachong.comm.logging_class import Log
from pachong.comm import openbrowser as ob
class WaitMoment:
    driver=ob.webdriver
    #�ȴ�ĳԪ���Ƿ���ʾ
    def wait_xpath(self, x_path):
        try:
            WebDriverWait(self.driver,5,1).until(
                EC.visibility_of_all_elements_located((By.XPATH, x_path)))
        except:
            Log().error(u"Ԫ��%s��ʾ�쳣" % (x_path))
            self.driver.close()
    #�ȴ��´�����ʾ
    def wait_newwindows(self):
        try:
            WebDriverWait(self.driver,5,1).until(EC.new_window_is_opened())
        except:
            Log().error("�´���û�д�")
            self.driver.close()



