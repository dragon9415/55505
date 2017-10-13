# C:\Python36\python.exe
# -*- coding:utf-8 -*-
#coding=utf-8
# coding=utf-8
from selenium import webdriver
from datetime import datetime
import unittest, time, re
from login_data import cms_Login
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchAttributeException
import HTMLTestRunner


class CMS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.base_url = "http://10.188.5.129:9091/jyCms"
        self.verificationErrors = []
        self.accept_next_alert = True


    def test_cms_Login(self):
        u"""登录密码错误"""
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_link_text("亲，请登录").click()
        driver.find_element_by_id("username").send_keys("qiye008")
        driver.find_element_by_id("password").send_keys("1234567")
        time.sleep(1)
        driver.find_element_by_xpath("//*[@type='button']").click()  # 点击登录
        time.sleep(3)
        try:
            driver.find_element_by_id("pra")  # 获取异常信息的元素
        except:
            driver.get_screenshot_as_file(u"D:/UI_Test/error_png/%s登录.png" % datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-3])  # 当获取不到上面的元素时就会截图当前界面，如果能获取到就不会截图
        self.driver.close()

    def test_cms_personal(self):
        u"""个人中心"""
        self.driver.get(self.base_url + '/')
        cms_Login(self.driver)
        time.sleep(2)
        self.driver.find_element_by_link_text("个人中心").click()
        time.sleep(2)
        self.driver.find_element_by_link_text("个人信息").click()
        time.sleep(2)
        js = "window.scrollTo(0,document.body.scrollHeight)"  # 滚动条滚到底部
        self.driver.execute_script(js)
        time.sleep(2)
        try:
            self.driver.find_element_by_value("企业008")
        except Exception as e:
            self.driver.get_screenshot_as_file(u"D:/UI_Test/error_png/%s.png" % datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-3])
        time.sleep(2)
        self.driver.find_element_by_link_text("资料查看").click()
        try:
            self.driver.find_element_by_style("color: green;")
        except Exception as e:
            self.driver.get_screenshot_as_file(u"D:/UI_Test/error_png/%s.png" % datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-3])

        time.sleep(2)
        self.driver.find_element_by_link_text("优惠信息").click()
        try:
            self.driver.find_element_by_style("0.0%")
        except:
            self.driver.get_screenshot_as_file(u"D:/UI_Test/error_png/%s.png" % datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-3])
        time.sleep(2)
        self.driver.find_element_by_link_text('订单管理').click()
        time.sleep(2)
        js = "window.scrollTo(0,document.body.scrollHeight)"  # 滚动拉到页面顶部
        self.driver.execute_script(js)
        time.sleep(2)
        self.driver.find_element_by_link_text('尾页').click()
        time.sleep(2)
        self.driver.find_element_by_link_text('个人返利金').click()
        js = "window.scrollTo(500,document.body.scrollHeight)"  # 滚动拉到页面中部
        self.driver.execute_script(js)
        time.sleep(3)
        self.driver.find_element_by_link_text('评价商品').click()
        time.sleep(3)
        self.driver.close()

    def test_cms_set(self):
        u"""点击分类栏"""
        driver = self.driver
        driver.get(self.base_url + '/')
        time.sleep(2)
        driver.find_element_by_link_text("晾衣机").click()
        time.sleep(2)
        driver.close()


    def test_cms_Search(self):
        u"""搜索及商品详情"""
        driver = self.driver
        driver.get(self.base_url + '/')
        time.sleep(1)
        driver.find_element_by_id("pra").send_keys("晾衣架")     #输入搜索商品名称
        time.sleep(1)
        driver.find_element_by_id('ai-topsearch').click()           #点击搜索商品
        time.sleep(2)
        driver.find_elements_by_css_selector("[class='i-pic limit']").pop(1).click()  # 获取页面第二个图位的商品连接
        time.sleep(2)
        js = "window.scrollTo(500,document.body.scrollHeight)"    #滚动拉到页面中部
        driver.execute_script(js)
        time.sleep(2)
        driver.find_elements_by_class_name("index-needs-dt-txt").pop(1).click()   #查看商品评价
        time.sleep(2)
        driver.find_elements_by_class_name("index-needs-dt-txt").pop(0).click()   #切换回商品详情
        time.sleep(2)
        driver.close()


    def test_cms_Buy(self):
        u"""立即购买"""
        driver = self.driver
        driver.get(self.base_url + '/')
        cms_Login(self.driver)
        time.sleep(1)
        driver.find_elements_by_css_selector("[class='list']").pop(0).click()  # 选择首页的商品
        time.sleep(1)
        driver.find_element_by_id("LikBuy").click()        #点击立即购买
        time.sleep(2)
        driver.find_element_by_id("79").click()  # 选择立即收货地址
        time.sleep(2)
        driver.find_element_by_css_selector("[class='pay taobao']").click()  # 选择支付方式
        time.sleep(2)
        driver.find_element_by_id("message").send_keys("123456")  # 输入客户留言
        time.sleep(2)
        driver.find_element_by_id("J_Go").click()  # 提交订单
        time.sleep(2)
        driver.close()


    def test_cms_Shopping(self):
        u"""加入购物车"""
        driver = self.driver
        driver.get(self.base_url + '/')
        cms_Login(self.driver)
        time.sleep(1)
        driver.find_elements_by_css_selector("[class='list']").pop(0).click() #
        time.sleep(1)
        driver.find_element_by_id("LikBasket").click()
        time.sleep(2)
        driver.close()

    def test_cms_Cart(self):
        u"""进入购物车进行结算"""
        driver = self.driver
        driver.get(self.base_url + '/')
        cms_Login(self.driver)
        time.sleep(1)
        driver.find_element_by_id("mc-menu-hd").click()  #进入购物车
        time.sleep(2)
        driver.find_elements_by_css_selector("[onclick='counts()']").pop(0).click()  # 选择需要结算的货物
        driver.find_element_by_id("J_Go").click()  #点击结算
        driver.find_element_by_id("79").click()  # 选择立即收货地址
        driver.find_element_by_css_selector("[class='pay taobao']").click()  # 选择支付方式
        driver.find_element_by_id("message").send_keys(u"hansilus")  # 输入客户留言
        time.sleep(3)
        js = "window.scrollTo(0,document.body.scrollHeight)"   #滚动条滚到底部
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_id("J_Go").click()        #提交订单(
        time.sleep(3)
        driver.close()


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
'''