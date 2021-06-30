#coding=gbk
from email.mime.text import MIMEText
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

subject="python邮件测试"
content=" 大佬，请查收"
user_from="xiwang513926@163.com"
pwd="FZWYJGIQOLCOKQEL"
msg_to=["1379931291@qq.com","190647116@qq.com"]
user_to=','.join(msg_to)                       #收件人多个的情况
filename="D://PycharmProjects/again/pythonunittest/pyResult.html"                       #附件内容
user_Cc="1165216607"
# user_to=("1379931291@qq.com")                #收件人一个的情况


#构造邮件
msg = MIMEMultipart()
msg["Subject"] = subject
msg["From"] = user_from
msg["To"] = user_to
msg["Cc"]= user_Cc

#添加正文
part=MIMEText(content)
msg.attach(part)

#添加附件
with open(filename,'rb') as fp:
    att =MIMEApplication(fp.read(), _subtype="html")
att.add_header('Content-Disposition','attachment',filename="pyResult.html")
msg.attach(att)

class Mail:
    def EMail(self):
        ret=True
        try:
            #指定你要发送邮件的邮箱服务器 ,smtp.qq.com 端口465，smtp.163.com 端口25
            #s=smtplib.SMTP_SSL("smtp.qq.com",465)  #QQ邮箱
            s=smtplib.SMTP("smtp.163.com", 25)   #163邮箱
            s.set_debuglevel(1)
            #登录邮箱
            s.login(user_from,pwd)

            #发送邮件 from to
            s.sendmail(user_from,user_to,msg.as_string())   #加上.as_string()是为了防止被当成垃圾邮件，不加会发不出去

        except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
            raise e
        finally:
            #关闭，所有用到的资源，用完要关闭
            s.quit()

        return ret
if __name__ == '__main__':
    a = Mail().EMail()
    if a:
        print("邮件发送成功")
    else:
        print("邮件发送失败")
