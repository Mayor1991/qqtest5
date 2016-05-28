"""
Created on 2016年5月24日

@author: v_tczhang
"""
import unittest
from appium import webdriver
from time import sleep


class Test(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps['appActivity'] = '.activity.SplashActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_Dianzan(self):

        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        Number = {"2599999997": "vtczhang", "2599999990": "987654321"}
        for key in Number.keys():
            i = 10
            sleep(1)
            el1 = self.driver.find_element_by_android_uiautomator('new UiSelector().description("请输入QQ号码或手机或邮箱")')
            el2 = self.driver.find_element_by_android_uiautomator(
                'new UiSelector().className("android.widget.EditText").index(2)')

            el1.send_keys(key)
            el2.click()
            sleep(1)
            self.driver.tap([(760, 535), ], 500)
            sleep(1)
            el2.send_keys(Number[key])
            self.driver.find_element_by_accessibility_id("登录").click()
            sleep(1)
            self.driver.tap([(668, 88)], 500)
            sleep(1)

            self.driver.find_element_by_name("搜索").click()
            sleep(1)
            self.driver.find_element_by_name("搜索").send_keys("594552867")
            #             el4.click()
            self.driver.find_element_by_name("(594552867)").click()
            sleep(1)
            self.driver.find_element_by_android_uiautomator('new UiSelector().description("聊天设置")').click()
            self.driver.tap([(320, 240)], 500)
            sleep(2)
            while (i):
                el3 = self.driver.find_elements_by_class_name("android.view.View")
                el3[1].click()
                i = i - 1
            self.driver.find_element_by_name("返回").click()
            self.driver.find_element_by_name("返回").click()
            self.driver.find_element_by_name("返回").click()
            self.driver.find_element_by_android_uiautomator('new UiSelector().description("帐户及设置")').click()
            self.driver.find_element_by_android_uiautomator('new UiSelector().description("设置")').click()
            self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "帐号管理")]').click()
            self.driver.swipe(width / 2, height / 2, width / 2, height / 4, 1000)
            sleep(2)
            self.driver.find_element_by_name("退出当前帐号").click()
            self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "确认退出")]').click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()