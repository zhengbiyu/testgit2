#coding=utf-8
'''
Created on 2015-11-30

@author: zhengbiyu
'''
import unittest
import time
import sys
import chardet
from selenium import webdriver
sys.path.append("\public")
from public import dataOperations


class RegisteTest(unittest.TestCase):

    global tds
    tds=dataOperations.readxml("C:\\Users\\zhengbiyu\\workspace\\qq\\src\\qqtest\\data\\registeTest.xml", "./registe")

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.base_url="http://qq.100bt.com/"

#注册测试
    def testRegiste(self):
        u"注册测试"
        driver=self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.find_element_by_class_name("navLinks_zhuce").click()
        time.sleep(3)
        driver.find_element_by_id("zloginPop_reg_code").clear()
        js="$.getJSON('http://wx.100bt.com/util/getCode.jsonp?callback=?',function(data){$('.zinput_txt').val(data.code);})"
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_id("zloginPop_reg_pwd1").clear()
        driver.find_element_by_id("zloginPop_reg_pwd1").send_keys(tds["reg_pwd1"])
        driver.find_element_by_id("zloginPop_reg_pwd2").clear()
        driver.find_element_by_id("zloginPop_reg_pwd2").send_keys(tds["reg_pwd2"])
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='registerForm']/div[5]/div[2]/input").click()
        
        #这里要等待几秒，下面的多多号和密才能打印出来
        time.sleep(3)     
        try:
            duoduoId=driver.find_element_by_class_name("regi_suc_duoduoId").text.encode("utf-8")
            password=driver.find_element_by_class_name("regi_suc_password").text.encode("utf-8")
            print chardet.detect(duoduoId)
            print chardet.detect(password)
            print "注册成功，多多号：%s，密码：%s"%(duoduoId,password) 
            driver.find_element_by_xpath(".//*[@id='zloginpop']/div[2]/div/div[4]/div[4]/a").click()
        except:
            print "注册失败"
            
        
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()