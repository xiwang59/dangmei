#-*-coding:utf-8-*-
import pytest
import allure
from api_pytest.common.read_data import ReadData
from  api_pytest.common import myRequest
from  api_pytest.common import config_file
from api_pytest.common.mylogging import Log
from api_pytest.common import dispose_response2
from api_pytest.common.random_generation import RandomGeneration as RG

# 1.获取所有的数据  os.getcwd()返回当前目录,replace替换"testcasa"为"testdata"
path = config_file.testdata_catalog.replace("\\", "/") + "/dangmei_api.xlsx"
# print(path)
testsheet = "用例"
initdatasheet="初始值"
#获取日志路径
logging_path=config_file.testlogging_catalog.replace("\\", "/") + "/python.txt"

# 实例化日志对象
logger=Log("testapi",logging_path)

# 实例化readdata函数，获取所有的数据
alldata = ReadData(path,testsheet,initdatasheet).Read()  # cls与self的效果是一样的
logger.info (alldata)
# print(alldata)
global_dict_vars={}    #定义一个全局变量 ，把需要的返回结果存放在这个里面
global_fail_id=[]    #定义个全局变量，把请求失败的用例id放在这儿
global_xfaid=''   #定义一个全局变量 ，把没有拿到返回结果的标识放这个里面

# 调用fixtures前置函数
@pytest.mark.usefixtures("fixture_manage")
@allure.feature("接口用例")  #定义模块名称
class Test_v4:
    @allure.severity(allure.severity_level.BLOCKER) #此标记用来标识测试用例或者测试类的级别，分为blocker，critical，normal，minor，trivial5个级别
    @allure.title("{casedata[test_title]}") #定义用例标题，放在函数外
    @pytest.mark.parametrize("casedata",alldata)
    # @pytest.mark.skip("目前无法对此进行测试")   #如果下面测试函数暂时不用执行，则用skip修饰，会跳过整个函数
    def test_v4(self,casedata):
        global global_dict_vars,global_xfaid,global_fail_id    #了解下global, 全局变量
        with allure.step(casedata["test_step"]):  # 定制allure 获取测试步骤
            # logger.info("global_dict_vars的值为：{}".format(global_dict_vars))
            # logger.info("global_xfaid的值为：{}".format(global_xfaid))
            randoms = RG()
            #判断下excel中skip_type是否为1，或者判断该用例是否关联失败了请求失败的用例，如果关联了，则直接跳过
            if casedata["skip_type"]==1 or casedata["relevance_case_id"] in global_fail_id:
                pytest.skip("这个用例是因为关联的用例失败了，所以直接跳过")

            #判断没有拿到返回数据中是否有标识，且请求数据中是否有这个没有拿到的返回标识，有，直接标记失败
            if  casedata["request_data"] is not None:
                if len(global_xfaid)>0 and casedata["request_data"].find(global_xfaid) >=0:
                    pytest.xfail("这个用例是因为请求参数没有获取到的所以直接标记失败")
            if len(randoms) > 0 and casedata["request_data"] is not None:
                for key, value in randoms.items():
                    # 利用find函数查找key是否在请求数据中，a.find（b）==-1 代表不在，
                    if casedata["request_data"].find(key) != -1:
                        # 在，就替换请求数据中的key值为value
                        casedata["request_data"] = casedata["request_data"].replace(key, value)
                    # 利用find函数查找key是否在返回结果数据中，a.find（b）==-1 代表不在，
                    if casedata["expected_data"].find(key) != -1:
                        # 在，就替换请求数据中的key值为value
                        casedata["expected_data"] = casedata["expected_data"].replace(key, value)

                #  动态替换请求的数据，上个接口结束时拿到了返回数据进行了处理，新数据去替换下一个的请求数据
                #判断请求数据中是否有需要替换成全局变量的值
                #判断全局变量里面有数据，且请求数据不为空
            if len(global_dict_vars)>0 and casedata["request_data"] is not None:
                    #提取出全局变量中的key与value
                for key, value in global_dict_vars.items():
                    #1.看请求参数是否需要这个值利用find函数查找key是否在请求数据中，a.find（b）==-1 代表不在，
                    if casedata["request_data"].find(key) !=-1:
                            #在，就替换请求数据中的key值为value
                        casedata["request_data"]=casedata["request_data"].replace(key,value)
                            # print(casedata["request_data"])
                #2.看url是否需要这个返回值
                    if casedata["url"].find(key)!=-1:
                        casedata["url"]= casedata["url"].replace(key,value)
                        print(casedata["url"])

            # print(casedata["request_data"])
            if casedata['request_data']is not None:
                if "$"in casedata["request_data"]  or "$" in casedata["expected_data"]:
                    print("最后的请求数据：",casedata["request_data"])
                    print(type(casedata["request_data"]))
                    pytest.xfail("这个用例有数据没有获取到，就直接跳过吧")
                #1发起请求
            res = myRequest.MyRequests(casedata["url"], casedata["method"],json=casedata["request_data"],header=casedata["request_header"])            #判断请求返回的状态码是否为200
            if res.status_code !=200:
                global_fail_id.append(casedata["case_id"])

            #2判断数据extract_data是否有值，有的话，就要取出来放到global_vars 中，global是全局变量
            if casedata['extract_data'] is not None :
                    #动态获取了，成为全局变量
                vars=dispose_response2.Respone_data_dispose(res.json(),casedata['extract_data'])
                logger.info("返回值取出来的东西".format(vars))

                #在Respone_data_dispose函数中，如果匹配成功则返回的是一个字典，匹配不到就返回的是字符串
                if type(vars) is dict:
                    global_dict_vars= vars
                else:
                    global_xfaid=vars

            allure.dynamic.description(casedata["test_description"])  #获取用例的描述
            #数据对比

            if int(casedata['compare_type'])==0:  #判断用例是要全部匹配，还是部分匹配，0--设定全部匹配
                assert res.text == casedata['expected_data'],"对比数据失败"
                logger.info("与预期一致:{}".format( res.text))
            else:
                assert  casedata['expected_data'] in res.text,"对比数据失败"  #期望结果是否存在-实际结果中~
                logger.info("部分匹配成功:{}".format( res.text))


                #使用allure.attach可以插入附件
                # except Exception as e:
                #     with open(logging_path,"rb") as f:
                #         context=f.read()
                #         allure.attach(context,"错误日志",
                #         attachment_type=allure.attachment_type.txt)
                #     raise e



if __name__ == "__main__":
    pytest.main()
