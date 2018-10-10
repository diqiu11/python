#coding:utf-8
import string
from urllib import request
from urllib.parse import quote


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None

        url_ = quote(url, safe=string.printable)    #quote函数是屏蔽掉url的无关字符    string.printable为打印所有可以打印的字符
        response = request.urlopen(url_)            #访问传入的url并且赋值给response

        if response.getcode() != 200:
            return None

        return response.read()      #返回url读取的内容