from appium import webdriver
"""
封装driver
秦坤
"""


class OpenApp:
    def __init__(self):
        desired_caps = {
            # 平台类型
            "platformName": "Android",
            # 平台版本号
            "platformVersion": "9",
            # 设备名称
            "deviceName": "INE_AL00 device:HWINE",
            # "deviceName": "PACM00",
            # app 包名
            "appPackage": "com.yundongjiao.lepao",
            # app 入口 acitivity
            "appActivity": "com.yundongjiao.lepao.Activity.module.Activity.SplashScreenActivity",
            "automationName": "uiautomator1",
            "noReset": True,
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def get_driver(self):
        return self.driver


open = OpenApp()
