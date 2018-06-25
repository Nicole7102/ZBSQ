# conding =utf-8
from selenium import webdriver
from selenium.webdriver import Remote


def driver():
    # 定义主机与浏览器
    # list = {'http://127.0.0.1:4444/wd/hub': 'chrome',
    #         'http://192.168.33.90:5555/wd/hub': 'chrome'}
    #
    # for host, browser in list.items():
    #     driver = Remote(command_executor=host,
    #                     desired_capabilities={'platform': 'ANY',
    #                                           'browserName': browser,
    #                                           'version': '',
    #                                           'javascriptEnabled': True
    #                                           }
    #                     )
    #     return driver

    driver = webdriver.Chrome()
    return driver
