'''
Created on 2016年4月13日

@author: v_tczhang
'''
import unittest
from appium import webdriver
import sys, os
from time import sleep
import Login
import qqsetUp

class ExpressMarkertTest(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.2'
        desired_caps['deviceName'] = 'Android Emulator'
        desired_caps['appPackage'] = 'com.tencent.mobileqq'
        desired_caps['appActivity'] = '.activity.SplashActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    # 从消息列表进入AIO聊天界面 》点击表情按钮>点击大表情>点击添加表情>验证进入表情商城

    def test_bqmark(self):
        '''验证进入表情商城'''
        #         sleep(4)
        #         selector = 'new UiSelector().className("android.widget.TabWidget").childSelector(new UiSelector().className("android.widget.RelativeLayout").index(0))'
        #         el = self.driver.find_element_by_android_uiautomator(selector)
        #         el.click()
        #
        #
        #         try:
        #             el1 = self.driver.find_element_by_name("搜索")
        #             self.assertEqual("搜索", el1.text)
        #
        #         except Exception as e:
        #             print(e)
        #         ca = ContactsAndroidTests()

        Login.login(self)
        sleep(1)

        self.driver.find_element_by_name("搜索").click()
        self.driver.find_element_by_name("搜索").send_keys("2599999997")
        self.driver.find_element_by_name("我的昵称很长足够用一百年").click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("表情")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().description("表情商城入口")').click()
        try:
            el = self.driver.find_element_by_name("表情")
            self.assertEqual(el.text, "表情")
        except Exception as e:
            print(e)
        self.driver.find_element_by_name("关闭").click()

    def tearDown(self):
        self.driver.quit()

# class ExpressManagerTest(unittest.TestCase):
#     def setUp(self):
#         qqsetUp.setUp(self)
#
#     # 从消息列表进入AIO聊天界面 》点击表情按钮>点击大表情>点击添加表情>点击我的表情>验证表情管理
#     def test_Manager(self):
#
#
#
#     def tearDown(self):
#         self.driver.quit()


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    # bqmark.run()
    unittest.main()