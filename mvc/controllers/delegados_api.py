import web
import simplejson as json
from datetime import datetime
import sqlite3

# api-delegados?
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
        
        if get_input == {}:
            return json.dumps('empty delegados api')

        # http://192.168.1.22:8080/api-delegados?years=list_years
        elif get_input.b == 'list_years':
            sql = """SELECT DISTINCT SUBSTR(IFNULL(fecha, '0000000'), 0, 5) as __fecha FROM ventas ORDER BY __fecha ASC"""
            listYears = self.requestSqlite(sql)
            return listYears

        # http://192.168.1.22:8080/api-delegados?a=delegados
        elif get_input.b == 'delegados': 
            sql = """SELECT DISTINCT ventas.delegado_id, ventas.delegado__erp, delegado.__nombre, SUBSTR(IFNULL(fecha, '0000000'), 0, 5) as agno, CAST(IFNULL(SUM(subtotal), 0) AS int) AS subtotal
                     FROM ventas 
                     INNER JOIN delegado ON ventas.delegado_id = delegado.__delegado__id
                     
                     GROUP BY ventas.delegado_id, ventas.delegado__erp, delegado.__nombre, agno
                     ORDER BY ventas.delegado__erp, agno ASC      
                  """ # WHERE delegado.__delegado__id > 33 AND delegado.__delegado__id < 50
            return self.requestSqlite(sql) 
        

        return 0