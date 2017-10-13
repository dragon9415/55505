# C:\Python36\python.exe
# -*- coding:utf-8 -*-
# coding=utf-8
import unittest
# 这里需要导入测试文件
import cms
import HTMLTestRunner

testunit = unittest.TestSuite()   # 定义一个单元测试容器
#将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(cms.CMS))  # cms.CMS中的为用例所在的.py文件的名称，CMS为测试用例集的名称
# 定义个报告存放路径，支持相对路径。
filename = 'D:\\UI_Test\\Test_Presentation\\result.html'
fp = open(filename, 'wb')
#runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='Test Report',description=u'Result:')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Report_title', description='Report_description')

# 执行测试用例
runner.run(testunit)
