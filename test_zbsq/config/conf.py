# conding =utf-8
from selenium import webdriver


def browser():
    driver = webdriver.Firefox()
    return driver
