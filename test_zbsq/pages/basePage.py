# coding=utf-8

class BasePage(object):
    '''
    基础类，用于所有页面的继承
    '''

    login_url = "http://192.168.33.90:8080/#"

    def __init__(self, driver, base_url=login_url):
        self.base_url = base_url
        self.driver = driver

    def on_page(self):
        return self.driver.current_url == (self.base_url+self.url)

    def _open(self, url):
        url_ = self.base_url + url
        print(url_)
        self.driver.get(url_)
        assert self.driver.current_url == url_, 'Did not land on %s' % url_

    def open(self):
        self._open(self.url)

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def click(self, *loc):
        self.find_element(*loc).click()

    def input(self, text, *loc):
        self.find_element(*loc).send_keys(text)


