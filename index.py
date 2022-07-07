from datetime import datetime
import web
import threading
from window_app import index_file

def worker():
    urls = (
        '/',                 'mvc.controllers.index.Index',
        '/total-ventas',     'mvc.controllers.index.Totalventas',
        
        '/api-total-ventas', 'mvc.controllers.api.ApiTotalVentas',
        '/sqlite',           'mvc.controllers.sqlite.Sqlite',
        '/(.*)',             'mvc.controllers.index.Other',
    )
    app = web.application(urls, globals())
    if __name__ == "__main__":
        app.run()


t = threading.Thread(target=worker, args=())
t.daemon = True
t.start()




app = index_file.App()
app.init_app()

