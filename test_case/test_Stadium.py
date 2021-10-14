import logging
import unittest

from Home.Stadium import Stadium_details, Switch_city, Address, Phone
from Tool import ComeHome, driver


class Stadium(unittest.TestCase):

    def setUp(self):
        ComeHome.GoHome()

    def test_StadiumDetails(self, button="com.yundongjiao.lepao:id/home_shop"):
        logging.info("验证场馆详情")
        self.assertTrue(Stadium_details(button))
        driver.open.get_driver().keyevent(4)

    # def test_switchCity(self, button="com.yundongjiao.lepao:id/home_shop"):
    #     # print("3")
    #     logging.info("切换城市功能")
    #     self.assertTrue(Switch_city(button))
    #     driver.open.get_driver().keyevent(4)

    def test_Address(self, button="com.yundongjiao.lepao:id/home_shop"):
        # print("2")
        logging.info("验证导航功能")
        self.assertTrue(Address(button))
        driver.open.get_driver().keyevent(4)
        driver.open.get_driver()

    def test_phone(self, button="com.yundongjiao.lepao:id/home_shop"):
        # print("1")
        logging.info("验证拨打电话功能")
        self.assertTrue(Phone(button))
        driver.open.get_driver().keyevent(4)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(
        [Stadium("test_StadiumDetails"), Stadium("test_switchCity"), Stadium("test_Address"), Stadium("test_phone")])
    runner = unittest.TextTestRunner()
    runner.run(suite)