#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
import time
from pachong.ElementLocator import user_token as  ut
class CookieLogin:
    def cl(self,url):
        option = webdriver.ChromeOptions()
        # �ڹȸ������������chrome://version���鿴��װĿ¼������Ŀ¼
        # --user-data-dir ָ���û��ļ���User Data·��
        option.add_argument(r"--user-data-dir=C:\Users\devz400-08\AppData\Local\Google\Chrome\User Data")
        #��ֹ��վ��������ʹ��ģ����
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
       # ��ʼ�� -- �����û�����
        driver = webdriver.Chrome("chromedriver",0,option)
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)
if __name__ == '__main__':
    CookieLogin().cl("https://admin-dm-stage.bolome.com/#/landing")