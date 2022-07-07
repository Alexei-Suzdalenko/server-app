from urllib import response
import web
import json
from data_base import connect, internal

render = web.template.render("C:\\Graficos-Froxa\\mvc\\views")

class Index():
    def GET(self, ):
        return render.index() 
       
# /total-ventas       
class Totalventas():
    def __init__(self):
       pass
       #  self.work_query = connect.SqlWorkDataBase()
    def GET(self): 
        # mydb = internal.InternalConnect.start_database_connect()
        # result = self.work_query.execute_sql_total_ventas(mydb)
        return render.totalventas()

class Other():
    def __init__(self):
       pass

    def GET(self, param): 
        # web.header('Content-Type', 'application/json')
        return param  


                 