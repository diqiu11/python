#!/usr/bin/env python
# coding=utf-8
#获取yahho天气
from xml.parsers.expat import ParserCreate
from urllib import request
class SAX(object):
    weather = {'city':'','forecast':[]}
    def start_element(self, name, attr):
        if name == 'yweather:location':
           self.weather['city'] = attr['city']
        if name == 'yweather:forecast':
            self.weather['forecast'].append({'date':attr['date'], 'day':attr['day'], 'high':attr['high'], 'low':attr['low']})
        #print('name:%s, attr:%s' %(name, str(attr)))
    def end_element(self, name):
        print('name:%s' %name)
    def char_data(self, text):
        print('data:%s' %text)
def parseXml(xml_str):
    handler = SAX()
    parser = ParserCreate()
    parser.StartElementHandler = handler.start_element
    parser.EndElementHandler = handler.end_element
    parser.CharacterDataHandler = handler.char_data
    parser.Parse(xml_str)

# 测试:
URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=xml'

with request.urlopen(URL, timeout=4) as f:
    data = f.read()

result = parseXml(data.decode('utf-8'))
assert result['city'] == 'Beijing'
