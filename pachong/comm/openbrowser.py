#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver import ChromeOptions  # 需要导入的类

option =ChromeOptions()
#隐藏是否保存密码弹窗
prefs = {"":""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
option.add_experimental_option("prefs", prefs)
        #防止网站发现我们使用模拟器79版本之前
option.add_experimental_option('excludeSwitches', ['enable-automation'])

        # 初始化 -- 加载用户配置
webdriver = webdriver.Chrome("chromedriver",0,option)
        # 防止网站发现我们使用模拟器79版本之后
webdriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": '''
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
        '''
        })
#隐性等待，每个执行最多等待10秒
webdriver.implicitly_wait(10)

