#-*-coding:utf-8-*-
from selenium import webdriver
from time import sleep
import time
from pachong.ElementLocator import user_token as  ut
class CookieLogin:
    def cl(self,url):
        option = webdriver.ChromeOptions()
        # 在谷歌浏览器中输入chrome://version，查看安装目录及缓存目录
        # --user-data-dir 指定用户文件夹User Data路径
        option.add_argument(r"--user-data-dir=C:\Users\devz400-08\AppData\Local\Google\Chrome\User Data")
        #防止网站发现我们使用模拟器
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
       # 初始化 -- 加载用户配置
        driver = webdriver.Chrome("chromedriver",0,option)
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)
if __name__ == '__main__':
    CookieLogin().cl("https://admin-dm-stage.bolome.com/#/landing")