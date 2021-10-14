import logging
import time
import unittest

from Home.Rank import rank_city, rank_stadium
from Tool import driver


class Rank(unittest.TestCase):

    # 城市排行
    def test_case01(self):
        logging.info("验证城市排行榜点击事件")
        result = rank_city()
        self.assertTrue(result)
        time.sleep(1)
        driver.open.get_driver().keyevent(4)

    # 社区排行
    def test_case02(self):
        logging.info("验证社区排行榜点击事件")
        result = rank_stadium()
        self.assertTrue(result)
        time.sleep(1)
        driver.open.get_driver().keyevent(4)


if __name__ == '__main__':
    unittest.main()