import time
import unittest
import parameterized as parameterized
from Tool.driver import open
from Login.denglu import start


class Advertising_test(unittest.TestCase):

    def setUp(self):
        pass

    def Assertion(self, phone, pwd):
        start.logon(phone, pwd)
        open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/logins').click()
        try:
            title = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/home_con')
            return title.text
        except:
            return 'False'

    def AssertionSheep(self, phone, pwd):
        start.logon(phone, pwd)
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/logins").click()
        try:
            title = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/home_con')
            title.click()
            price = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/price")
            return price
        except:
            return 'False'

    # 消 费记录
    def Assertionconsume(self, phone, pwd):
        start.logon(phone, pwd)
        open.find_element_by_id("com.yundongjiao.lepao:id/logins").click()
        # 进入我的页面
        open.get_driver().find_element_by_class_name("android.widget.RelativeLayout").click()
        # 点击开通按钮
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/me_yt").click()
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/conversion").click()
        try:
            title = open.get_driver().find_element_by_class_name("android.widget.TextView")
            if title.text == '卡包明细':
                return 'True'
            else:
                return 'False'
        except:
            return 'False'

    def AssertionZF(self, phone, pwd):
        start.logon(phone, pwd)
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/logins").click()
        try:
            open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/home_con').click()
            open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/btn_zf").click()
            price =  open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/price")
            # denlu.set_driver().find_element_by_id("com.yundongjiao.lepao:id/btn_zf").click()
            # denlu.set_driver().find_element_by_id("com.yundongjiao.lepao:id/ck_zfb").click()
            return ''
        except:
            return 'False'

    # 验证不同类型的卡对应的价格、天数
    def type(self, phone, pwd, number):
        list = []
        start.logon(phone, pwd)
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/logins").click()
        open.get_driver().find_element_by_class_name("android.widget.RelativeLayout").click()
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/me_yt").click()

        while number < 3:
            self.get_size(800, 350)
            number = number + 1
        ioc = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/ion").text
        data = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/date").text
        prize = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/price").text
        list.append(ioc)
        list.append(data)
        list.append(prize)
        return list

    # 购买下一页价格显示正确
    def sheepDetail(self, phone, pwd, number):
        start.logon(phone, pwd)
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/logins").click()
        open.get_driver().find_element_by_class_name("android.widget.RelativeLayout").click()
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/me_yt").click()
        while number < 3:
            self.get_size(800, 350)
            number = number + 1
        try:
            ioc = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/ion").text
            prize = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/price").text
            open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/btn_zf").click()
            time.sleep(3)
            title = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/title").text
            prize1 = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/price").text
            if ioc == title and prize == prize1:
                return "True"
            else:
                return "False"
        except:
            return "False"

    def get_size(self, m, n):
        x = open.get_driver().get_window_size()['width']
        y = open.get_driver().get_window_size()['height']
        open.get_driver().swipe(m, 1500, n, 1500, 400)

    @parameterized.parameterized.expand(
        [
            ('18782048139', '1234567', '运动月卡已过期'),
            ('15120915620', '123456', 'True'),
            ('18084910005', '123456', '月卡优惠')
        ]
    )
    def test_case01(self, phone, pwd, msg):
        result = self.Assertion(phone, pwd)
        self.assertEqual(msg, result)

    @parameterized.parameterized.expand(
        [
            ('18782048139', '1234567', '99.00'),  # 正常月卡过期，无优惠
            ('15120915620', '123456', 'False'),  # 剩余月卡天数正常
            ('18084910005', '123456', '77.00')  # 优惠状态
        ]
    )
    #  不同月卡价格验证
    def test_case03(self, phone, pwd, msg):
        result = self.AssertionSheep(phone, pwd)
        self.assertEqual(msg, result)

    def test_04(self):
        result = self.Assertionconsume("18782048139", "1234567")
        self.assertEqual(result, "True")

    # 参数化滑动次数，查看不同卡的价格
    @parameterized.parameterized.expand(
        [
            ("3", ["运动角月卡", "30天", "99.00"]),
            ("2", ["运动角季卡", "120天", "299.00"]),
            ("1", ["运动角年卡", "395天", "699.00"])
        ]
    )
    def test_05(self, number, prizes):
        result = self.type("18782048139", "1234567", number)
        self.assertEqual(result, prizes)
        list.clear()

    @parameterized.parameterized.expand(
        [
            ("3", "Ture"),
            ("2", "Ture"),
            ("1", "Ture")
        ]
    )
    def test_06(self, number, msg):
        result = self.sheepDetail("18782048139", "1234567", number)
        self.assertEqual(result, msg)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(Advertising_test("test_case01"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
