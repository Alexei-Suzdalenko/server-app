import web
import threading


class hello:
    def GET(self, name):
        if not name:
            raise web.seeother('static/index.html')
        else:
            # pyDict = {'one':1,'two':2}
            # web.header('Content-Type', 'application/json')
            # return json.dumps(pyDict)
            return "<html>" + 'test function' + "</html>"

def worker():
    urls = ('/(.*)', 'hello')
    app = web.application(urls, globals())
    if __name__ == "__main__":
        app.run()