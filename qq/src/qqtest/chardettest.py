
'''
Created on 2015-12-17

@author: zhengbiyu
'''
from selenium import webdriver
import unittest
import chardet
class RegisteTest(unittest.TestCase):


    def setUp(self):
        self.driver=webdriver.Chrome()
        self.base_url="http://qq.100bt.com/"

    def testRegiste(self):
        driver=self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.implicitly_wait(30)
        a=driver.find_element_by_class_name("navLinks_zhuce").text.encode("utf-8")
        print a
        print chardet.detect(a)

        
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()