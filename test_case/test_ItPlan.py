import logging
import unittest

from Home.ItPlan import make_plan, get_plan, start_plan
from Tool import driver


class plan(unittest.TestCase):

    def test_MakePlan(self):
        logging.info("创建智能训练计划")
        result = make_plan()
        self.assertTrue(result)
        driver.open.get_driver().keyevent(4)

    def test_plan(self):
        logging.info("检查智能训练计划的状态")
        result = get_plan()
        self.assertTrue(result)
        driver.open.get_driver().keyevent(4)

    def test_Start(self):
        logging.info("验证开始智能训练计划")
        result = start_plan()
        self.assertTrue(result)
        driver.open.get_driver().keyevent(4)


if __name__ == '__main__':
    unittest.main()