#-*-coding:utf-8-*-
import random
import string
<<<<<<< HEAD

# def getRandChar(n):
#     l = []
#     #sample = '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+=.'
#     sample = random.sample(string.ascii_letters + string.digits, 62)## ��a-zA-Z0-9����ָ������������ַ��� list����
#     sample = sample + list('!@#$%^&*()-+=.')#ԭ�����ϼ���һЩ����Ԫ��
#     for i in range(n):
#         char = random.choice(sample)#��sample��ѡ��һ���ַ�
#         l.append(char)
#     return ''.join(l)  # �����ַ���
#
# if __name__ == '__main__':
#     print(getRandChar(7))
=======
def getRandChar(n):
    l = []
    #sample = '0123456789abcdefghijklmnopqrstuvwxyz!@#$%^&*()-+=.'
    sample = random.sample(string.ascii_letters + string.digits, 62)## ��a-zA-Z0-9����ָ������������ַ��� list����
    sample = sample + list('!@#$%^&*()-+=.')#ԭ�����ϼ���һЩ����Ԫ��
    for i in range(n):
        char = random.choice(sample)#��sample��ѡ��һ���ַ�
        l.append(char)
    return ''.join(l)  # �����ַ���

if __name__ == '__main__':
    print(getRandChar(7))
>>>>>>> 6d085cf (各种蒙圈)




