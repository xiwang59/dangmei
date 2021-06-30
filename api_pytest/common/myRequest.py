#-*-coding:utf-8-*-
import  requests
from requests.adapters import HTTPAdapter
def MyRequests(url,method,json=None,header=None):
    s = requests.session()
    # max_retries=3 重试3次
    s.mount('http://', HTTPAdapter(max_retries=3))
    s.mount('https://', HTTPAdapter(max_retries=3))
    #判读下请求数据是否为空
    if  json  is not None:
        json=eval(json)   #不为空，转换成字典格式
    if header is not None:
        header=eval(header)
    # 1.判断请求的方法get/post
    if method=="get":
        res=s.request("get",url,headers=header)
    elif method=="post":
        res=s.request("post",url,headers=header,json=json)
    elif method=="put":
        res=s.request("put",url,headers=header,json=json)
    elif method =="del":
        res=s.request("delete",url,json)
    else:
        res=None
    return res
if __name__ == '__main__':
    url="https://api-admin-dm-stage.bolome.com/accounts/mp?size=10&page=1&keyword=西瓜"
    method="get"
    header={"Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZWxvbmdUeXBlIjoxLCJleHAiOjE2MjQ5NTEzMDYsImdyYW50VHlwZSI6MSwiaWF0IjoxNjI0OTQ5NTA2LCJpc3MiOiJncmFudC1odWJwZCIsImp0aSI6IjE2MjQ5NDk1MDY2OTQ5OTc2MTQiLCJzdWIiOiI2MDUyODM3ODk5MTg1OTQ2NjI2In0.MUbIUee6os1kFEqwXt9hevnrqlc7TcbfUOQ3wtItHgprHvaJfYSasVZQ1g_gmflE-kFl4tAW5ow7a4OZkmF88vqE9xfbZLLmANztJ8kcuHKydaaxcuEzXTqZY_lpExONz64zTIae7aNBGbbwbGQoJx4Vfm8MWDdi9_NpXqQ8NlNLQ185RoiPoVMAidCc2op6dlMjsgaM6wWsWw2n0MjGEbUb3p9tJYQrCu7Ub6D9OZo5NegnbT0t9u0cKhNuwaKkcFadNZxJ47o9Tq9xrwCXvzKiHWUQQgxCt1Ocfl_cO3nlcu_aPWbIILLUE9Lrr-oMdzsrwhDDCNsEHZpNfdFYWw"}
    # header={"Authorization":"Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZWxvbmdUeXBlIjoxLCJleHAiOjE2MjQ1MzA1NjMsImdyYW50VHlwZSI6MSwiaWF0IjoxNjI0NTI4NzYzLCJpc3MiOiJncmFudC1odWJwZCIsImp0aSI6IjE2MjQ1Mjg3NjMyNjQ5MTk1OTUiLCJzdWIiOiI2MDUyODM3ODk5MTg1OTQ2NjI2In0.7kS3zeXrXkKsG37Dhk6h0tzOO_hk0CUJHA5rDh_yXHgZ2qaViWkR7BZ4UgNS6cAR1wU_ctj4F6Jo4WzelwnjLm3kgA1wngt9fczEaaXSHb6ZPXJOlYzDnIYcjQj4B7MKh7k3Dtl1R8uaWAnDNizYgHTPGZD6K2tJ8pes0pzJokmTv8ep8zwwOwiYIO0QLzvcs9fBHonxnmGyq9I-qs-ipskyUXBFliSrbZVdRCsd940EI2UT41dK6rIA86qM5Vu-_X8eueUBKXD2u1w6hcZIz9SICZmtgOQqTzqky9FeCGbrkwyWHbcr33qv8fxpAmUXNxgLIO5Me3dhndC-cLDviQ"}
    # header={'Authorization':'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZWxvbmdUeXBlIjoxLCJleHAiOjE2MjQ1MzAzOTQsImdyYW50VHlwZSI6MSwiaWF0IjoxNjI0NTI4NTk0LCJpc3MiOiJncmFudC1odWJwZCIsImp0aSI6IjE2MjQ1Mjg1OTQ1NzgxMzM0MjQiLCJzdWIiOiI2MDUyODM3ODk5MTg1OTQ2NjI2In0.21xxp5PfqUeP9elTyNYUyQPhF38g8UPaHHGC-TxrAwtMRt1ugQPcVytNPx9-44y87qG_K774QxkEduHE67sqLHnhLzl3w-BJyJozR8io85XU2R26CsN6svTWsQHayfUSTxeWL7HsP3LOkgklA0xjuzJECUPFNDwqj80TFAjqH3EA_KcGh1W0t4h0V-3R9cNz2DeUKLkpmFITofpPOtQOHkDGmQlp7FXaUU__l5tzz5TKj24y_w4cnWxxLAuSYTZTFZwt_sLMFlEABVbO9pV4zBlk1pjo18Ag8ocIpualE4z-oo4u9DHmLZ5j1AwyqSoJCG9b67XUdGF1d3ZLYKZQDA'}
    # header={"Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJiZWxvbmdUeXBlIjoxLCJleHAiOjE2MjQ1Mjg1OTgsImdyYW50VHlwZSI6MSwiaWF0IjoxNjI0NTI2Nzk4LCJpc3MiOiJncmFudC1odWJwZCIsImp0aSI6IjE2MjQ1MjY3OTg3NjUwNTk5NDIiLCJzdWIiOiI2MDUyODM3ODk5MTg1OTQ2NjI2In0.ITspYpMMJoAd7J3dKzMVy6SjxP7FC9zJrCR38xQhoFlWydlLLYjymXSlzfgzl5FQG14BBFtIDZvknqi17SKFBE4dMYAF3OH1OGOzfu9l8Wy3Az9q78kIhe9sR6NrETgB2qPEQvt3oqtiFsc6bSUWe39lNJK6rfIim9YYAj90fkZIR79WnbAp7RMv5FrFWh--i8UiVkbG_IvWk4AJAM3vlaugWGTEeMtPJYdk5op2HZsvUfmLvuqH8_bCDPXpN8CkiWEcJVVIRCwMl1Dn8WQIyU5Owi73FijK_RYYVgbWPXTUKz7pKXViEEoOkuYjS-4-nMplfa8K-G4FZ8DCfuXGcg"}
    print(MyRequests(url,method,header=str(header)).status_code)
    # url="https://api-admin-dm-stage.bolome.com/login"
    # method="post"
    # json={
    #     "signId": "测试竹笋",
    #     "password": "QAZwsx123",
    #     "loginType": 0,
    #     "captcha":{
    #         "cSessionId": "0152JIZgtMjy7iQLwB8JakWWlj_CejnEFyufXFVghoZTydbpmRSzeiZ903hWOuOJDAKHRusUhtFuMRhS68u_R5J9ILksAsi_jOiYiArUQCcwdB868MvOl8tcUwL1pP4CneJFs0kqDa_QKAjr8GlKlBF67UDjc9t1R6WUgzwqsFszdmWh1ixrgaaySPuOZpAaU-nALcbseNIzyI6tVyQ-jUIA",
    #         "sig": "05a1C7nT4bR5hcbZlAujcdyTIjGz0Egt91iX1IO3BzqF7hV0jTbGeQfzcZH0xvdWXr5J84kcgH9c9zp1yfKofbpYPJZNCILq88zK8kwvlUzftiGp4-RSlo2wwzH2kqN58cClOZ0tlsrSyFEh-uBHcO3U8hB6j_6iOHPukehFkMLvoOCzXwBEkJKhq2dgVGQlVWmYjNqZ2POxkOytMuqObDXsuQ2awYSBPbiPoOMehcPdiJ5qhY_MrcYaNOV0HVaB0v01Ar3YahFiLVfGqfBS59zuSGQDFnJXQXe3cTNWNQ2ISK5e8oi-qqAULm58huKu0pFxr74Oi-gWqnCUs0ZJcb3QnbYWOYxOwHM4VW3QbnAyCnitR2TkiJ85fzEsSc_7elckMJiyFnpvi2tF_nzTlklz0ZFS1mz4z4HP5D9PkHdQQmPnY9ZLGRzQR6veGARoZRSSLSgx6nhjJzAPlv8DBG5EaU1nu80LDoS4Mp0Kxo1zk",
    #         "ncToken": "FFFF000000000176722F:1596447519431:0.7135216002337363",
    #         "scene": "nc_login"
    #     }
    # }
    #
    # print(MyRequests(url,method,json=str(json)).text)