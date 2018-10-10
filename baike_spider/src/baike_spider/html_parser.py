#coding:utf-8
import re
import urllib.parse
from bs4 import BeautifulSoup


class HtmlParser(object):
    def _get_new_urls(self, page_url, soup):
        new_urls = set()    #将新的urls存放到set集合中
        links = soup.find_all('a', href=re.compile(r"/item/"))      #匹配所有的url
        # ��ַ�б䣬���ʽ���˵���
        for link in links:
            new_url = link['href']      #将url存入
            new_full_url = urllib.parse.urljoin(page_url, new_url)      #从相对路径得到绝对路径
            # Py3���õ���ģ�����Ʊ�Ϊurllib.parse
            new_urls.add(new_full_url)      #然后增加这个绝对路径
        return new_urls     

    def _get_new_data(self, page_url, soup):
        res_data = {}

        # url
        res_data['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"> <h1></h1>
        title_node = soup.find('dd', class_='lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()

        # <div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_='lemma-summary')
        if summary_node is None:
            return
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:       #如果没有下载的新网页就返回
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')#引入beautifulsoup包
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
