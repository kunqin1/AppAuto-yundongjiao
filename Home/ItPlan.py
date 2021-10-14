import random
import time
import unittest
import logging
import logging.config
from Tool import driver
from Login import denglu
from Tool import GoMainView,ComeHome

"""
智能训练计划测试
秦坤
"""

logging.config.fileConfig("../Tool/log.conf")
logging = logging.getLogger("infoLogger")


# 获取首页训练计划状态
def get_PlanState():
    ComeHome.GoHome()
    time.sleep(10)
    denglu.down_Swipe()
    # 获取首页计划状态
    text = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_day").text
    return text


# 退出智能训练计划
def exit_plan():
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_day").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/gd").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/start").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/yes").click()
    driver.open.get_driver().keyevent(4)
    # denglu.down_Swipe()


# 创建未生成状态
def make_No():
    if get_PlanState() == "未生成":
        pass
    else:
        exit_plan()


# 创建智能计划训练点击事件
def click_MakePlan():
    but1 = "com.yundongjiao.lepao:id/obj_zj"
    but2 = "com.yundongjiao.lepao:id/obj_jz"
    but3 = "com.yundongjiao.lepao:id/obj_sx"
    button = random.choice([but1, but2, but3])
    week_but1 = "com.yundongjiao.lepao:id/week_yi"
    week_but2 = "com.yundongjiao.lepao:id/week_er"
    week_but3 = "com.yundongjiao.lepao:id/week_san"
    week_but4 = "com.yundongjiao.lepao:id/week_si"
    week_but5 = "com.yundongjiao.lepao:id/week_wu"
    week_but6 = "com.yundongjiao.lepao:id/week_liu"
    week_but7 = "com.yundongjiao.lepao:id/week_qi"
    week_button1 = random.choice([week_but1, week_but2, week_but3])
    week_button2 = random.choice([week_but4, week_but5])
    week_button3 = random.choice([week_but6, week_but7])
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_day").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/drill").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/ckb").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/dri_state").click()
    driver.open.get_driver().find_element_by_id(week_button1).click()
    driver.open.get_driver().find_element_by_id(week_button2).click()
    driver.open.get_driver().find_element_by_id(week_button3).click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/next").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/next").click()
    driver.open.get_driver().find_element_by_id(button).click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/next").click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/start").click()


# 创建智能训练计划
def make_plan():
    if get_PlanState() != "未生成":
        exit_plan()
        click_MakePlan()
        try:
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/drill")
            result = False
        except:
            result = True
    else:
        click_MakePlan()
        try:
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/drill")
            result = False
        except:
            result = True
    return result


def get_plan():
    if get_PlanState() == "未生成":
        # print("1")
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_day").click()
        try:
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/drill")
            return True
        except:
            return False
    elif get_PlanState() == "今日休息":
        # print("休息")
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_day").click()
        try:
            driver.open.get_driver().find_element_by_xpath('//*[@text="今天不用训练哦!"]')
            return True
        except:
            return False
    elif get_PlanState() == "今日未完成":
        # print("未完成")
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_day").click()
        try:
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/con")
            return True
        except:
            return False
    elif get_PlanState() == "今日已完成":
        # print("已完成")
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_day").click()
        try:
            driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/sr")
            return True
        except:
            return False


# 开始智能训练计划
def start_plan():
    # 餐饮计划
    CateringPlan = "com.yundongjiao.lepao:id/cy_layout"
    JiJie = "com.yundongjiao.lepao:id/hom_img"
    # 智能训练计划第几节定位
    xpath = "//android.support.v7.widget.RecyclerView/android.widget.RelativeLayout"
    startButton = "com.yundongjiao.lepao:id/dri_btn"
    if get_PlanState() != "今日休息":
        driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_day").click()
        Sections = driver.open.get_driver().find_elements_by_xpath(xpath)
        try:
                Sections[0].click()
                driver.open.get_driver().find_element_by_id(startButton).click()
                time.sleep(30)
                driver.open.get_driver().keyevent(4)
                driver.open.get_driver().find_element_by_id(startButton)
                # driver.open.get_driver().keyevent(4)
                return True
        except:
            return False
    else:
        pass


class plan(unittest.TestCase):

    def test_MakePlan(self):
        logging.info("创建智能训练计划")
        result = make_plan()
        self.assertTrue(result)
        driver.open.get_driver().keyevent(4)

    def test_plan(self):
        logging.info("验证智能训练计划状态")
        result = get_plan()
        self.assertTrue(result)
        driver.open.get_driver().keyevent(4)

    def test_Start(self):
        logging.info("验证开始智能训练计划")
        result = start_plan()
        self.assertTrue(result)
        driver.open.get_driver().keyevent(4)

    # def tearDown(self):
    #     driver.open.get_driver().keyevent(4)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()
    suite.addTests(
        [plan("test_Start")], )
    runner = unittest.TextTestRunner()
    runner.run(suite)
    # make_plan()
    # test()
