#-*-coding:utf-8-*-
from selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from pachong.PageObject.Login import Login_DM
from pachong.comm import openbrowser as ob
Login_DM().LoginDM()
driver=ob.webdriver
driver.switch_to.alert()

