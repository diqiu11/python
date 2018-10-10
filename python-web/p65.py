#!/usr/bin/env python
# coding=utf-8
#HTMLParse解析静态页面
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request
from urllib.request import urlopen
class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print('<%s>' % tag)

    def handle_endtag(self, tag):
        print('</%s>' % tag)

    def handle_startendtag(self, tag, attrs):
        print('<%s/>' % tag)

    def handle_data(self, data):
        print(data)

    def handle_comment(self, data):
        print('<!--', data, '-->')

    def handle_entityref(self, name):
        print('&%s;' % name)

    def handle_charref(self, name):
        print('&#%s;' % name)

page = 'http://www.lindiqiu.top'
with request.urlopen(page, timeout=4) as url:
    data = url.read()

parser = MyHTMLParser()
parser.feed(data.decode('utf-8'))

