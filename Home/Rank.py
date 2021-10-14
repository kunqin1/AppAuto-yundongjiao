import time
import unittest
from Tool import driver
from Login import denglu

"""
排行榜测试
秦坤
"""


# 排行榜滑动查看
def Swipe():
    try:
        denglu.up_Swipe()
        time.sleep(3)
        denglu.down_Swipe()
    except:
        print("滑动失败")


# 卡路里、马拉松、荣耀每个排行榜数据滑动
def switch():
    try:
        driver.open.get_driver().find_element_by_android_uiautomator('new UiSelector().text("日排行榜")').click()
        Swipe()
    except:
        pass
        driver.open.get_driver().find_element_by_android_uiautomator('new UiSelector().text("周排行榜")').click()
    Swipe()
    driver.open.get_driver().find_element_by_android_uiautomator('new UiSelector().text("月排行榜")').click()
    Swipe()


# 点击首页排行榜
def click_record():
    time.sleep(2)
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/record").click()


# # 场馆排名
# def rank_click():
#     # click_record()
#     try:
#         driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/calorie").click()
#         switch()
#         driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/marathon").click()
#         switch()
#         driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/glory").click()
#         switch()
#         result = "True"
#     except:
#         result = "False"
#     return result


# 市排名
def rank_stadium():
    click_record()
    try:
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/calorie").click()
        switch()
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/marathon").click()
        switch()
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/glory").click()
        switch()
        result = "True"
    except:
        result = "False"
    return result


def rank_city():
    click_record()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/city").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/img_y").click()
    try:
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/calorie").click()
        switch()
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/marathon").click()
        switch()
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/glory").click()
        switch()
        result = "True"
    except:
        result = "False"
    return result


class Rank(unittest.TestCase):

    # 城市排行
    def test_case01(self):
        result = rank_city()
        self.assertTrue(result)
        time.sleep(1)
        driver.open.get_driver().keyevent(4)

    # 社区排行
    def test_case02(self):
        result = rank_stadium()
        self.assertTrue(result)
        time.sleep(1)
        driver.open.get_driver().keyevent(4)


if __name__ == '__main__':
    unittest.main()
    # switch()
    # click_record()
