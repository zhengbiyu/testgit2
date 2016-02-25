#coding=utf-8
'''
Created on 2015-11-26

@author: zhengbiyu
'''
import unittest
from selenium import webdriver
import time
import sys
sys.path.append("\public")
from public import commonFunctions,dataOperations


class Test(unittest.TestCase):
    
    global tds
    tds=dataOperations.readxml("C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\data\\writeSNovalTest.xml", "./snoval")


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://qq.100bt.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
        
    #短篇小说发表测试
    def testwsnovel(self):
        u"短篇小说发表测试 "
        driver=self.driver
        url=self.base_url+tds["moreurl"]
        driver.get(url)
        driver.implicitly_wait(30)
        driver.maximize_window()
        time.sleep(3)
        commonFunctions.login1(self,tds["username"],tds["password"],tds["nikename"])
        time.sleep(3)

        driver.find_element_by_id("novelName").clear()
        driver.find_element_by_id("novelName").send_keys(u"%s"%tds["novalName"])
        driver.find_element_by_id("authorName").clear()
        driver.find_element_by_id("authorName").send_keys(u"%s"%tds["authorName"])
        driver.find_element_by_xpath(u"%s"%tds["length"]).click()
        driver.find_element_by_class_name("cate_tri").click()
        driver.find_element_by_link_text(u"%s"%tds["category"]).click()
        
        #把元素设为可视化便于操作，hidden设为text使可输入url
        js="document.getElementById('coverImgSrc').setAttribute('type','text')"
        driver.execute_script(js)
        
        #暂时没有更好的办法，可上传url
        driver.find_element_by_id("coverImgSrc").send_keys(u"%s"%tds["coverImgSrc"])    
        driver.find_element_by_id("novelBrief").clear()
        driver.find_element_by_id("novelBrief").send_keys(u"%s"%tds["novelBrief"])
        driver.find_element_by_xpath(u"%s"%tds["bindTops"]).click()
        driver.find_element_by_id("markText").clear()
        driver.find_element_by_id("markText").send_keys(u"%s"%tds["markText"])
        driver.find_element_by_id("submitInformation").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"查看我的小说").click()
        time.sleep(3)
        try:
            driver.find_element_by_link_text(u"%s"%tds["novalName"]).is_displayed()
            print "小说发表成功"
        except:
            print "发表失败"
        
        #清除测试数据
        driver.find_element_by_link_text(u"删除").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"是的,就这么做").click()    
        try:
            driver.find_element_by_link_text(u"%s"%tds["novalname"]).is_displayed()
            print"删除小说失败"            
        except:
            print "删除小说成功"
        
        #登出圈圈
        commonFunctions.logout(self)
        
    def tearDown(self):
        #退出浏览器
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()