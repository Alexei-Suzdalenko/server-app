import web
import simplejson as json
from datetime import datetime
from data_base import internal
import sqlite3

class ApiTotalVentas():
    def __init__(self):
        # self.mydb =  internal.InternalConnect().start_database_connect()
        # self.mycursor = self.mydb.cursor()

        self.sqliteDatabase = sqlite3.connect('testDB.db')
        self.sqliteCursor = self.sqliteDatabase.cursor()

    def data_base_request(self, query): pass
        # self.mycursor.execute(query)
        # result = json.dumps(self.mycursor.fetchall())
        # self.stop_data_base()
        # return result

    def requestSqlite(self, query):
        self.sqliteCursor.execute(query)
        result = json.dumps(self.sqliteCursor.fetchall())
        self.stopSqlite()
        return result    

    def stopSqlite(self):
        self.sqliteCursor.close()
        self.sqliteDatabase.close()

    def stop_data_base(self): pass
        # self.mycursor.close()
        # self.mydb.close()    
            
    def GET(self): 
        web.header('Content-Type', 'application/json')
        get_input = web.input(_method='get')
        print(get_input)

        if get_input == {}:
            return json.dumps('empty')

        elif get_input.a == 'default':
            countFirstYear = 2017
            listSQL = []
            while(True): 
                try:                          
                    mesSql = " AND CAST(SUBSTRING(fecha, 6, 2) AS int) = CAST("+get_input.mes+" AS int) " # str(get_input.mes)
                except:
                    mesSql = ' '    
                try:
                    delegadoSql = " AND CAST(delegado__erp AS int) =  CAST("+get_input.delegado+" AS int) ";
                except:
                    delegadoSql = " "                            
                sql = """SELECT CAST(strftime('%Y', fecha) AS int) AS agno, ROUND(SUM(subtotal), 0) AS subtotal 
                         FROM ventas 
                         WHERE agno = """ + str(countFirstYear) + mesSql + delegadoSql + """ 
                         """ + """ GROUP BY agno """
                countFirstYear = countFirstYear + 1
                if countFirstYear > datetime.now().year: 
                    listSQL.append(sql)
                    break
                sql = sql + ' UNION '
                listSQL.append(sql)

            allChildQuery = ''
            for x in listSQL:
                allChildQuery = allChildQuery + x

            print(allChildQuery)
            myresult = self.requestSqlite(allChildQuery)           
            return myresult

        elif get_input.a == 'all': 
            sql = "SELECT COUNT(contador) FROM ventas"
            myresult = self.requestSqlite(sql)  
                   
            return myresult

        elif get_input.a == 'delegados': 
            sql = "SELECT DISTINCT delegado__erp FROM ventas ORDER BY delegado__erp ASC"
            return self.requestSqlite(sql)     

        elif get_input.a == 'familias': 
            sql = "SELECT DISTINCT __familia__id, __familia__id || '  ' || IFNULL(__familia____descripcion, '') as fam FROM ventas ORDER BY __familia__id ASC"
            return self.requestSqlite(sql)          
       

                        