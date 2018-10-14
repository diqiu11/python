#coding:utf-8
class urlManager(object):
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()
    def has_new_url(self):
        return len(self.new_urls) != 0
    def add_new_urls(self,urls):
        if len(urls)==0 or urls is None:
            return
        for url in urls:
            add_new_url(url)
    def add_new_url(self,url):
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        if len(url)==0:
            return
    def get_new_url(self):
        url_ = self.new_urls.pop()
        self.old_urls.add(url_)
        return url_