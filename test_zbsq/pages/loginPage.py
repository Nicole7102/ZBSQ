# coding=utf-8
from selenium.webdriver.common.by import By
from .basePage import BasePage


class LoginPage(BasePage):
    '''
    装备视情登录页面模型
    '''
    url = '/login'
    # 定位器(组装成tuple或list,然后通过func(*（参数）))传入
    enter_btn = (By.CLASS_NAME, 'btnEnter')

    # 操作
    def click_enter_btn(self):
        # 点击进入按钮
        self.click(*self.enter_btn)
