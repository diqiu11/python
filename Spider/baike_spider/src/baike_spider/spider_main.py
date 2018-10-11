#coding:utf-8


from baike_spider import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):#各个器具的作用要时刻清楚，记得
    def __init__(self):  # 在此声明初始化其他的类和方法，以便在下方调用，因为，这是一个总的大纲
        self.urls = url_manager.UrlManager()  # url管理器
        self.downloader = html_downloader.HtmlDownloader()  # 下载器中创建下载类
        self.parser = html_parser.HtmlParser()  # 解析器
        self.outputer = html_outputer.HtmlOutputer()  # 输出器

    def craw(self, root_url):   #定义craw的方法，并引进对应的参数root_url
        count = 1           
        self.urls.add_new_url(root_url)     #urls应该是一个存取url的地方，此刻有一个方法add入口的url
        while self.urls.has_new_url():      #当urls整个url集合里有新的url时循环，又一个方法
            try:            #应该考虑到会有异常出现，特别在出口主class中，要注意设置异常检测
                new_url = self.urls.get_new_url()   #从urls中那到新进入的url
                print('craw %d : %s' % (count, new_url))#打印craw的数量和对应的url是什么
                html_cont = self.downloader.download(new_url)#downloader中的调用download方法，并有一个url参数，是为下载的网页
                #解析器调用parse方法解析url对应的下载内容并存放在ulrs和data中
                new_urls, new_data = self.parser.parse(new_url, html_cont)
                #将此url回收到urls中
                self.urls.add_new_urls(new_urls)
                #输出器中收集这些数据
                self.outputer.collect_data(new_data)

                if count >= 100:    #设置爬取得网页数量
                    break

                count += 1

            except Exception as e:
                print(str(e))
                # 抛出异常

            self.outputer.output_html()         #输出器输出这些数据


if __name__ == '__main__':      #初始化，有一个main函数的出口，一般在这里进行调用
    root_url = 'https://baike.baidu.com/item/%E8%8A%88%E6%9C%88%E4%BC%A0/73703?fr=aladdin'
    obj_spider = SpiderMain()   #将spidermain类保存进obj_spider中，方便调用，像java的new对象
    obj_spider.craw(root_url)   #调用spidermain中的方法并保存入参数
