import time
import unittest
import logging
import logging.config
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
from Tool import driver, ComeHome, moreButton
from Login import denglu

"""
推荐课程测试
秦坤
"""

# 读取loggin配置文件
logging.config.fileConfig("../Tool/log.conf")
# 设置配置项
logging = logging.getLogger("infoLogger")


# 推荐课程页面banner位滑动是否正常
def TJCourses(button):
    global result
    moreButton.click_MoreButton(button)
    # 推荐课程页面banner位
    courses = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/banner")
    # print(courses)
    for i in range(1, 6):
        try:
            courses.click()
            driver.open.get_driver().keyevent(4)
            time.sleep(2)
            # 滑动屏幕
            # TouchAction(driver.open.get_driver()).press(x=320, y=480).move_to(x=600, y=480).release().perform()
            denglu.right_Swipe(320, 480, 600, 480)
            # print("t")
            result = True
        except:
            # print("f")
            result = False
    return result


# 验证全部推荐课程页面
def AllCourse(button):
    global result
    moreButton.click_MoreButton(button)
    driver.open.get_driver().find_element_by_id('com.yundongjiao.lepao:id/allCurri').click()
    courses = driver.open.get_driver().find_elements_by_id("com.yundongjiao.lepao:id/img")
    # print(courses)
    for i in range(len(courses)):
        try:
            time.sleep(2)
            courses[i].click()
            driver.open.get_driver().keyevent(4)
            result = True
        except:
            result = False
    return result


# 筛选课程功能和进退课程详情页正常
def WeederCourse(button):
    global result
    moreButton.click_MoreButton(button)
    CourseTypes = driver.open.get_driver().find_elements_by_xpath('//android.support.v7.app.ActionBar.Tab')
    courses = driver.open.get_driver().find_elements_by_id("com.yundongjiao.lepao:id/img")
    for i in range(len(CourseTypes)):
        try:
            time.sleep(2)
            CourseTypes[i].click()
            for j in range(len(courses)):
                time.sleep(2)
                courses[j].click()
                driver.open.get_driver().keyevent(4)
                result = True
            # return result
        except:
            result = False

    return result


# 课程详情页，开始、退出功能
def StartCourse(button):
    moreButton.click_MoreButton(button)
    CourseTypes = driver.open.get_driver().find_elements_by_xpath('//android.support.v7.app.ActionBar.Tab')
    courses = driver.open.get_driver().find_elements_by_id("com.yundongjiao.lepao:id/img")
    # driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/banner").click()
    CourseTypes[2].click()
    courses[2].click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/join").click()
    try:
        text = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/join").text
        if text != "开始课程":
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/join").click()
        else:
            pass
        # WebDriverWait(driver, 300).until(lambda x: x.find_element_by_id("com.yundongjiao.lepao:id/sha_fx"))
        # 课程完成显示分享页面
        # time.sleep(300)
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/video_ui")
        # print("T")
        return False
    except:
        return True
        # print("F")


class Course(unittest.TestCase):

    def setUp(self):
        logging.info("返回到首页")
        ComeHome.GoHome()

    def test_Banner(self):
        logging.info("课程banner位")
        result = TJCourses(button="com.yundongjiao.lepao:id/all_kc")
        self.assertTrue(result)

    def test_AllCourse(self):
        logging.info("遍历查看全部课程")
        result = AllCourse(button="com.yundongjiao.lepao:id/all_kc")
        self.assertTrue(result)

    def test_WeederCourse(self):
        logging.info("赛选课程功能")
        result = WeederCourse(button="com.yundongjiao.lepao:id/all_kc")
        self.assertTrue(result)

    def test_StartCourse(self):
        logging.info("遍历开始课程")
        result = StartCourse(button="com.yundongjiao.lepao:id/all_kc")
        self.assertTrue(result)


if __name__ == '__main__':
    # StartCourse(button="com.yundongjiao.lepao:id/all_kc")
    # AllCourse(button="com.yundongjiao.lepao:id/all_kc")
    # TJCourses(button="com.yundongjiao.lepao:id/all_kc")
    # WeederCourse(button="com.yundongjiao.lepao:id/all_kc")
    unittest.main()
