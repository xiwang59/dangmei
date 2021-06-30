# -*-coding:utf-8-*-
from faker import Faker
def RandomGeneration():
    faker={}
    fake = Faker(locale="zh_CN")
    name = fake.name()
    phone = fake.phone_number()
    faker["${name}"]=name
    faker["${phone}"]=phone
    return faker
if __name__ == '__main__':
    print(RandomGeneration())