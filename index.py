import tkinter as tk
import web
import json
import threading
import sys
from class_app import classes 


p = classes.Person()
p.go_action()
sys.exit()

def worker():
    urls = ('/(.*)', 'hello')
    app = web.application(urls, globals())
    if __name__ == "__main__":
        print(app)
        app.run()
        


class hello:
    def GET(self, name):
        if not name:
            raise web.seeother('static/index.html')
        else: 
            # pyDict = {'one':1,'two':2}
            # web.header('Content-Type', 'application/json')
            # return json.dumps(pyDict)
            return "<html>" + 'test function' + "</html>" 



window = tk.Tk()
greeting = tk.Label(text='Server S.A.')
greeting.pack()

def helloCallBack():
    t = threading.Thread(target=worker, args=())
    t.daemon = True
    t.start()
    
        
  
    

buttonActivity = tk.Button(text ="Start Server", command = helloCallBack)
buttonActivity.pack()

helloCallBack()

window.mainloop()


# urls = (
#     '/(.*)', 'hello'
# )
# app = web.application(urls, globals())
# 
# class hello:
#     def GET(self, name):
#         if not name:
#             raise web.seeother('static/index.html')
#         else: 
#             # pyDict = {'one':1,'two':2}
#             # web.header('Content-Type', 'application/json')
#             # return json.dumps(pyDict)
#             return "<html>" + first_func() + "</html>" 
# 
# if __name__ == "__main__":
#     app.run()


    