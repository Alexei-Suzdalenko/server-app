import mysql.connector
from datetime import datetime
import web

class SqlWorkDataBase:
    def execute_sql_total_ventas(self, mydb): 
        # get_input = web.input(_method='get'); print(get_input.a)
        mycursor = mydb.cursor()

        countFirstYear = 2017
        listSQL = []
        while(True):
            sql = "SELECT SUM(__subtotal), YEAR(__fecha) AS agno FROM albaranventa WHERE YEAR(__fecha) = "+str(countFirstYear) + " GROUP BY agno "
            countFirstYear = countFirstYear + 1
            if countFirstYear > datetime.now().year: 
                listSQL.append(sql)
                break
            sql = sql + ' UNION '
            listSQL.append(sql)

        allChildQuery = ''
       
        for x in listSQL:
            allChildQuery = allChildQuery + x
        
        mycursor.execute(allChildQuery)
        myresult = mycursor.fetchall()

        listResult = []
        for x in myresult:
            tuplaResult = x[1], int(x[0])
            listResult.append(tuplaResult)
            
        mycursor.close()
        mydb.close()
        return listResult


