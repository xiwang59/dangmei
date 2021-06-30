#-*-coding:utf-8-*-
import unittest
import  time
import HTMLTestRunnerNew
from again.api_request.testcase import test_v2_unittest
# from  again.api_request.common import config_file

#创建用例集
suite=unittest.TestSuite()
ul=unittest.TestLoader()
suite.addTests(ul.loadTestsFromModule(test_v2_unittest))


now=time.strftime('%H-%M-%S')
name="apitest"+now+".html"
fp=open(name,"wb+")

#创建执行者
runner=HTMLTestRunnerNew.HTMLTestRunner(stream=fp,title="api接口测试",verbosity=2)
runner.run(suite)