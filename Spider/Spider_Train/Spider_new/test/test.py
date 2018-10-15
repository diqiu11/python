#coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
def download(url):
    html=urlopen(url)
    print(html.read())
    return html.read()
def parse(data):
    return_data = {}
    soup = BeautifulSoup(data,"html.parser")
    all = soup.find('div',class_='main_content')
    if all is None:
        return
    return_data['main'] = all.get_text()
    return return_data
def output(all_data):
    file = open('gw.html','w',encoding='utf-8')
    file.write('<html>')
    file.write('<body>')
    file.write('<p>%s</p>'%all_data['main'])
    file.write('</body>')
    file.write('</html>')
    file.close()
url = 'http://www.gjgwy.org/201801/368129.html'
data = download(url)
all_data = parse(data)
output(all_data)