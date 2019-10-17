'''
Created on 2015年9月18日

@author: v_tczhang
'''

import os
import unittest
from appium import webdriver
from time import sleep
import Login
from appium.webdriver.common.touch_action import TouchAction
import sys
import time
import HTMLTestRunner
from unittest import runner
from warnings import catch_warnings
from test.testcase.Login import login


class ContactsAndroidTests(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps['appActivity'] = '.activity.SplashActivity'
        desired_caps['unicodeKeyboard'] = 'true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    #     def login(self):
    #
    #         sleep(2)
    #         el1 = self.driver.find_element_by_android_uiautomator('new UiSelector().description("请输入QQ号码或手机或邮箱")')
    #         el2 = self.driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.EditText").index(2)')
    #
    #         el1.send_keys('x')
    #         el2.click()
    #         sleep(2)
    #         self.driver.tap([(760, 535),], 500)
    #         sleep(1)
    #         el2.send_keys('x')
    #         self.driver.find_element_by_accessibility_id("登录").click()

    def test_add_load(self):
        """QQ登录测试"""
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']

        Login.login(self)
        sleep(4)
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("帐户及设置")').click()
        sleep(1)
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("设置")').click()
        sleep(2)
        self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "帐号管理")]').click()
        self.driver.swipe(width / 2, height / 2, width / 2, height / 4, 1000)
        self.driver.find_element_by_name("退出当前帐号").click()
        self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "确认退出")]').click()

        try:

            sleep(2)
            self.driver.swipe(width / 2, height / 2, 114, height / 2, 1000)
            sleep(2)
        except Exception as e:
            print(e)

    def tearDown(self):
        self.driver.quit()

        # width = self.driver.get_window_size()['width']
        # height = self.driver.get_window_size()['height']
        # sleep(4)
        # self.driver.swipe(width/2, 600, width/7, 600, 1000)
        # sleep(4)
        # self.driver.swipe(500, 600, 500, 400, 1000)
        # sleep(4)


if __name__ == '__main__':
    # suite = unittest.TestLoader().loadTestsFromTestCase(ContactsAndroidTests)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()






