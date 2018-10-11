'''

'''
#coding:utf-8
from http import cookiejar
from urllib import request
import urllib
import urllib3

filename = 'cookie1.txt'
cookie = cookiejar.MozillaCookieJar(filename)
hander = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(hander)
loginurl = 'http://www1.gdpi.edu.cn/jwc/login'
data = {'stu':'20162202072', 'password':'123456'}
result = opener.open(loginurl, data)
cookie.save(filename, ignore_discard=True, ignore_expires=True)
gradeUrl = ''
result1 = opener.open(gradeUrl)
print(result1.read())
