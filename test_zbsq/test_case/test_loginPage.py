# coding=utf-8
from ..pages.loginPage import LoginPage
from ..public import myunit


# 测试登录页
class Test_EnterPage(myunit.MyUnit):
    '''测试登录页'''

    def test_a_open(self):
        '''打开测试网址'''
        login_page = LoginPage(self.driver)
        login_page.open()
        title = self.driver.title
        self.assertEqual(title,"装备智能保障决策支持系统",msg="网址打开失败!")

    def test_b_login(self):
        '''点击“进入”按钮进入首页'''
        login_page = LoginPage(self.driver)
        login_page.open()
        login_page.click_enter_btn()
        current_url = self.driver.current_url
        self.assertEqual(current_url,"http://192.168.33.90:8080/#/maps",msg="跳转到首页失败！")
