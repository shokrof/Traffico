import sys
from googleTrafficCrawler import googleTrafficCrawler
from DatabaseConnectorCouchDb import DatabaseConnectorCouchDb
from BugNotifierBugSnag import  BugNotifierBugSnag
from Engine import Engine
def load_CONFIG():
    res=dict(map(lambda x:x.strip().split("="),\
                 filter(lambda x:x[0]!='#' and x.strip()!="",file("CONFIG").readlines())))
    return res

CONFIG=load_CONFIG()
def main(argv):
    db=DatabaseConnectorCouchDb()
    Curr_Engine=Engine(db)
    g=googleTrafficCrawler(CONFIG['GOOGLE_API_KEY'],CONFIG['START_LOC'],CONFIG['END_LOC'])
    Curr_Engine.addCrawler(g)
    Notifiers=[]
    if "Exception_Notifier_api_key" in CONFIG and CONFIG["Exception_Notifier_api_key"]!='':
        Notifiers.append(BugNotifierBugSnag(CONFIG["Exception_Notifier_api_key"]))    
    try:
        Curr_Engine.run()
    except Exception as e:
        map(lambda x:x.notify(e),Notifiers)

if __name__ == "__main__":
    main(sys.argv[1:])
