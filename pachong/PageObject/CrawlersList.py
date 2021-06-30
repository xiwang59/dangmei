#-*-coding:utf-8-*-
from selenium import webdriver
from time import  sleep
from pachong.ElementLocator import crawlers_list_element as  cl
class CL:
    def __init__(self, driver):
        self.driver = driver
