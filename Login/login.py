import time
import unittest
from telnetlib import EC
import parameterized as parameterized
from selenium.webdriver.support.wait import WebDriverWait
from Tool.driver import open
from Login.denglu import start

"""
登录测试用例
秦坤
"""


class Login(unittest.TestCase):

    def agreement(self, num=4):
        for j in range(num):
            buton = 'com.yundongjiao.lepao:id/tv_agree'
            try:
                e = WebDriverWait(self, 1, 0.5).until(EC.find_element_by_id(buton))
                e.click()
            except:
                pass

    # 密码登录和验证码登录
    def login(self, phone, pwd):
        start.skip()
        username = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/phonenumber')
        username.clear()
        username.send_keys(phone)
        password = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/password')
        password.clear()
        password.send_keys(pwd)

    # 验证登录是否成功断言
    def Assertion(self, phone, pwd):
        # start.skip()
        self.login(phone, pwd)
        open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/logins').click()
        time.sleep(2)
        try:
            open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/login')
            result = False
        except:
            result = True
        return result

    def AssertionCode(self, phone, pwd):
        self.login(phone, pwd)
        open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/logins').click()
        time.sleep(2)
        try:
            open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/login')
            result = False
        except:
            result = True
        return result

    # 电话号码格式验证，发送验证码按钮，参数化断言
    def send_code(self, phone):
        start.skip()
        id = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/phonenumber')
        id.clear()
        id.send_keys(phone)
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/code").click()
        time.sleep(5)
        try:
            button = ("xpath", ".//*[contains(@text,'手机号格式有误')]")
            elm = WebDriverWait(open.get_driver(), 5).until(EC.presence_of_element_located(button))
            result = elm
        except:
            result = True
        return result

    def always_allow(self, number=5):
        '''
        fuction:权限弹窗-始终允许
        args:1.传driver
        2.number，判断弹窗次数，默认给5次
        其它：
        WebDriverWait里面0.5s判断一次是否有弹窗，1s超时
        '''
        for i in range(number):
            loc = ("xpath", "//*[@text='始终允许']")
            try:
                e = WebDriverWait(self, 1, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                pass

    def password(self, password, isPassword):
        self.send_code()
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/password").send_keys(password)
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/ispassword").send_keys(isPassword)

    # 重置密码，电话号码验证码验证，参数化断言
    def Assert(self, phone, pwd):
        self.login(phone, pwd)
        open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/next').click()
        time.sleep(2)
        try:
            text = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/next')
            if text == '下一步':
                return 'False'
            else:
                return 'True'
        except:
            return 'True'

    # 注册功能
    def register(self, phone, code, password, ispassword):
        start.skip()
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/register")
        phone1 = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/phonenumber")
        phone1.send_keys(phone)
        code1 = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/code")
        code1.send_keys(code)
        password1 = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/password")
        password1.send_keys(password)
        ispassword1 = open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/isPassword")
        ispassword1.send_keys(ispassword)
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/register").click()
        time.sleep(2)
        title = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/register')
        if title == "注册":
            return 'False'
        else:
            return 'True'

    # 参数化电话号码和密码
    @parameterized.parameterized.expand(
        [
            ('18782048139', '12345', 'False'),
            ('', '1234567', 'False'),
            ('18782048139', ' ', 'False'),
            ('18782048139', '123557', 'False'),
            ('18782048139', '123456', 'True'),
        ]
    )
    # 账号密码登录验证
    def test_case01(self, phone, pwd, msg):
        result = self.Assertion(phone, pwd)
        self.assertEqual(msg, result)

    # 参数化话电话号码和验证码
    @parameterized.parameterized.expand(
        [
            ('', '', 'False'),
            ('18782048139', '95274', 'False'),
            ('18782048139', ' ', 'False'),
            (' ', '9527', 'False'),
            ('18782048139', '9527', 'True'),
        ]
    )
    # 验证码登录正确验证
    def test_case02(self, phone, pwd, msg):
        start.skip()
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/switchs").click()
        result = self.AssertionCode(phone, pwd)
        self.assertEqual(msg, result)

    # # 注册功能参数化
    # @parameterized.parameterized.expand(
    #     [
    #         ('18782048138', '9527', '123456', '123456', 'True'),  # 正常注册
    #         ('18782048', '9527', '123456', '123456', 'False'),  # 错误个数电话号码注册
    #         (' ', '9527', '123456', '123456', 'False'),  # 空的电话号码注册
    #         ('18782048139', '9527', '123456', '123456', 'False'),  # 已经注册的号码再次注册
    #         ('18782048137', '9525', '123456', '123456', 'False'),  # 错误的验证码注册
    #         ('18782048137', ' ', '123456', '123456', 'False'),  # 空的验证码注册
    #         ('18782048137', '95271', '123456', '123456', 'False'),  # 错误的验证码注册
    #         ('18782048131', '9527', '', '123456', 'False'),  # 空的密码注册
    #         ('18782048131', '9527', '123456', ' ', 'False'),  # 空的确认密码注册
    #         ('18782048131', '9527', '123456', '1234567', 'False'),  # 不一致的密码注册
    #     ]
    # )
    # def test_case03(self, phone, code, password, ispassword, msg):
    #     result = self.register(phone, code, password, ispassword)
    #     self.assertEqual(result, msg)

    # # 电话格式验证
    # @parameterized.parameterized.expand(
    #     [('18782048139', 'True'),
    #      ('55656566', '手机号格式有误'),
    #      (' ', '请输入手机号'),
    #      ('18782048158', '手机号未注册'),
    #      ]
    # )
    # # 发送验证码验证按钮验证，已注册、未注册、电话号码格式错误
    # def test_05(self, phone, msg):
    #     self.driver.find_element_by_id("com.yundongjiao.lepao:id/switchs").click()
    #     time.sleep(2)
    #     result = self.send_code(phone).text
    #     print(msg)
    #     print(result)
    #     self.assertEqual(msg, result)

    # 忘记密码，电话号码和验证码验证
    # @parameterized.parameterized.expand(
    #     [
    #         ('18782048139', '9527', 'True'),
    #         ('18782048139', '95274', 'False'),
    #         ('18782048139', ' ', 'False'),
    #         (' ', '9527', 'False'),
    #         (' ', ' ', 'False'),
    #     ]
    # )
    # def test_07(self, phone, pwd, msg):
    #     start.skip()
    #     open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/forget").click()
    #     time.sleep(2)
    #     result = self.Assert(phone, pwd)
    #     self.assertEqual(result, msg)


if __name__ == '__main__':
    unittest.main()
