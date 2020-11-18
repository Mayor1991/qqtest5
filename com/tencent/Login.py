'''
Created on 2016年5月23日

@author: v_tczhang
'''
import unittest
from time import sleep
from appium import webdriver


def login(self):
    sleep(2)
    el1 = self.driver.find_element_by_android_uiautomator('new UiSelector().description("请输入QQ号码或手机或邮箱")')
    el2 = self.driver.find_element_by_android_uiautomator(
        'new UiSelector().className("android.widget.EditText").index(2)')

    el1.send_keys('XXXXX')
    el2.click()
    sleep(2)
    self.driver.tap([(760, 535), ], 500)
    sleep(1)
    el2.send_keys('XXXXX')
    self.driver.find_element_by_accessibility_id("登录").click()
