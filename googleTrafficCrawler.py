import requests,json
from Crawler import Crawler
class googleTrafficCrawler(Crawler):
    def __init__(self, api_key , location1 ,location2):
        self.api_key=api_key
        self.location1=location1
        self.location2=location2
        self.name='googleTrafficCrawler'
    def parseJson(self,j):
        resRawJson=json.loads(j)
        resJson={}
        resJson['summary']=resRawJson['routes'][0]['summary']
        resJson['duration']=resRawJson['routes'][0]['legs'][0]['duration']['value']
        resJson['distance']=resRawJson['routes'][0]['legs'][0]['distance']['value']
        resJson['steps']=[]
        for step in resRawJson['routes'][0]['legs'][0]['steps']:
            stepJson={}
            stepJson['distance']=step['distance']['value']
            stepJson['duration']=step['duration']['value']
            stepJson['summary']=step['html_instructions']
            resJson['steps'].append(stepJson)
        return resJson
        
    def fetch(self):
        base="https://maps.googleapis.com/maps/api/directions/json?origin=%s&destination=%s&key=%s"
        url1=base%(self.location1,self.location2,self.api_key)
        url2=base%(self.location2,self.location1,self.api_key)
        res1=requests.get(url1)
        res2=requests.get(url2)
        if res1.status_code != 200 or res2.status_code != 200:
            self.status='Halted'
            raise Exception("googleTrafficCrawler failed code %d,%d",res1.status_code,res2.status_code)
        resJson1=self.parseJson(res1.content)
        resJson2=self.parseJson(res2.content)
        return {"depart": resJson1,"return":resJson2}

        
