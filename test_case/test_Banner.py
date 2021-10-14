import logging
import unittest

from Home.Banner import banner


class test_Banner(unittest.TestCase):
    def test_Banner1(self, i=0):
        logging.info("第一个")
        result = banner(i)
        self.assertTrue(result)

    def test_Banner2(self, i=0):
        logging.info("第二个")
        result = banner(i)
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
