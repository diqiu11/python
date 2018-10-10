#!/usr/bin/env python
# coding=utf-8
#提取网页json

from urllib import request
from urllib.request import urlopen
import requests
import json
def fetch_data(url):
    with request.urlopen(url) as page:
        data = page.read()
        print('Date:', data.decode('utf-8'))
    j = requests.get(url)
    print(j.json())

URL = 'https://query.yahooapis.com/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20%3D%202151330&format=json'
data = fetch_data(URL)
#print(data)
