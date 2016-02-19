#coding=utf-8
'''
Created on 2015-11-30

@author: zhengbiyu
'''
import unittest
import time
import HTMLTestRunner

def testlist():
    #定义一个单元测试容器
    testunit=unittest.TestSuite()
    #测试用例存放路径
    casedir="C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\test_case"
    #drisover方法定义，返回的是套件集合
    discover=unittest.defaultTestLoader.discover(casedir, pattern="test_registe.py", top_level_dir=None)
    #drisover是套件集合，需要双重循环取到用例名字
    for test_suit in discover:
        for case_name in test_suit:
            testunit.addTest(case_name)
    return testunit

casenames=testlist()

#取当前时间
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
#定义测试报告存放路径
#filename="C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\report\\"+now+"result.html"
filename="C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\report\\result.html"
fp=file(filename,"wb")

runner=HTMLTestRunner.HTMLTestRunner(
                                     stream=fp,
                                     title=u"圈圈测试报告",
                                     description=u"用例执行情况:"
                                     )
#运行测试容器中的用例，并将结果写入的报告中
runner.run(casenames)
