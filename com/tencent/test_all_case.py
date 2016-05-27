import os

'''if __name__ == '__main__':
    caselist = os.listdir('D:\\software\\eclipse\\eclipse\\workspace\\Test\\src\\test\\testcase\\test_case')
    for a in caselist:
        s = a.split('.')[1]

        if s == "py":
            os.system('D:\\software\\eclipse\\eclipse\\workspace\\Test\\src\\test\\testcase\\test_case\\%s 1>>log.txt 2>&1'%a)
'''
import unittest
import HTMLTestRunner
import time

# from test.testcase import alltest_list


listaa = "D:\\software\\eclipse\\eclipse\\workspace\\Test\\src\\test\\testcase\\test_case"


def creatsuitel():
    suit = unittest.TestSuite()
    # discover 方法定义
    dis = unittest.defaultTestLoader.discover(listaa, pattern='test_*.py', top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suit in dis:
        print('test_suit : %s' % test_suit)
        for test in test_suit:
            suit.addTest(test)
    return suit


alltestnames = creatsuitel()
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

filename = "D:\\report\\" + now + "_result.html"
fp = open(filename, 'wb')
runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="测试报告", description="测试结果")

# 执行测试用例
runner.run(alltestnames)
fp.close()


