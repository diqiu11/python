#coding:utf-8
class htmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_newdate(self,date):
        if date is None:
            return
        self.datas.append(date)

    def htmloutput(self):
        file = open('gjgwy.html', 'w', encoding='utf-8')
        file.write('<html>')
        file.write('<body>')
        for data in self.datas:
            file.write('<h>%s</h1>' %  data['title'])
            file.write('<p>%s</p>' % data['summary'])

        file.write('</body>')
        file.write('</html>')
        file.close()
