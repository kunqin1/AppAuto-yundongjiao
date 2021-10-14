import json
import time
from telnetlib import EC
from selenium.webdriver.support.wait import WebDriverWait
from Tool import handjson
from Tool.driver1 import appium_desired

"""
封装元素定位方法
"""


class Element:

    def __init__(self):
        self.driver = appium_desired()

    def find_element(self, locator):
        if not isinstance(locator, dict):
            # 比如:{"name": "输入账号", "by": "id", "value": "xxx"}
            print("请传入字典格式的定位参数")
        # 通过id定位
        if locator.get("type") == "id":
            value = data.get("value")
            element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_id(value))
        # 通过Android定位
        elif locator.get("type") == "android":
            value = data.get("value")
            element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_android_uiautomator(value))
        # 通过classname定位
        elif locator.get("type") == 'className':
            value = data.get("value")
            element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_class_name(value))
        # 通过xpath定位
        elif locator.get("type") == "xpath":
            value = data.get("value")
            # _loc = ("xpath", value)
            element = WebDriverWait(self.driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(value))
        else:
            # 使用list定位
            # types = json.load(data.get("type"))
            # loc = (types, data.get("value"))
            # print(loc)
            loc = (data["type"], data["value"])
            element = WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_elements_located(loc))
        return element

    # 截图
    def get_screen(self, path):
        self.driver.get_screenshot_as_file(path)

    def click(self, locator):
        """点击元素"""
        el = self.find_element(locator)
        el.click()

    def send_text(self, locator, text):
        """发送文本"""
        el = self.find_element(locator)
        el.send_keys(text)


element = Element()

if __name__ == '__main__':
    time.sleep(2)
    data = handjson.read_json("rank.json", "查看排行榜")
    data1 = handjson.read_json("rank.json", "周排行榜")
    data3 = handjson.read_json("rank.json", "当前城市1")
    element.click(data)
    # element.click(data)
    # element.click(data1)
    # element.click(data3)
