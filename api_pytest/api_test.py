#-*-coding:utf-8-*-
import requests
from again.api_request.common.read_data import ReadData

class ApiTest(ReadData):

    def Api_test(self):
        try:
            a=self.Read()
            for i in range(len(a)):
                # print(a[i])
                if a[i]["method"] == "get":
                    params=a[i]["request_data"]
                    # print(params)
                    response = requests.get(a[i]["url"],params).text
                else:
                    response = requests.get(a[i]["url"], a[i]["request_data"]).text

                assert response ==a[i]["expected_data"]
                print(response)
        except Exception as e:
            raise e


if __name__ == '__main__':
    p="D:/PycharmProjects/again/api_request/data.xlsx"
    s="用例"
    a=ApiTest(p,s).Api_test()

