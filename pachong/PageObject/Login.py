#-*-coding:utf-8-*-
from selenium import webdriver
from  selenium.webdriver import ActionChains
from time import sleep
from pachong.ElementLocator import user_token as  ut
from pachong.ElementLocator import login_element as le
from selenium.webdriver import ChromeOptions  # 需要导入的类
from pachong.comm import openbrowser as ob
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Login_DM:
    def LoginDM(self):
        driver=ob.webdriver
        #访问链接
        driver.get(ut.loginurl)
        driver.maximize_window()
        #等待3秒
        driver.implicitly_wait(3)
        driver.find_element_by_xpath(le.input_user).send_keys(ut.user)
        driver.find_element_by_xpath(le.input_pasewor).send_keys(ut.paseword)
        #滑块开始
        begin=driver.find_element_by_xpath(le.slider_begin)
        #按住鼠标左键
        action=ActionChains(driver)
        #移动你要的距离
        action.click_and_hold(begin).perform()
        action.reset_actions()
        action.move_by_offset(333, 0).release().perform()
        action.click_and_hold()
        sleep(2)
        driver.find_element_by_xpath(le.login_user).click()
        # # 等待alert弹出框可见
        # WebDriverWait(driver, 20).until(ec.alert_is_present())
        # # 从html页面切换到alert弹框
        # al=driver.switch_to.alert
        # al.dismiss()
if __name__ == '__main__':
    Login_DM().LoginDM()