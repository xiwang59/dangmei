#-*-coding:utf-8-*-
#-*-coding:utf-8-*-
from selenium import webdriver
from  selenium.webdriver import ActionChains
from time import sleep
from pachong.ElementLocator import user_token as  ut
from selenium.webdriver import ChromeOptions  # 需要导入的类
from pachong.PageObject.Login import Login_DM
from pachong.InputData import CreatePachong as cp
from pachong.comm import openbrowser as ob
from pachong.ElementLocator import  create_crawlers_element as cc
from pachong.comm.wait import WaitMoment as WM

class RSS:
    def create_rss(self):
        driver=ob.webdriver
        Login_DM().LoginDM()
        sleep(3)
        driver.get(ut.pachongurl)
        WM().wait_xpath(cc.new_crawlers)
        #如果元素被截获，使用script的方式
        newcrawlers=driver.find_element_by_xpath(cc.new_crawlers)
        driver.execute_script("arguments[0].click();", newcrawlers)
        driver.find_element_by_xpath(cc.crawlers_type).click()
        driver.find_element_by_xpath(cc.determine).click()
        WM().wait_newwindows()
        sleep(10)
        #切换到新的窗口
        windows=driver.window_handles
        driver.switch_to.window(windows[-1])
        WM().wait_xpath(cc.crawlers_name)
        driver.find_element_by_xpath(cc.crawlers_name).send_keys(cp.createpa["name"])
        #添加新的融合号
        # driver.find_element_by_xpath(cc.add_mp).click()
        # sleep(3)
        # driver.find_element_by_xpath(cc.mp_name).send_keys(cp.createpa["mp"])
        # driver.find_element_by_xpath(cc.mp_type).click()
        # driver.find_element_by_xpath(cc.mp_type1).click()
        # driver.find_element_by_xpath(cc.sheng).click()
        # driver.find_element_by_xpath(cc.sheng1).click()
        # driver.find_element_by_xpath(cc.shi).click()
        # driver.find_element_by_xpath(cc.shi1).click()
        # driver.find_element_by_xpath(cc.sure).click()
        driver.find_element_by_xpath(cc.mp).send_keys(cp.createpa["mp"])
        WM().wait_xpath(cc.select_mp)
        driver.find_element_by_xpath(cc.select_mp).click()
        WM().wait_xpath(cc.add_lanmu)
        driver.find_element_by_xpath(cc.add_lanmu).click()
        WM().wait_xpath(cc.input_lanmu)
        driver.find_element_by_xpath(cc.input_lanmu).send_keys(cp.createpa["collectorApply"])
        driver.find_element_by_xpath(cc.sure).click()
        WM().wait_xpath(cc.next_step)
        driver.find_element_by_xpath(cc.next_step).click()
        WM().wait_xpath(cc.address)
        driver.find_element_by_xpath(cc.address).send_keys(cp.createpa["url"])
        driver.find_element_by_xpath(cc.filished).click()
        sleep(3)
if __name__ == '__main__':
    RSS().create_rss()