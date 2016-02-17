#coding=utf-8
'''
Created on 2015-12-7

@author: zhengbiyu
'''
import unittest
from selenium import webdriver
import time
import sys
sys.path.append("\public")
from public import dataOperations


class QQSearchTest(unittest.TestCase):
    
    global tds
    tds=dataOperations.readxml("C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\data\\qqSearchTest.xml", "./search")


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://qq.100bt.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    #输入关键字搜索测试
    def testNoneSearch(self):
        u"输入关键字搜索测试"
        driver=self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_id("autocompleteTxt").clear()
        driver.find_element_by_id("autocompleteTxt").send_keys(u"%s"%tds["mykey"])
        nowhandle=driver.current_window_handle
        driver.find_element_by_class_name("submit ").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        
        #定位到搜索结果窗口
        allhandles=driver.window_handles
        for handle in allhandles:
            if handle!=nowhandle:
                driver.switch_to_window(handle)
        
        try: 
            self.assertRegexpMatches(driver.find_element_by_xpath(".//*[@id='main']/div[3]/div/div[1]/div[2]/div[1]").text, r"^[\s\S]*%s[\s\S]*$"%tds["mykey"])
            print "搜索成功"
        except AssertionError as e: 
            self.verificationErrors.append(str(e))
            print "搜索失败"
        
        time.sleep(3)
        
    #默认关键字搜索测试
    def testDefaultKeySearch(self):
        u"默认关键字搜索测试"
        driver=self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(3)
        nowhandle=driver.current_window_handle
        driver.find_element_by_class_name("submit ").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        
        #定位到搜索结果窗口
        allhandles=driver.window_handles
        for handle in allhandles:
            if handle!=nowhandle:
                driver.switch_to_window(handle)
        
        try: 
            self.assertRegexpMatches(driver.find_element_by_xpath(".//*[@id='main']/div[3]/div/div[1]/div[2]/div[1]").text, r"^[\s\S]*%s[\s\S]*$"%tds["defautkey"])
            print "搜索成功"
        except AssertionError as e: 
            self.verificationErrors.append(str(e))
            print "搜索失败"
        
        time.sleep(3)
        
    #空关键字搜索测试
    def testEmptyKeySearch(self):
        u"空关键字搜索测试"
        driver=self.driver
        driver.get(self.base_url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_id("autocompleteTxt").clear()
        nowhandle=driver.current_window_handle
        driver.find_element_by_class_name("submit ").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        
        #定位到搜索结果窗口
        allhandles=driver.window_handles
        for handle in allhandles:
            if handle!=nowhandle:
                driver.switch_to_window(handle)
        
        try: 
            self.assertRegexpMatches(driver.find_element_by_xpath(".//*[@id='main']/div[3]/div/div[1]/div[2]/div[1]").text, r"^[\s\S]*%s[\s\S]*$"%tds["defautkey"])
            print "搜索成功"
        except AssertionError as e: 
            self.verificationErrors.append(str(e))
            print "搜索失败"
        
        time.sleep(3)
        
        
        #关键字为全空格时搜索测试
    def testSpaceKeySearch(self):
        u"关键字为全空格时搜索测试"
        driver=self.driver
        driver.get(self.base_url) 
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(3)
        driver.find_element_by_id("autocompleteTxt").clear()
        driver.find_element_by_id("autocompleteTxt").send_keys(u"%s"%tds["spacekey"])
        driver.find_element_by_class_name("submit ").click()         
        try: 
            self.assertEqual(tds["errortips"], driver.find_element_by_class_name("errorTips").text)
            print "预期结果正常，关键字不能为空，要输入搜索关键字"
        except AssertionError as e: 
            self.verificationErrors.append(str(e))
            print "预期结果异常"
            
        time.sleep(3)
    


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()