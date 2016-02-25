#coding=utf-8
'''
Created on 2015-11-27

@author: zhengbiyu
'''
import unittest
from selenium import webdriver
import time
import sys
sys.path.append("\public")
from public import commonFunctions,dataOperations
from selenium.webdriver.common.action_chains import ActionChains



class PublishTopicTest(unittest.TestCase):
    
#读取测试数据
    global tds
    tds=dataOperations.readxml("C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\data\\publishTopicTest2.xml", "./topic")

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url="http://qq.100bt.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

#未加圈发话题测试 
    def test1PublishTopic(self):
        u"未加圈发话题测试 "
        driver=self.driver
        url=self.base_url+"%s/"%tds["qqid"]
        driver.get(url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        commonFunctions.login1(self,tds["username"], tds["password"], tds["nikename"])
        time.sleep(3)
        nowhandle=driver.current_window_handle
        driver.find_element_by_link_text(u"发表话题").click()
        driver.implicitly_wait(30)
        time.sleep(3)
        
        #由于发表新话题会新窗口打开，所以要指向新窗口，即发话题窗口
        allhandles=driver.window_handles
        for handle in allhandles:
            if(handle!=nowhandle):
                driver.switch_to_window(handle)

        #填写话题数据             
        driver.find_element_by_link_text(u"%s"%tds["category"]).click()
        driver.find_element_by_xpath(".//*[@id='main']/div[4]/div/div/div/div[3]/input").clear()
        driver.find_element_by_xpath(".//*[@id='main']/div[4]/div/div/div/div[3]/input").send_keys(u"%s"%tds["title"])
        driver.find_element_by_xpath(".//*[@id='ueditor_0']").send_keys(u"​%s"%tds["view"])
        driver.find_element_by_id("shareforQQwb").click()

 
        #点击发表话题，根据提示加入该圈子
        driver.find_element_by_xpath(".//*[@id='main']/div[4]/div/div/div/div[6]/a[1]").click()
        time.sleep(3)
        driver.find_element_by_link_text(u"加入该圈子").is_displayed()
        driver.find_element_by_link_text(u"加入该圈子").click()
        driver.find_element_by_link_text(u"知道了").click()
        
        #重新点击发表话题   
        driver.find_element_by_xpath(".//*[@id='main']/div[4]/div/div/div/div[6]/a[1]").click()

        time.sleep(3)
        #验证是否发话题成功
        try:
            topictitle=driver.find_element_by_xpath(".//*[@id='st-Title']/div/h1/span").text
            if topictitle==tds["title"]:
                print "发表话题成功"
        except:
            print "发表话题失败"
        
        #在当前页面的管理弹框上退出该圈子
        commonFunctions.qiutqq1(self,tds["qqname"]) 


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()