import unittest
from Tool import driver, ComeHome, moreButton

"""
健身目的测试
秦坤
"""


def Select_total(i):
    # GoMainView.GoMainView(0)
    ComeHome.GoHome()
    # moreButton.GoHomeTop()
    total = driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/home_type")
    total.click()
    totals = driver.open.get_driver().find_elements_by_id("com.yundongjiao.lepao:id/ion")
    print(totals)
    button = totals[i]
    button.click()
    driver.open.get_driver().find_element_by_id("com.yundongjiao.lepao:id/ok").click()
    if button == totals[0]:
        if total.text == "减脂":
            return True
        else:
            return False
    elif button == totals[1]:
        if total.text == "体能":
            return True
        else:
            return False
    elif button == totals[2]:
        if total.text == "增肌":
            return True
        else:
            return False


class JSTotal(unittest.TestCase):

    def test_JZTotal(self, i=0):
        result = Select_total(i)
        self.assertTrue(result)

    def test_TNTotal(self, i=1):
        result = Select_total(i)
        self.assertTrue(result)

    def test_ZJTotal(self, i=2):
        result = Select_total(i)
        self.assertTrue(result)


if __name__ == '__main__':
    # unittest.main()
    Select_total(1)
