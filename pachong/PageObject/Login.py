#-*-coding:utf-8-*-
from selenium import webdriver
from  selenium.webdriver import ActionChains
from time import sleep
from pachong.ElementLocator import user_token as  ut
from pachong.ElementLocator import login_element as le
from selenium.webdriver import ChromeOptions  # ��Ҫ�������
from pachong.comm import openbrowser as ob
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Login_DM:
    def LoginDM(self):
        driver=ob.webdriver
        #��������
        driver.get(ut.loginurl)
        driver.maximize_window()
        #�ȴ�3��
        driver.implicitly_wait(3)
        driver.find_element_by_xpath(le.input_user).send_keys(ut.user)
        driver.find_element_by_xpath(le.input_pasewor).send_keys(ut.paseword)
        #���鿪ʼ
        begin=driver.find_element_by_xpath(le.slider_begin)
        #��ס������
        action=ActionChains(driver)
        #�ƶ���Ҫ�ľ���
        action.click_and_hold(begin).perform()
        action.reset_actions()
        action.move_by_offset(333, 0).release().perform()
        action.click_and_hold()
        sleep(2)
        driver.find_element_by_xpath(le.login_user).click()
        # # �ȴ�alert������ɼ�
        # WebDriverWait(driver, 20).until(ec.alert_is_present())
        # # ��htmlҳ���л���alert����
        # al=driver.switch_to.alert
        # al.dismiss()
if __name__ == '__main__':
    Login_DM().LoginDM()