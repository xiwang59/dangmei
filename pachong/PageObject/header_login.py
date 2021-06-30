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
        #option.add_argument('Authorization="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZWxvbmdUeXBlIjoxLCJleHAiOjE2MTg5MTg2NjUsImdyYW50VHlwZSI6MSwiaWF0IjoxNjE4OTE2ODY1LCJpc3MiOiJncmFudC1odWJwZCIsImp0aSI6IjE2MTg5MTY4NjU3OTEzMTcwMzkiLCJzdWIiOiI2MDUyODM3ODk5MTg1OTQ2NjI2In0.X_lkpoUdDsg4qwQ_bRSXirTDF0Ecg9dXZr8yUnBto45hnDOMCXHlx-JqbhcOoz-BjwA651HuxH0XnmCAqGc9yr_Mp30obMo723HM6kAJsrviBlu6FD8l44CP4eeRpyOT5r9GF1_CqSdTTHVg4BArKrw4gvR7s7ztI_5cAj_IguGg1gIKBC64at_aWU1lfqmgH-rRz7bAn4mcv-xDkO94cMiXS4yxYHNNXGddnjm3Lv6J3H2zQ8rmhtpsBSDSZQvlQ__ZwM_KgXYBrAR2LEDG6oXwDqnzZI7rBXA8YblKWMF1jWAPbB3Xe2q-ZwprVbdSg8lHzmt7Oc9VExdxeBcUmA"')
        option.add_argument(r"--user-data-dir=C:\Users\devz400-08\AppData\Local\Google\Chrome\User Data")
        option.add_argument('user-agent=" Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36"')
        option.add_argument('Authorization="Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZWxvbmdUeXBlIjoxLCJleHAiOjE2MTk0MTg4NDYsImdyYW50VHlwZSI6MSwiaWF0IjoxNjE5NDE3MDQ2LCJpc3MiOiJncmFudC1odWJwZCIsImp0aSI6IjE2MTk0MTcwNDYyMDI0MDcyOTMiLCJzdWIiOiIyMDE3NjEyNjMzMDYxOTgyMjExIn0.aOB-jm2TE9Ryy0-WB-5ax4FMOpjnvMYkZF4LM8ViH9pi8JCjl8bPKQEtTHPmmF9kPflV4wt5Ie2gEcx0pc_fcDvzsYaE4ll1X0N-hLy9FBql87f_TJxz-DG6muLFJn4LltH_XDu3Jj8aZ1RJLqNBgVUaXuC-I14z7I1-HavSIhRLZdfivQUm8FXq61cvL0IROQE1yCq-XnhLG3cwMpi6xDuXDu-2xggQ_gmXYtnGLKv0HfMvuSlk488rYBR-Oqbz3-fWH94FdSLdvUGJthj6CGGZcYpBHonLYwOGnQHn8hD5nDCAZs4v1QOBtsPqjbBybfpbuNz8vtNi3LtdaVxIKw"')
        #防止网站发现我们使用模拟器
        option.add_experimental_option('excludeSwitches', ['enable-automation'])
       # 初始化 -- 加载用户配置
        driver = webdriver.Chrome("chromedriver",0,chrome_options=option)
        driver.maximize_window()
        driver.get(url)
        time.sleep(5)
if __name__ == '__main__':
    CookieLogin().cl("https://admin-dm-stage.bolome.com/#/landing")