#coding:utf-8
import string
from urllib import request
from urllib.parse import quote
class HtmlDownload(object):
    def download(self, url):
        if url is None:
            return None
        url_ = quote(url, safe=string.printable)
        response = request.urlopen(url_)
        if response.getcode() != 200:
            return False
        #print(response.read())
        return response.read()