from urllib import response
import web
import json
from data_base import connect, internal

render = web.template.render("C:\\Graficos-Froxa\\mvc\\views")

# /
class Index():
    def GET(self, ):
        return render.index() 

# /delegados    
class Delegados():
    def GET(self, ):
        return render.delegados()     

# /*
class Other():
    def __init__(self):
       pass

    def GET(self, param): 
        # web.header('Content-Type', 'application/json')
        return param  


                 