import time
from Tool.driver import open

"""
进入登录页面
秦坤
"""


# 向右滑动
def right_Swipe(x1, y1, x2, y2):
    open.get_driver().swipe(x1, y1, x2, y2, 400)


# 向左滑动
def left_Swipe():
    open.get_driver().swipe(600, 1000, 150, 1000, 400)


# 向上滑动
def up_Swipe():
    open.get_driver().swipe(450, 1600, 450, 750, 800)


# 向下滑动
def down_Swipe():
    open.get_driver().swipe(450, 900, 450, 1700, 800)


class Start:

    def get_size(self):
        x = open.get_driver().get_window_size()['width']
        y = open.get_driver().get_window_size()['height']

    def skip(self):
        try:
            # 隐私协议同意按钮
            open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/tv_agree').click()
            # 跳过按钮
            SkipButton = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/tg')
            SkipButton.click()
            # StartButton = Start().find_element_by_id('com.yundongjiao.lepao:id/btn')
            # StartButton.click()
        except:
            pass
        time.sleep(4)

    # 密码登录和验证码登录
    def logon(self, phone, pwd):
        self.skip()
        username = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/phonenumber')
        username.clear()
        username.send_keys(phone)
        password = open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/password')
        password.clear()
        password.send_keys(pwd)

    def login(self, phone, pwd):
        self.logon(phone, pwd)
        open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/logins").click()
        try:
            open.get_driver().find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
            open.get_driver().find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()

        except:
            pass


start = Start()
if __name__ == '__main__':
    start.logon('18782048139', '1234567')
