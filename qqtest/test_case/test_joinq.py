#coding=utf-8
'''
Created on 2015-12-4

@author: zhengbiyu
'''
import unittest
from selenium import webdriver
import time
import sys
sys.path.append("\public")
from public import commonFunctions,dataOperations


class JionQ(unittest.TestCase):
    
    global tds
    tds=dataOperations.readxml("C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\data\\joinqTest.xml", "./joinq")


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://qq.100bt.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
#在全部圈页面加入圈圈     
    def test1JionQ(self):
        u"在全部圈页面加入圈圈测试"
        driver=self.driver
        driver.get(self.base_url+tds["url"])
        driver.implicitly_wait(30)
        time.sleep(3)
        commonFunctions.login1(self,tds["username"], tds["password"], tds["nikename"])
        driver.find_element_by_link_text(u"%s"%tds["tab"]).click()
        elements= driver.find_elements_by_link_text(u"加入")
        time.sleep(2)
        for element in elements:
            a=element.get_attribute("onclick").split(",")[1]
#由于a带有双引号，所以这个tds["qqname1"]是带有双引号的圈名
            if a==tds["qqname1"]:
                element.click()
            break
        time.sleep(3)
        #点击知道了
        driver.find_element_by_xpath(".//*[@id='ipop-qqList1']/div[2]/div[2]/a/span").click()
        driver.find_element_by_link_text(u"我的圈").click()
        driver.implicitly_wait(30)
        driver.find_element_by_link_text(u"我加入的圈子").click()
        time.sleep(3)
        try:
            driver.find_element_by_link_text(u"%s"%tds["qqname"]).is_displayed()
            print "加入%s成功"%tds["qqname"].encode("utf-8")
        except:
            print "加入%s失败"%tds["qqname"].encode("utf-8")
  
        time.sleep(3)

#退出方法test1JionQ加入的圈子,从我的圈页面上退出
    def test2qiutq(self):
        u"从我的圈页面上退出方法test1JionQ加入的圈子测试"
        driver=self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        commonFunctions.login1(self,tds["username"], tds["password"], tds["nikename"])
        commonFunctions.qiutqq(self,tds["qqid"])
    
        
        
            
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
    

        





if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()