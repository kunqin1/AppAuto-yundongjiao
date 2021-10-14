import logging
import unittest

from Home.Course import TJCourses, AllCourse, WeederCourse, StartCourse
from Tool import ComeHome


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
    unittest.main()
