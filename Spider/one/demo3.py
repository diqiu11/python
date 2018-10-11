'''

'''
#coding:utf-8
from urllib import request
import urllib
import urllib3
values = {'username' : 'didi', 'password' : '123'}
data = urllib3.request.urlencode(values)
#response = request.urlopen("http://www.baidu.com", timeout=10)
#response2 = request.urlopen("http://www.baidu.com", data, 10)


try:
    request.urlopen("http://www.xxxx123.com")
except urllib.error.URLError as e:     #python3
    print(e.reason)

