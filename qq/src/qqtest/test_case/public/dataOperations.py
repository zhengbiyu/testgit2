#coding=utf-8
'''
Created on 2015-11-18

@author: zhengbiyu
'''
#import xml.dom.minidom
from xml.etree import ElementTree as ET

#读取单个标签
'''
def readxml(self,filename,tagname):
    dom=xml.dom.minidom.parse(filename)
    root=dom.documentElement
    value=root.getElementsByTagName(tagname)[0].firstChild.data
    return value
'''

#遍历login下的所有字标签
#tagname格式"./login"
def readxml(filename,tagname):
    datas={}
    per=ET.parse(filename)
    p=per.findall(tagname)
    for oneper in p:
        for child in oneper.getchildren():
            #print child.tag,':',child.text
            datas[child.tag]=child.text
    return datas

    
    