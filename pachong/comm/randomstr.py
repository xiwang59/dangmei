#-*-coding:utf-8-*-
import random
import string
<<<<<<< HEAD

# def getRandChar(n):
#     l = []
#     #sample = '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+=.'
#     sample = random.sample(string.ascii_letters + string.digits, 62)## 从a-zA-Z0-9生成指定数量的随机字符： list类型
#     sample = sample + list('!@#$%^&*()-+=.')#原基础上加入一些符号元素
#     for i in range(n):
#         char = random.choice(sample)#从sample中选择一个字符
#         l.append(char)
#     return ''.join(l)  # 返回字符串
#
# if __name__ == '__main__':
#     print(getRandChar(7))
=======
def getRandChar(n):
    l = []
    #sample = '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+=.'
    sample = random.sample(string.ascii_letters + string.digits, 62)## 从a-zA-Z0-9生成指定数量的随机字符： list类型
    sample = sample + list('!@#$%^&*()-+=.')#原基础上加入一些符号元素
    for i in range(n):
        char = random.choice(sample)#从sample中选择一个字符
        l.append(char)
    return ''.join(l)  # 返回字符串

if __name__ == '__main__':
    print(getRandChar(7))
>>>>>>> 6d085cf (鍚勭钂欏湀)




