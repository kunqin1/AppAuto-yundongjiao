import time
import unittest

from appium import webdriver


class Study_test(unittest.TestCase):

    def setUp(self):
        desired_caps = {
            # 平台类型
            "platformName": "Android",
            # 平台版本号
            "platformVersion": "10",
            # 设备名称
            "deviceName": "PACM00",
            # app 包名
            "appPackage": "com.yundongjiao.lepao",
            # app 入口 acitivity
            "appActivity": "com.yundongjiao.lepao.Activity.module.Activity.SplashScreenActivity",
            "automationName": "uiautomator1",
            "noReset": False,
        }

        # 连接Appium server。前提：appium desktop要启动。有监听端口。
        # 将desired_caps发送给appium server。打开app
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(5)

        # x = 0
        # while x < 1:
        #     self.get_size()
        #     x = x + 1
        # 立即开启按钮
        try:
            # 隐私协议同意按钮
            self.driver.find_element_by_id('com.yundongjiao.lepao:id/tv_agree').click()
            # 跳过按钮
            SkipButton = self.driver.find_element_by_id('com.yundongjiao.lepao:id/tg')
            SkipButton.click()
            StartButton = self.driver.find_element_by_id('com.yundongjiao.lepao:id/btn')
            StartButton.click()
        except:
            pass

    def test_01(self):
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")')
