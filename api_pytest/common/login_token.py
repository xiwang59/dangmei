#-*-coding:utf-8-*-
import requests
from api_pytest.common.myRequest import MyRequests
url = "https://api-admin-dm-stage.bolome.com/login"
method = "post"
json = {
    "signId": "测试竹笋",
    "password": "QAZwsx123",
    "loginType": 0,
    "captcha": {
        "cSessionId": "0152JIZgtMjy7iQLwB8JakWWlj_CejnEFyufXFVghoZTydbpmRSzeiZ903hWOuOJDAKHRusUhtFuMRhS68u_R5J9ILksAsi_jOiYiArUQCcwdB868MvOl8tcUwL1pP4CneJFs0kqDa_QKAjr8GlKlBF67UDjc9t1R6WUgzwqsFszdmWh1ixrgaaySPuOZpAaU-nALcbseNIzyI6tVyQ-jUIA",
        "sig": "05a1C7nT4bR5hcbZlAujcdyTIjGz0Egt91iX1IO3BzqF7hV0jTbGeQfzcZH0xvdWXr5J84kcgH9c9zp1yfKofbpYPJZNCILq88zK8kwvlUzftiGp4-RSlo2wwzH2kqN58cClOZ0tlsrSyFEh-uBHcO3U8hB6j_6iOHPukehFkMLvoOCzXwBEkJKhq2dgVGQlVWmYjNqZ2POxkOytMuqObDXsuQ2awYSBPbiPoOMehcPdiJ5qhY_MrcYaNOV0HVaB0v01Ar3YahFiLVfGqfBS59zuSGQDFnJXQXe3cTNWNQ2ISK5e8oi-qqAULm58huKu0pFxr74Oi-gWqnCUs0ZJcb3QnbYWOYxOwHM4VW3QbnAyCnitR2TkiJ85fzEsSc_7elckMJiyFnpvi2tF_nzTlklz0ZFS1mz4z4HP5D9PkHdQQmPnY9ZLGRzQR6veGARoZRSSLSgx6nhjJzAPlv8DBG5EaU1nu80LDoS4Mp0Kxo1zk",
        "ncToken": "FFFF000000000176722F:1596447519431:0.7135216002337363",
        "scene": "nc_login"
    }
}
return_result=MyRequests(url,method,json=str(json)).text
# print(return_result)
return_result=eval(return_result)
# print(return_result)
token="Bearer "+return_result["data"]["token"]
