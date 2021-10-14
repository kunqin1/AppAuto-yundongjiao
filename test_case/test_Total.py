import logging
import unittest

from Home.Total import Select_total


class JSTotal(unittest.TestCase):

    def test_JZTotal(self, i=0):
        logging.info("验证把健身目的切换为减脂正常")
        result = Select_total(i)
        self.assertTrue(result)

    def test_TNTotal(self, i=1):
        logging.info("验证把健身目的切换为体能正常")
        result = Select_total(i)
        self.assertTrue(result)

    def test_ZJTotal(self, i=2):
        logging.info("验证把健身目的切换为增肌正常")
        result = Select_total(i)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()