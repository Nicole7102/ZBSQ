# coding=utf-8
import unittest
from test_zbsq.test_case.test_loginPage import Test_EnterPage
from test_zbsq.test_case.test_mapsPage import Test_StatusBox
from test_zbsq.public.HTMLTestReportCN import HTMLTestRunner
import time
from test_zbsq.public.send_email import new_report,send_mail

if __name__=="__main__":

    # 选择用例执行
    # testsuit = unittest.TestSuite()
    # testsuit.addTest(Test_EnterPage('test_open'))
    # testsuit.addTest(Test_EnterPage('test_login'))
    # testsuit.addTest(Test_StatusBox('test_quick_repair'))

    # 定义测试用例目录
    test_dir = "./test_zbsq/test_case"
    discover = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py',top_level_dir="D:\pycharm_3\ZBSQ")

    # 生成HTML报告
    test_report = ".\\report"
    now =time.strftime("%Y-%m-%d %H-%M-%S")
    fp = open(test_report+"/"+now+"_report.html", "wb")
    runner = HTMLTestRunner(stream=fp, title="装备视情--测试报告", description="用例执行情况：")
    runner.run(discover)
    fp.close()

    # # 发送报告邮件
    # new_report = new_report(test_report)
    # send_mail(new_report)