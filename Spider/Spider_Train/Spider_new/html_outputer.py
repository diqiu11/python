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
        for date in self.datas:
            pass

        file.write('</body>')
        file.write('</html>')
        file.close()
