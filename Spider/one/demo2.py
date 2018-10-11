'''

'''
import requests
import re
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = 'https://www.zhihu.com/question/20399991'
r = requests.get(url,headers=header)
text = r.text
#User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36

jpg = re.compile(r'https://[^\s]*?_r\.jpg')
jpge = re.compile(r'https://[^\s]*?_r\.jpge')
gif = re.compile(r'https://[^\s]*?_r\.gif')
png = re.compile(r'https://[^\s]*?_r\.png')
imgs=[]
imgs+=jpg.findall(text)
imgs+=jpge.findall(text)
imgs+=png.findall(text)
imgs+=gif.findall(text)

def download(url):
    req = requests.get(url)
    if req.status_code == 200:
        name = url.split('/')[-1]
        f = open("./"+name, 'wb')
        f.write(req.content)
        f.close()
        return True
    else:
        return False
    
    errors = []
    for img_url in imgs:
        print("download :"+img_url)
    else:
        errors.append(img_url)
    
    print("ERROR URLS:")
    print(errors)
    