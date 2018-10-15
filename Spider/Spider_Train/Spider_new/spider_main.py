#coding:utf-8
from Spider_new import html_download, html_outputer, html_parser, url_manager
class spiderMain(object):
    def __init__(self):
        self.download = html_download.HtmlDownload()
        self.manager = url_manager.urlManager()
        self.parser = html_parser.htmlParser()
        self.output = html_outputer.htmlOutput()

    def craw(self,root_url):
        num = 1
        self.manager.add_new_url(root_url)
        while self.manager.has_new_url():
            try:
                new_url = self.manager.get_new_url()
                print('爬虫数%d,所爬网页%s:'%(num, new_url))
                html_cont = self.download.download(new_url)
                new_urls, new_data = self.parser.htmlparser(new_url, html_cont)
                self.manager.add_new_urls(new_urls)
                self.output.collect_newdate(new_data)

                if num >= 500:
                    break
                num=num+1


            except Exception as e:
                print(str(e))
            self.output.htmloutput()



if __name__ == '__main__':
    root_url = 'http://www.gjgwy.org/201801/368129.html'
    spider = spiderMain()
    spider.craw(root_url)