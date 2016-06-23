from appium import webdriver
def setUppackage(self):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '4.2'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.tencent.mobileqq'
    desired_caps['appActivity'] = '.activity.SplashActivity'

    # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)