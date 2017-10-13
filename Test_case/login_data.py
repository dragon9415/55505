# coding=utf-8


from selenium import webdriver
import time

def cms_Login(driver):
    u"""用户登录"""
    driver.find_element_by_link_text("亲，请登录").click()
    driver.find_element_by_id("username").send_keys("qiye008")
    driver.find_element_by_id("password").send_keys("123456")
    time.sleep(1)
    driver.find_element_by_xpath("//*[@type='button']").click()  # 点击登录
    time.sleep(1)