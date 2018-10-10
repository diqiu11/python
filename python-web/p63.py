#!/usr/bin/env python
# coding=utf-8
#操作XML用SAX提取XML的标签返回
import requests
from xml.parsers.expat import ParserCreate
class Sax(object):
    def start_element(self, name, attr):
        print('name:%s, attr:%s'%(name, str(attr)))
    def end_element(self, name):
        print('end name:%s'%name)
    def char_data(self, text):
        print('data:%s'% text)

def downloadXML():
    r = requests.get('http://www.lindiqiu.top')
    return r.text
    #print(r.text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>'''

handler = Sax()
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
dw = downloadXML()
parser.Parse(xml)
#dw = downloadXML()
