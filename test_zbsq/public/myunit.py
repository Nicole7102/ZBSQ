# coding=utf-8
import unittest
from ..config.conf import driver


def setUpModule():
    pass


def tearDownModule():
    pass


class MyUnit(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @ classmethod
    def setUpClass(cls):
        cls.driver = driver()
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @ classmethod
    def tearDownClass(cls):
        cls.driver.quit()
