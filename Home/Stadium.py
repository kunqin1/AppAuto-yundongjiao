import re
import unittest
from Tool import moreButton, ComeHome, driver

"""
场馆测试
秦坤
"""


# 验证场馆详情页，场馆名称是否一致
def Stadium_details(button):
    # global result
    global result
    moreButton.click_MoreButton(button)
    # 定位所有的场馆介绍
    stadiums = driver.open.get_driver().find_elements_by_xpath('//android.support.v7.widget.RecyclerView/android.widget'
                                                               '.RelativeLayout')
    # 定位所有的场馆名称
    names = driver.open.get_driver().find_elements_by_id("com.yundongjiao.lepao:id/name")

    for i in range(len(stadiums)):
        try:
            stadiums[i].click()
            shopName = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/shopname").text
            # print(shopName)
            driver.open.get_driver().keyevent(4)
            if names[i].text == shopName:
                result = "True"
            # print("pass")
            else:
                result = "False"
                # print("Failed")
        except:
            return False
    return result


# 验证切换地区功能
def Switch_city(button):
    global result
    moreButton.click_MoreButton(button)
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/city").click()
    citys = driver.open.get_driver().find_elements_by_xpath('//android.view.ViewGroup/android.widget.TextView')
    for i in range(len(citys)):
        try:
            name = citys[i].text
            citys[i].click()
            cityName = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/name").text
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/city").click()
            # 正则匹配详细地址是否含有市名
            res = re.match(cityName, name)
            if res != 'None':
                result = "True"
            else:
                result = "False"
        except:
            return False
    return result


# 验证导航功能
def Address(button):
    moreButton.click_MoreButton(button)
    stadiums = driver.open.get_driver().find_elements_by_xpath('//android.support.v7.widget.RecyclerView/android.widget'
                                                               '.RelativeLayout')
    stadiums[0].click()
    # 导航
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/address").click()
    try:
        driver.open.get_driver().find_element_by_id("android:id/parentPanel")
        GD = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/gd")
        BD = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/bd")
        GD.click()
        return True
    except:
        return False


def Phone(button):
    moreButton.click_MoreButton(button)
    stadiums = driver.open.get_driver().find_elements_by_xpath('//android.support.v7.widget.RecyclerView/android.widget'
                                                               '.RelativeLayout')
    stadiums[0].click()
    # 电话
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/dh").click()
    try:
        # 取消拨打电话
        QX = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/qx")
        QX.click()
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/dh").click()
        BD = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/qd")
        BD.click()
        return True
    except:
        return False


class Stadium(unittest.TestCase):

    def setUp(self):
        ComeHome.GoHome()

    def test_StadiumDetails(self, button="com.yundongjiao.lepao:id/home_shop"):
        # print("4")
        self.assertTrue(Stadium_details(button))
        driver.open.get_driver().keyevent(4)

    def test_switchCity(self, button="com.yundongjiao.lepao:id/home_shop"):
        # print("3")
        self.assertTrue(Switch_city(button))
        driver.open.get_driver().keyevent(4)

    def test_Address(self, button="com.yundongjiao.lepao:id/home_shop"):
        # print("2")
        self.assertTrue(Address(button))
        driver.open.get_driver().keyevent(4)
        driver.open.get_driver()

    def test_phone(self, button="com.yundongjiao.lepao:id/home_shop"):
        # print("1")
        self.assertTrue(Phone(button))
        driver.open.get_driver().keyevent(4)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(
        [Stadium("test_StadiumDetails"), Stadium("test_switchCity"), Stadium("test_Address"), Stadium("test_phone")])
    runner = unittest.TextTestRunner()
    runner.run(suite)
