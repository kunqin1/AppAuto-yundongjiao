import time
from Tool import driver

"""
工具类方法
回到首页
秦坤
"""


# 返回到首页
def Click_back():
    time.sleep(5)
    try:
        driver.open.get_driver().find_element_by_android_uiautomator('new UiSelector().text("首页")')
    except:
        driver.open.get_driver().keyevent(4)
        return "False"


def GoHome():
    while Click_back() == "False":
        Click_back()


if __name__ == '__main__':
    GoHome()
