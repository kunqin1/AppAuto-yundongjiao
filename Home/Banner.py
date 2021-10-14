import logging
import time
import unittest
from Tool import driver
import logging.config

"""
首页轮播图测试
秦坤
"""

# 读取loggin配置文件
logging.config.fileConfig("../Tool/log.conf")
# 设置配置项
logging = logging.getLogger("infoLogger")


# 验证首页轮播图点击事件
def banner(i):
    time.sleep(4)
    Banners = driver.open.get_driver().find_elements_by_id("com.yundongjiao.lepao:id/img")
    Banners[i].click()
    try:
        Button = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/back")
        Button.click()
        return True
    except:
        return False


class Banner(unittest.TestCase):

    def test_Banner1(self, i=0):
        logging.info("第一个")
        result = banner(i)
        self.assertTrue(result)

    def test_Banner2(self, i=0):
        logging.info("第二个")
        result = banner(i)
        self.assertTrue(result)

    # def test_Banner3(self, i=0):
    #     result = banner(i)
    #     self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()
