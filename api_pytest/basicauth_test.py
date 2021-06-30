#-*-coding:utf-8-*-
#-*-coding:utf-8-*-
import requests

from requests.auth import HTTPBasicAuth   # 使用基本认证basicauth
username="zusun"
passwd="zusun"
ulr="http://jenkins.bolo.me/job/Bolome-Android-AutoBuild/"

auth=HTTPBasicAuth(username,passwd)
request=requests.get(ulr,auth=auth)
print(request)
print(request.text)