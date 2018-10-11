



from http import cookiejar
from urllib import request
import urllib

#for bianliang
cookie = cookiejar.CookieJar()      #p2->p3 cookielib -> cookiejar

#mack cookie handler
handler = request.HTTPCookieProcessor(cookie)
#create opener
opener = request.build_opener(handler)
try:
    opener.open("http://www.baidu.com")
    for item in cookie:
        print('Name='+item.name)
        print('Values='+item.value)
except urllib.error.HTTPError as e:
    print(e.code)

#for file
filename = 'cookie.txt'

cookie1 = cookiejar.MozillaCookieJar(filename)
handle = request.HTTPCookieProcessor(cookie1)
opener1 = request.build_opener(handle)      #==urlopen
opener1.open("http://www.baidu.com")
cookie1.save(filename, ignore_discard=True, ignore_expires=True)

cookie1.load(filename, ignore_discard=True, ignore_expires=True)
response = opener1.open("http://www.baidu.com")
print(response.read())
