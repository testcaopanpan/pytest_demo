# _*_ coding:utf-8 _*_
import smtplib
from email.header import Header
from email.mime.text import MIMEText

#登录邮箱服务器
def send_email():
    #配置邮箱服务器
    email_user = smtplib.SMTP_SSL("smtp.qq.com",465)
    #通过邮箱、三方使用授权码进行登录
    email_user.login("957406615@qq.com","amawgzfmhpzabbbe")
#用于邮箱配置日志打印
#email_user.set_debuglevel()

#配置邮件正文内容
    msg = "本次测试已完成，请登录查看测试报告"

#配置邮件信息
    msg = MIMEText(msg,'plain','utf-8')    #配置邮件正文
    msg['from'] = Header("曹盼盼","utf-8")
    msg['to'] = Header("各位同事","utf-8")
    msg['Subject'] = Header("自动化执行报告","utf-8")

    reserve_email =['2389726116@qq.com','957406615@qq.com']
    for email in reserve_email:
        email_user.sendmail("957406615@qq.com",email,msg.as_string())