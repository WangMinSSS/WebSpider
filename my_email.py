from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

'''
示例用法
mail必须为列表，即使只有一个收件人
mail = ['969821285@qq.com', 'wangmin.min@qq.com']
m_SendEmail('hello,wangmin', 'plain', *mail) # plain可替换为html

'''
'''
f = open('moive.txt', 'r')
t = f.readlines()
t = '\n'.join(t)
f.close()
'''

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))



def m_SendEmail(text, texttype='plain', *to_addr):      # texttype纯文本、HTML分别为plain,html
    # 发送邮箱信息
    from_addr = '13174147700@163.com'
    password = 'wangmin1993'
    smtp_server = 'smtp.163.com'

    msg = MIMEText(text, texttype, 'utf-8')
    # 发送邮箱地址
    msg['From'] = _format_addr('易水晓寒 <%s>' % from_addr)
    # 收件箱地址
    msg['To'] = ",".join(to_addr)   # 群发需要
    # 主题
    msg['Subject'] = Header('来自晓寒的推送~', 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465) # 阿里云不支持25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, to_addr, msg.as_string())
    server.quit()







