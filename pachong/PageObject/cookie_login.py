#-*-coding:utf-8-*-
from selenium import webdriver
from time import  sleep
from pachong.ElementLocator import user_token as  ut
class CookieLogin:
    def __init__(self, driver):
        self.driver = driver
    def cl(self,url,cookie1,cookie2):
        self.driver.get(url)
        self.driver.add_cookie(cookie1)
        self.driver.add_cookie(cookie2)
        self.driver.refresh()
        self.driver.get(url)
if __name__ == '__main__':
    url="https://admin-dm-stage.bolome.com/#/landing"
    cookie1={"name":"_umdata","value":"G6D4B6CF3EAE093ECFCABA5AE06F8C9F51DE14C"}
    cookie2={"name":"_uab_collina","value":"159659413519101486038188"}
    driver=webdriver.Chrome()
    CookieLogin(driver).cl(url,cookie1,cookie2)
