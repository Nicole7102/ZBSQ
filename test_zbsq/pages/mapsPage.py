# coding=utf-8
from selenium.webdriver.common.by import By
from .basePage import BasePage

import time


class MapsPage(BasePage):
    '''
    装备视情首页模型
    '''
    url = '/maps'

    # 定位器
    quick_repair_btn = (By.CSS_SELECTOR,"div.statusBox>div.status-top>button>span")
    equip_num_click = (By.XPATH, "//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[1]/div/div/div[1]/input")

    equip_num_selectbox = (By.XPATH,"/html/body/div[4]/div/div/ul")
    equip_reTime = (By.XPATH,"//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[4]/div/div[1]/input")
    equip_faCode = (By.XPATH,"//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[5]/div/div[1]/input")
    submit_button = (By.CSS_SELECTOR,".el-button.el-button--primary")
    cancle_button = (By.XPATH,"//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[6]/div/button[2]/span")
    status_fail = (By.XPATH,"/html/body/div[5]/div/p")
    status_success = (By.XPATH,"/html/body/div[4]/div/p")
    fa_error_info = (By.XPATH,"//*[@id='app']/div/div[2]/section/div[6]/div/div[2]/form/div[5]/div/div[2]")

    radar_green = (By.CSS_SELECTOR,".statusBox>div:nth-child(2)>span>cite")
    radar_orange = (By.CSS_SELECTOR,".statusBox>div:nth-child(3)>span>cite")
    radar_red = (By.CSS_SELECTOR,".statusBox>div:nth-child(4)>span>cite")
    close_button = (By.CSS_SELECTOR,"div.el-dialog__header>button")

    # app > div > div.content > section > div.el-dialog__wrapper.quickDialog.dialogTitle > div > div.el-dialog__header > button
    # 点击快速报修按钮
    def click_quick_repair_btn(self):
        self.click(*self.quick_repair_btn)

    # 输入装备批次号
    def input_equipNum(self,text):
        time.sleep(5)
        self.click(*self.equip_num_click)
        list = self.find_element(*self.equip_num_selectbox).find_elements_by_tag_name('li')
        length = len(list)
        for i in range(0, length):
            print(list[i].text)
            if list[i].text == text:
                list[i].click()
                break
            else:
                i = i + 1

    # 输入剩余寿命
    def input_equipReTime(self,reTime):
        self.input(reTime, *self.equip_reTime)

    # 输入故障编码
    def input_faCode(self,faCode):
        self.input(faCode, *self.equip_faCode)

    # 点击提交按钮
    def click_submit_button(self):
        self.click(*self.submit_button)

    # 查看提交状态
    # def status(self):
    #     status_fail = self.find_element(*self.status_fail).get_attribute("textContent")
    #     status_true = self.find_element(*self.status_success).get_attribute("textContent")
    #     if status_info == "提交成功！":
    #         return True
    #     else:
    #         fa_error_info = self.find_element(*self.fa_error_info).get_attribute("textContent")
    #         return fa_error_info

    #  点击取消报修按钮
    def click_cancle_button(self):
        self.click(*self.cancle_button)

    def view_radar_green_list(self):
        time.sleep(3)
        self.click(*self.radar_green)

    def view_radar_orange_list(self):
        time.sleep(3)
        self.click(*self.radar_orange)

    def view_radar_red_list(self):
        time.sleep(3)
        self.click(*self.radar_red)

    def click_close_button(self):
        self.click(*self.close_button)
