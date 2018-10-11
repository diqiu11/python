#coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set()   #初始化。将新和旧的url全部存入set（）集合中
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)       #用循环将新的url放入urls中

    def has_new_url(self):
        return len(self.new_urls) != 0  #当new_urls字节不为0的时候，返回。

    def get_new_url(self):
        new_url = self.new_urls.pop()   #移除new_urls最后一个url并且返回
        self.old_urls.add(new_url)      #将上面返回的url存储到old_urls这个数组中
        return new_url                  #返回




