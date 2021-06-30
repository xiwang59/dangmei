#-*-coding:utf-8-*-
import pytest
from common.read_data import ReadData
from common import config_file
from common import login_token
#scope="module"相当于setupclass，默认是function"，autouse默认为False，使用autouse=True后，其他的测试脚本会自动用这个文件
@pytest.fixture(scope="function",autouse=True)
def fixture_manage():
    print("setup-开始测试啦")
    # # 1.获取所有的数据  os.getcwd()返回当前目录,replace替换"testcasa"为"testdata"
    # path = config_file.testdata_catalog.replace("\\", "/") + "/dangmei_api.xlsx"
    # # print(path)
    # testsheet = "用例"
    # initdatasheet = "初始值"
    # # 2.实例化readdata函数，获取所有的数据
    # alldata = ReadData(path, testsheet, initdatasheet).Read()  # cls与self的效果是一样的
    # #将当次获取的token替换成最新的
    # for i in alldata:
    #     new_token=i['request_header'].replace("${token}",login_token.token)
    #     i['request_header']=new_token
    # return alldata


    yield
    print("teardown 后置操作")
if __name__ == '__main__':

    print(fixture_manage())



