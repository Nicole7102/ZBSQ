# coding=utf-8
from ..public import myunit
from ..pages.mapsPage import MapsPage


# 测试快速报修状态面板
class Test_StatusBox(myunit.MyUnit):
    '''测试雷达报修面板'''

    # 输入的值
    equipNum = "151101010"  # 选择的装备批次号,默认海南地区
    reTime = "3"  # 剩余寿命设置3
    faCode_orange = "111111"  # 预警故障编号
    faCode_red = "000000"  # 紧急故障编号

    def test_a_quick_repair(self):
        '''报修故障预警雷达'''
        qr = MapsPage(self.driver)
        qr.open()
        qr.click_quick_repair_btn()
        qr.input_equipNum(self.equipNum)
        qr.input_equipReTime(self.reTime)
        qr.input_faCode(self.faCode_orange)
        qr.click_submit_button()
        # self.assertTrue(qr.status(),msg=qr.status())

    def test_b_quick_repair_red(self):
        '''报修紧急故障的雷达'''
        qr = MapsPage(self.driver)
        qr.open()
        qr.click_quick_repair_btn()
        qr.input_equipNum(self.equipNum)
        qr.input_equipReTime(self.reTime)
        qr.input_faCode(self.faCode_red)
        qr.click_submit_button()

    def test_c_cancle_repair(self):
        '''取消报修'''
        qr = MapsPage(self.driver)
        qr.open()
        qr.click_quick_repair_btn()
        qr.input_equipNum(self.equipNum)
        qr.input_equipReTime(self.reTime)
        qr.input_faCode(self.faCode_red)
        qr.click_cancle_button()

    def test_d_view_radar_green_info(self):
        '''查看健康雷达信息'''
        qr = MapsPage(self.driver)
        qr.open()
        qr.view_radar_green_list()
        qr.click_close_button()

    def test_e_view_radar_orange_info(self):
        '''查看预警雷达信息'''
        qr = MapsPage(self.driver)
        qr.open()
        qr.view_radar_orange_list()
        qr.click_close_button()

    def test_f_view_radar_red_info(self):
        '''查看紧急雷达信息'''
        qr = MapsPage(self.driver)
        qr.open()
        qr.view_radar_red_list()
        qr.click_close_button()
