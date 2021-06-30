#-*-coding:utf-8-*-
#专门放配置文件的路径，方便获取到绝对的路径
import os

catalog=os.path.split(os.path.abspath(__file__))[0]#获取当前文件所在目录
testdata_catalog=catalog.replace("common","testdata")
testmain_catalog=catalog.replace("common","testmain")
testlogging_catalog=catalog.replace("common","testlogging")
