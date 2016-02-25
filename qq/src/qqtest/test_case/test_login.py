#coding=utf-8
'''
Created on 2015-11-4

@author: zhengbiyu
'''
import unittest
import sys
sys.path.append("\public")
from public import commonFunctions,dataOperations
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time


class LoginTest(unittest.TestCase):
    
    global tds
    tds=dataOperations.readxml("C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\data\\loginTest.xml", "./login")


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://qq.100bt.com"
        self.verificationErrors = []
        self.accept_next_alert = True
        
#弹框登录测试   
    def testLogin(self):
        u"弹框登录测试"
        driver=self.driver      
        driver.get(self.base_url)
        #commonFunctions.login(self,tds["username"],tds["password"])
        commonFunctions.login1(self,tds["username"],tds["password"],tds["nikename"])
        
        #登出圈圈
        commonFunctions.logout(self)
        
        
        
        
        
        

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()