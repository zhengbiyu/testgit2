#coding=utf-8
'''
Created on 2015-11-6

@author: zhengbiyu
'''
import time
import chardet
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

#面板登录
def login(self,un,pw):
        driver=self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        time.sleep(10)
        driver.find_element_by_xpath(".//*[@id='nologin']/dl/dd[1]/input").clear()
        driver.find_element_by_xpath(".//*[@id='nologin']/dl/dd[1]/input").send_keys(un)
        driver.find_element_by_xpath(".//*[@id='nologin']/dl/dd[2]/input").clear()
        driver.find_element_by_xpath(".//*[@id='nologin']/dl/dd[2]/input").send_keys(pw)
        
        #自动获取验证码并填写
        js="$.getJSON('http://wx.100bt.com/util/getCode.jsonp?callback=?',function(data){$('.imgcode').val(data.code);})"
        driver.execute_script(js)
        time.sleep(7)
        driver.find_element_by_xpath(".//*[@id='nologin']/dl/dd[5]/a").click()
        time.sleep(3)
        userid=driver.find_element_by_xpath(".//*[@id='haslogin']/div[1]/div[2]/a").text
        try:
            if userid==un:
                print "登录成功"
        except:
            print "登录失败"

#弹框登录
def login1 (self,un,pw,nikename):
        driver=self.driver
        driver.maximize_window()
        driver.implicitly_wait(30)
        time.sleep(3)
        driver.find_element_by_link_text(u"登录").click()
        time.sleep(3)
        driver.find_element_by_id("zloginPop_login_duoduoId").clear()
        driver.find_element_by_id("zloginPop_login_duoduoId").send_keys(un)
        driver.find_element_by_id("zloginPop_login_pwd").clear()
        driver.find_element_by_id("zloginPop_login_pwd").send_keys(pw)
        #自动获取验证码并填写
        driver.find_element_by_id("zloginPop_login_code").clear()
        js="$.getJSON('http://wx.100bt.com/util/getCode.jsonp?callback=?',function(data){$('#zloginPop_login_code').val(data.code);})"
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_xpath(".//*[@id='loginForm']/div[4]/input").click()
        time.sleep(3)
        name=driver.find_element_by_xpath(".//*[@id='w_navCtn']/div[2]/div[2]/div[2]/div/span[1]/a").text
        try:
            if name==nikename:
                print "登录成功"
        except:
            print "登录失败"
            

#登出圈圈         
def  logout(self):
            driver=self.driver
            time.sleep(3)
            above=driver.find_element_by_xpath(".//*[@id='w_navCtn']/div[2]/div[2]/div[2]/div/span[1]/a")
            ActionChains(driver).move_to_element(above).perform()
            time.sleep(2)
            driver.find_element_by_link_text(u"退出").click()
            driver.implicitly_wait(30)
            time.sleep(2)
            try:
                t=driver.find_element_by_xpath(".//*[@id='w_navCtn']/div[2]/div[1]/a[1]").text.encode("utf-8")
                #print chardet.detect(t)
                b="登录"
                #print chardet.detect(b)
                if t==b:
                    print"退出成功"
            except:
                print "退出失败"
            
            
            

#在某圈主页上加入圈圈            
def joinqq(self):
    driver=self.driver
    try:
        driver.find_element_by_id("jiaruquanquan").click()
        driver.find_element_by_link_text("知道了").click()
        print "加圈成功"
    except:
        print "加圈失败"
        

#我的圈页面退出已加入的圈子           
def qiutqq(self,qqid):
    driver=self.driver
    driver.find_element_by_link_text(u"我的圈").click()
    driver.implicitly_wait(30)
    driver.find_element_by_link_text(u"我加入的圈子").click()
    time.sleep(3)
    driver.find_element_by_xpath(".//*[@id=%s]/div/div[1]/a[2]"%qqid).click()
    time.sleep(2)
    driver.find_element_by_link_text(u"是的,就这么做").click()
    time.sleep(2) 
    driver.find_element_by_link_text(u"知道了").click()
    time.sleep(2)
    try:
        driver.find_element_by_xpath(".//*[@id=%s]/div/div[1]/a[2]"%qqid).is_displayed()
        print "退出圈子失败"
    except:
        print "退出圈子成功"
        
#在某圈主页上的管理弹框退出圈圈  
def qiutqq1(self,qqname):
    driver=self.driver
    time.sleep(3)
    driver.find_element_by_link_text(u"管理>>").click()
    time.sleep(2)
    above=driver.find_element_by_xpath(".//*[@id='npopPop_4']/div/div[2]/div/div[2]/ul/li/span/a[1]")
    ActionChains(driver).move_to_element(above).perform()
    time.sleep(2)
    elements=driver.find_elements_by_link_text(u"[退出]")
    for element in elements:
        a=element.get_attribute("onclick").split("'")[1]
        print a
        if a==qqname:
            element.click()
        break
    driver.find_element_by_link_text(u"是的,就这么做").click()
    driver.find_element_by_link_text(u"知道了").click()
    try:
        driver.find_element_by_link_text(u"[退出]").is_displayed()
        print "退出圈子失败"
    except:
        print "退出圈子成功"
    time.sleep(2)
    
        
    
        
    
    

     
        