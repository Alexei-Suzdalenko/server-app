from datetime import datetime

import web
import threading
from window_app import index_file, server_file

def worker():
    urls = ('/(.*)', 'hello')
    app = web.application(urls, globals())
    if __name__ == "__main__":
        app.run()

class hello:
    def GET(self, name):
        render = web.template.render('templates/')
        return render
       #  if name:
       #      return "say <em> hello </em> to $name "
       #  else:
       #      return "<em> Else index.py Hello </em>, world!"
       # if not name:
       #      raise web.seeother('static/index.html')
       # else:
       #      # pyDict = {'one':1,'two':2}
       #      # web.header('Content-Type', 'application/json')
       #      # return json.dumps(pyDict)
       #      return "<html>template name:" + name + "</html>"



t = threading.Thread(target=worker, args=())
t.daemon = True
t.start()

app = index_file.App()
app.init_app()

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
