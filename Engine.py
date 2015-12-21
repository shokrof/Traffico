import datetime,time

def datetimeToJson(d):
    res={}
    res['year']=d.year
    res['day']=d.day
    res['month']=d.month
    res['hour']=d.hour
    res['minute']=d.minute
    return res

class Engine:
    def __init__(self,DataBaseConnector):
        self.DataBaseConnector=DataBaseConnector
        self.SleepTime=3600
        self.Crawlers=[]
        self.startTime=datetime.datetime.now()
    def addCrawler(self,Crawler):
        self.Crawlers.append(Crawler)
    def run(self):
        while True:
            currStat={}
            currStat['Time']=datetimeToJson(datetime.datetime.now())
            for c in self.Crawlers:
                currStat[c.name]=c.fetch()
            self.DataBaseConnector.save(currStat)
            time.sleep(self.SleepTime)
            
        
