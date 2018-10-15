#coding:utf-8
import re
from bs4 import BeautifulSoup
import urllib
class htmlParser(object):
    def get_new_url(self, new_url,soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r"/2018/"))
        for link in links:
            page_url = link['href']
            new_full_url = urllib.parse.urljoin(new_url, page_url)
            new_urls.add(new_full_url)
    def get_new_data(self, new_url, soup):
        res_data = {}
        res_data['url'] = new_url
        title = {'id':'content'}
        title_node = soup.find('div', attrs=title).find('h1')
        res_data['title'] = title_node.get_text()
        summary = {'id':'article_content'}
        summary_node = soup.find('div', attrs=summary).find_all_next(text=True)
        if summary_node is None:
            return
        res_data['summary'] = summary_node.get_text()
        return res_data

    def htmlparser(self, new_url, html_cont):
        if new_url is None or html_cont is None:
            return
        soup = BeautifulSoup('html_cont', "html.parser", from_encoding='utf-8')
        new_urls = self.get_new_url(new_url,soup)
        new_data = self.get_new_data(new_url, soup)
        return new_urls,new_data