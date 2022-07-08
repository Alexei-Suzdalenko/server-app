from datetime import datetime
import web
import threading
from window_app import index_file

def worker():
    urls = (
        '/',                 'mvc.controllers.index.Index',
        '/api-total-ventas', 'mvc.controllers.api.ApiTotalVentas',

        '/delegados',        'mvc.controllers.index.Delegados',   
        '/api-delegados',    'mvc.controllers.delegados_api.DelegadosApi', 
        
        
        
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

