import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formatdate
import os


# 发送邮件
def send_mail(file_new):
    sender = "jianling.guo@isinonet.com"
    receiver = "jianling.guo@isinonet.com"
    # acc = "2205131769@qq.com，1433027648@qq.com"
    pwd = "ABCabc123"

    server = smtplib.SMTP()
    server.connect("smtp.isinonet.com")
    server.login(sender, pwd)
    # 构造MIMEMultipart对象做为根容器
    main_msg = MIMEMultipart()
    text_msg = MIMEText("测试报告见附件")
    main_msg.attach(text_msg)
    #  构造MIMEText对象做为邮件显示内容并附加到根容器
    contype = "application/octet-stream"
    maintype,subtype = contype.split('/',1)
    # 读入文件内容并格式化
    data = open(file_new,"rb")
    file_msg = MIMEBase(maintype,subtype)
    file_msg.set_payload(data.read())
    data.close()
    encoders.encode_base64(file_msg)
    # 设置附件头
    file_name = os.path.basename(file_new)
    # 解决中文附件名乱码问题
    file_msg.add_header('Content-Disposition', 'attachment', filename=('gbk','', file_name))
    main_msg.attach(file_msg)
    # 设置根容器属性
    main_msg['From'] = sender
    main_msg['To'] = receiver
    # main_msg['cc'] = acc
    main_msg['Subject'] = Header("装备视情自动化测试报告","utf-8")
    main_msg['Date'] = formatdate()
    # 得到格式化后的完整文本
    fullText = main_msg.as_string()
    # 用smtp发送邮件
    try:
        server.sendmail(sender,receiver,fullText)
    finally:
        server.quit()


# 查找测试报告目录中最新报告
def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn:os.path.getmtime(testreport+"\\"+fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new


# if __name__=="__main__":
#     test_report = "D:\\pycharm_3\\ZBSQ\\report"
#     new_report = new_report(test_report)
#     send_mail(new_report)  # 发送测试报告