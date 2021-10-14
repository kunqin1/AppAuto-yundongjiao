import sys
import time
import unittest

import HTMLTestRunner

base_path = 'D:\\pythonProject'
sys.path.append(base_path)

if __name__ == '__main__':
    case_path = '../test_case'
    now_time = time.strftime("%Y-%m-%d %H-%M-%S")
    report_path = now_time + "../report/report.html"
    suit = unittest.defaultTestLoader.discover(case_path, pattern='test*.py')
    # unittest.TextTestRunner().run(discover)
    with open(report_path, "wb") as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title="测试报告", description="运动角")
        runner.run(suit)
