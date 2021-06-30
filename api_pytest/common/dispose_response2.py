#-*-coding:utf-8-*-
import  re
#用正则表达式获response_data的数据
def Respone_data_dispose(response_data,extract_data):
    #第一个参数不能为空或者none
    if response_data is not None or response_data =='':
        dict_extract_data={}
        temp=extract_data.split("=",1)
        #方法1
        # a = re.compile(temp[1], re.MULTILINE | re.DOTALL)
        # b = a.findall(response_data, re.MULTILINE | re.DOTALL)

        #方法2
        # print(str(response_data))
        str_response_data=str(response_data)
        b=re.findall(temp[1],str_response_data)
        if len(b) !=0:
            dict_extract_data[temp[0]]=b[0]
            return dict_extract_data
        else:
            return False
if __name__ == '__main__':
    response_data={'errCode': 0, 'errMsg': '',
         'data': {'id': '3458764513820541153', 'sign': '王倩', 'mpStatus': 0, 'mpSource': 0, 'roles': ['MP_MANAGER'],
                  'createAt': 1624590038, 'needAnnualVerification': False,
                  'mp': {'icon': 'default_logo.png', 'name': '王倩', 'type': 0, 'intro': '',
                         'domain': {'id': '5', 'name': '科技'},
                         'imageUrlMap': {'icon': 'https://cb-dm-stage.bolome.com/hubpd-stage/default_logo.png'},
                         'credible': 0},
                  'org': {'name': '', 'license': '', 'confirm': '', 'qualification': '', 'location': '上海-上海',
                          'officialWebsite': '', 'imageUrlMap': {'confirm': '', 'license': '', 'qualification': ''}},
                  'registrant': {'name': '', 'type': '', 'code': '', 'img': '', 'email': '',
                                 'imageUrlMap': {'img': ''}}, 'phone': ''}}

    # response_data={"errCode":0,"errMsg":"","data":{"id":"1152921504606877245","sign":"邓丹丹","mpStatus":0,"mpSource":0,"roles":["MP_MANAGER"],"createAt":1624534040,"needAnnualVerification":false,"mp":{"icon":"default_logo.png","name":"邓丹丹","type":0,"intro":"","domain":{"id":"5","name":"科技"},"imageUrlMap":{"icon":"https://cb-dm-stage.bolome.com/hubpd-stage/default_logo.png"},"credible":0},"org":{"name":"","license":"","confirm":"","qualification":"","location":"上海-上海","officialWebsite":"","imageUrlMap":{"confirm":"","license":"","qualification":""}},"registrant":{"name":"","type":"","code":"","img":"","email":"","imageUrlMap":{"img":""}},"phone":""}}
    extract_data="${id}='id': '(.*?)', 'sign':"
    data=Respone_data_dispose(response_data,extract_data)
    print(data)