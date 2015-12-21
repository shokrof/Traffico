from DatabaseConnector import DatabaseConnector
from couchdbkit import *

class DatabaseConnectorCouchDb(DatabaseConnector):
    def __init__(self):
        self.server = Server()
        self.db = self.server.get_or_create_db("traffico")
    def save(self,json):
        res=self.db.save_doc(json)
        if not res['ok']:
            raise Exception("CouchDb failed to save the reading")
        
