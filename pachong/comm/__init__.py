#coding=gbk
from email.mime.text import MIMEText
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

subject="python�ʼ�����"
content=" ���У������"
user_from="xiwang513926@163.com"
pwd="FZWYJGIQOLCOKQEL"
msg_to=["1379931291@qq.com","190647116@qq.com"]
user_to=','.join(msg_to)                       #�ռ��˶�������
filename="D://PycharmProjects/again/pythonunittest/pyResult.html"                       #��������
user_Cc="1165216607"
# user_to=("1379931291@qq.com")                #�ռ���һ�������


#�����ʼ�
msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = user_from
msg["To"] = user_to
msg["Cc"]= user_Cc

#�������
part=MIMEText(content)
msg.attach(part)

#��Ӹ���
with open(filename,'rb') as fp:
    att =MIMEApplication(fp.read(), _subtype="html")
att.add_header('Content-Disposition','attachment',filename="pyResult.html")
msg.attach(att)

class Mail:
    def EMail(self):
        ret=True
        try:
            #ָ����Ҫ�����ʼ������������ ,smtp.qq.com �˿�465��smtp.163.com �˿�25
            #s=smtplib.SMTP_SSL("smtp.qq.com",465)  #QQ����
            s=smtplib.SMTP("smtp.163.com", 25)   #163����
            s.set_debuglevel(1)
            #��¼����
            s.login(user_from,pwd)

            #�����ʼ� from to
            s.sendmail(user_from,user_to,msg.as_string())   #����.as_string()��Ϊ�˷�ֹ�����������ʼ������ӻᷢ����ȥ

        except Exception as e:  # ��� try �е����û��ִ�У����ִ������� ret=False
            raise e
        finally:
            #�رգ������õ�����Դ������Ҫ�ر�
            s.quit()

        return ret
if __name__ == '__main__':
    a = Mail().EMail()
    if a:
        print("�ʼ����ͳɹ�")
    else:
        print("�ʼ�����ʧ��")
