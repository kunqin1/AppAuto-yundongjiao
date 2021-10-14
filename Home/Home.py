import time
import unittest
import parameterized
import logging
import logging.config
from Tool.driver import open
from Tool import moreButton

"""
首页点击事件测试
秦坤
"""

logging.config.fileConfig("../Tool/log.conf")
logging = logging.getLogger("infoLogger")


# 验证首页点击跳转事件
def Advertising(Button):
    moreButton.GoHomeTop(Button)
    # start.login("18782048139", "123456")
    open.get_driver().find_element_by_id(Button).click()
    # open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").click()
    try:
        open.get_driver().find_element_by_android_uiautomator("累计消耗")
        return False
    except:
        return True


# 验证点击查看全部按钮
def All(Button):
    moreButton.click_MoreButton(Button)
    try:
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/e")
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/back ").click()
        result = True
    except:
        result = False
    return result


def goal():
    # start.login("18782048139", "123456")
    time.sleep(2)
    open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/hom_plan").click()
    try:
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/ok")
        result = True
    except:
        result = False
    return result


class Home(unittest.TestCase):
    def setUp(self):
        open.get_driver()

    # # 验证banner
    # def test_banner(self):
    #     result = banner()
    #     self.assertTrue(result)

    # 验证广告页
    @parameterized.parameterized.expand(
        [
            "com.yundongjiao.lepao:id/home_img",
            "com.yundongjiao.lepao:id/record",
            "com.yundongjiao.lepao:id/day",  # f
            'com.yundongjiao.lepao:id/img',
            'com.yundongjiao.lepao:id/ion',  # f
            # 'com.yundongjiao.lepao:id/qk',
        ]
    )
    def test_advertising(self, Button):
        # Button = "com.yundongjiao.lepao:id/home_img"
        result = Advertising(Button)
        self.assertTrue(result)
        time.sleep(2)

    # 首页总的卡路里
    def test_total(self):
        logging.info("验证总卡路里")
        Button = 'com.yundongjiao.lepao:id/qk'
        result = Advertising(Button)
        self.assertTrue(result)

    # # 验证全部场馆按钮
    # def test_allCg(self):
    #     result = All(Button="com.yundongjiao.lepao:id/home_shop")
    #     self.assertTrue(result)
    #
    # # 验证全部课程按钮
    # def test_allKc(self):
    #     result = All(Button="com.yundongjiao.lepao:id/all_kc")
    #     self.assertTrue(result)

    # 验证健身目的
    def test_toal(self):
        logging.info("验证健身目的")
        result = goal()
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
    # Advertising("com.yundongjiao.lepao:id/home_img")
