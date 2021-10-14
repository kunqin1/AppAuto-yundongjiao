import logging
import time
import unittest
from Tool.driver import open
import parameterized
from Tool import ComeHome, moreButton, driver, GoMainView
from Home.Home import Advertising, goal


class Home(unittest.TestCase):
    def setUp(self):
        ComeHome.GoHome()

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
            # 'com.yundongjiao.lepao:id/ion',  # f
            # 'com.yundongjiao.lepao:id/qk',
        ]
    )
    def test_advertising(self, Button):
        logging.info("测试首页各模块点击事件")
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
        # time.sleep(2)
        GoMainView.GoMainView(0)
        logging.info("返回首页")

    # # 验证全部场馆按钮
    # def test_allCg(self):
    #     result = All(Button="com.yundongjiao.lepao:id/home_shop")
    #     self.assertTrue(result)
    #
    # # 验证全部课程按钮
    # def test_allKc(self):
    #     result = All(Button="com.yundongjiao.lepao:id/all_kc")
    #     self.assertTrue(result)

    # # 验证健身目的
    # def test_toal(self):
    #     logging.info("验证健身目的")
    #     result = goal()
    #     self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()