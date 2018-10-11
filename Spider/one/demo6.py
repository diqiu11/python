'''

'''
#coding:utf-8
from urllib import request
import urllib
import re
from click._compat import raw_input

import time


class QSBK:
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        self.headers = {'User-Agent' : self.user_agent}
        self.storise = []
        self.enable = False
    
    def getPage(self,pageIndex):#download
        try:
            url = 'https://www.qiushibaike.com/article/' + str(pageIndex)
            response = request.urlopen(url, headers = self.headers)
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):#*
                print('mistake', e.reason)
                return None
    
    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print('mistake')
            return None
        pattern = re.compile('h2>(.*?)</h2.*?content.*?span>(.*?)</.*?!--.*?-->(.*?)</.*?number>(.*?)</i>')#look html
        items = re.findall(pattern, pageCode)#*
        pageStories = []
        for item in items:
            havaimg = re.search("img", item[3])
            if not havaimg:
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR, "\n", item[1]) #*
                pageStories.append([item[0].strip(), text.strip(),item[2].strip(), item[4].strip()]) #*
            return pageStories

    def loadPage(self):
        if self.enable == True:
            if len(self.storise)<2:
                pageStorise = self.getPageItems(self.pageIndex)
                if pageStorise:
                    self.storise.append(pageStorise)
                    self.pageIndex += 1
                    
    
    
    def getOneStory(self, pageStories, nowPage):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == 'Q':
                self.enable == False
                return
            print("%d  %s  %s  %s  %s" %(nowPage,story[0],story[2],story[3],story[1]))
    
    
    def start(self):        #spider_main
        print('enter or Q')
        self.enable = True
        self.loadPage()
        nowPage = 0
        while self.enable:
            if len(self.stories)>0:
                pageStories = self.stories[0]
                nowPage += 1 
                del self.stories[0]
                self.getOneStory(pageStories, nowPage)


spider = QSBK()
spider.start()