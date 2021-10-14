import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

from Tool import driver
from Login import denglu
from Tool import element


def test():
    import json
    Dict = {"name": "tom"}
    DATA = json.load(Dict)
    print(DATA)


if __name__ == '__main__':
    test()
