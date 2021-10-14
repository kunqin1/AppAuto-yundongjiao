# 点击更多场馆按钮
import time

from Login import denglu
from Tool import driver

"""
工具类方法
首页点击按钮
秦坤
"""


def click_MoreButton(button):
    time.sleep(5)
    denglu.up_Swipe()
    # MoreButton = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_shop")
    try:
        driver.open.get_driver().find_element_by_id(button)
    except:
        denglu.up_Swipe()
    driver.open.get_driver().find_element_by_id(button).click()


def GoHomeTop(button):
    time.sleep(5)
    denglu.down_Swipe()
    try:
        driver.open.get_driver().find_element_by_id(button)
    except:
        denglu.down_Swipe()
