# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import NoSuchElementException


def select_click(list,text):
    length = len(list)
    for i in range(0, length):
        print(list[i].text)
        if list[i].text == text:
            list[i].click()
            break
        else:
            i = i + 1


if __name__=="__main__":
    driver = webdriver.Chrome()
    driver.get("http://192.168.33.90:8080/#/maps")
    time.sleep(3)
    driver.find_element_by_css_selector(".statusBox>div:nth-child(2)>span>cite").click()
    driver.find_element_by_css_selector("#app>div> div.content > section > div.el-dialog__wrapper.quickDialog.dialogTitle > div > div > button > i").click()
    # driver.find_element_by_css_selector("div.statusBox>div.status-top>button>span").click()  # 点击报修按钮
    # time.sleep(5)
    # click_driver = driver.find_element_by_xpath(
    #     "//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[1]/div/div/div[1]").click()  # 点装备批次号
    #
    # list = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/ul").find_elements_by_tag_name('li')
    # text = "151101010"
    # select_click(list,text)
    # driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[4]/div/div[1]/input").send_keys("1") # 填剩余寿命
    # driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[5]/div/div[1]/input").send_keys("111111") #填故障编码
    # # driver.find_element_by_css_selector(".el-button.el-button--primary").click() # 提交
    # driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[6]/div/button[2]/span").click()
    # driver.find_element_by_css_selector(".statusBox>div:nth-child(2)>span").click()


    # 获取是否提交成功
    #fail = driver.find_element_by_xpath("/html/body/div[5]/div/p").get_attribute("textContent")

    # text = driver.find_element_by_class_name("el-message__group").text
    # print(text)

    # 获取故障码提示语
    #error_info = driver.find_element_by_xpath("//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[5]/div/div[2]").get_attribute("textContent")
    #print(error_info)
