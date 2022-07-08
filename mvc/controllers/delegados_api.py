import web
import simplejson as json
from datetime import datetime
import sqlite3

class DelegadosApi():
    def __init__(self):
        self.sqliteDatabase = sqlite3.connect('testDB.db')
        self.sqliteCursor = self.sqliteDatabase.cursor()
    def requestSqlite(self, query):
        self.sqliteCursor.execute(query)
        result = json.dumps(self.sqliteCursor.fetchall())
        self.stopSqlite()
        return result    
    def stopSqlite(self):
        self.sqliteCursor.close()
        self.sqliteDatabase.close() 
           
    def GET(self): 
        web.header('Content-Type', 'application/json')
        get_input = web.input(_method='get')
        print(get_input)    