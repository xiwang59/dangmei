#-*-coding:utf-8-*-
from selenium import webdriver
from selenium.webdriver import ChromeOptions  # ��Ҫ�������

option =ChromeOptions()
#�����Ƿ񱣴����뵯��
prefs = {"":""}
prefs["credentials_enable_service"] = False
prefs["profile.password_manager_enabled"] = False
option.add_experimental_option("prefs", prefs)
        #��ֹ��վ��������ʹ��ģ����79�汾֮ǰ
option.add_experimental_option('excludeSwitches', ['enable-automation'])

        # ��ʼ�� -- �����û�����
webdriver = webdriver.Chrome("chromedriver",0,option)
        # ��ֹ��վ��������ʹ��ģ����79�汾֮��
webdriver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": '''
        Object.defineProperty(navigator, 'webdriver', {
        get: () => undefined
        })
        '''
        })
#���Եȴ���ÿ��ִ�����ȴ�10��
webdriver.implicitly_wait(10)

