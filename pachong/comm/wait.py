#coding=gbk
from selenium import webdriver
from selenium.webdriver import ChromeOptions  # 需要导入的类
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import logging
from pachong.comm.logging_class import Log
from pachong.comm import openbrowser as ob
class WaitMoment:
    driver=ob.webdriver
    #等待某元素是否显示
    def wait_xpath(self, x_path):
        try:
            WebDriverWait(self.driver,5,1).until(
                EC.visibility_of_all_elements_located((By.XPATH, x_path)))
        except:
            Log().error(u"元素%s显示异常" % (x_path))
            self.driver.close()
    #等待新窗口显示
    def wait_newwindows(self):
        try:
            WebDriverWait(self.driver,5,1).until(EC.new_window_is_opened())
        except:
            Log().error("新窗口没有打开")
            self.driver.close()



