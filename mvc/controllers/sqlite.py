import web
# import simplejson as json
import json
import sqlite3
from data_base import internal
from datetime import datetime

class create_dict(dict): 
    def __init__(self): 
        self = dict() 
     
    def add(self, key, value): 
        self[key] = value

class Sqlite:
    def GET(self):

        connSQLITE = sqlite3.connect('testDB.db') # timeout=99999000.0
        cursor = connSQLITE.cursor()

        try:    
            cursor.execute("CREATE TABLE statistic (id INTEGER PRIMARY KEY, __rows__created REAL)")
            connSQLITE.commit(); cursor.execute("INSERT INTO statistic (id, __rows__created) VALUES (?,?)", (None, 1)); connSQLITE.commit()
            print("table statistic created")
        except: print("table statistic EXISTS")    

        try:
            cursor.execute("DELETE FROM delegado");  connSQLITE.commit()
        except:  print("Nothing to deleted delegado")
        try:
           cursor.execute("DROP TABLE delegado"); connSQLITE.commit(); print(" DROPPED delegado")
        except: print("Nothing dropped") 
        try:    
            cursor.execute("CREATE TABLE delegado (__erp TEXT, __nombre TEXT, __state TEXT, __delegado__id REAL)")
            connSQLITE.commit(); print("CREATED delegado")
        except: print("nothing created delegado")

        # return 1;

        allRowsDeleted = False
        try:
            cursor.execute("DELETE FROM ventas")
            connSQLITE.commit(); print(" Deleted all rows "); allRowsDeleted = True 
        except:  print("Nothing to deleted ventas") 

        try:
            if allRowsDeleted == False:
                cursor.execute("DROP TABLE ventas")
                connSQLITE.commit(); print(" DROPPED ")
        except: print("Nothing dropped")    
        try:    
            if allRowsDeleted == False:
                cursor.execute("CREATE TABLE ventas (unidades REAL, pvp REAL, precio REAL, tarifa REAL, __articulo__id REAL, __articulo____erp TEXT, __articulo____descripcion TEXT, __familia__id TEXT, __familia____descripcion TEXT, lote TEXT, precio_pvp REAL, subtotal REAL, subtotal_con_rappel REAL, precio_coste REAL, rappel REAL, porc_rappel REAL, dto REAL, dto_com REAL, dto_pp REAL, contador REAL, total REAL, peso REAL, delegado_id TEXT, delegado__erp TEXT, fecha TEXT, cliente_id TEXT, cliente_erp TEXT, cliente TEXT, pedido TEXT, albaran TEXT, factura TEXT)")
                connSQLITE.commit(); print(" CREATED ")
        except: print("nothing created")


        mydb = internal.InternalConnect().start_database_connect()
        mycursor = mydb.cursor()


        sql = "SELECT __erp, __nombre, __state, id FROM delegado"
        mycursor.execute(sql)
        delegados = mycursor.fetchall() 
        for delegado in delegados:
            i = {}
            i['__erp']          = str(delegado[0] or '')
            i['__nombre']       = str(delegado[1] or '')
            i['__state']        = str(delegado[2] or '')
            i['__delegado__id'] = float(delegado[3] or 0)
            sql = "INSERT INTO delegado (__erp, __nombre, __state, __delegado__id) VALUES (?,?,?,?)"
            val = (i['__erp'], i['__nombre'], i['__state'], i['__delegado__id'])
            cursor.execute(sql, val)
            connSQLITE.commit()

        sql = "SELECT * FROM ventas_delegado_cliente_fecha"

        mycursor.execute(sql)
        result = mycursor.fetchall() 
        mycursor.close()
        mydb.close()
        
        y = 0

        for res in result:
            i = {}
            i['unidades'] = float(res[0] or 0)
            i['pvp']      = float(res[1] or 0)
            i['precio']   = float(res[2] or 0)
            i['tarifa']   = float(res[3] or 0)
            i['__articulo__id'] = float(res[4])
            
            i['__articulo____erp'] = str(res[5] or '')
            i['__articulo____descripcion'] = str(res[6] or '')
            i['__familia__id'] = str(res[7] or '')
            i['__familia____descripcion'] = str(res[8] or '')
            i['lote'] = str(res[9] or '')
            
            i['precio_pvp'] = float(res[10] or 0)
            i['subtotal'] = float(res[11] or 0)
            i['subtotal_con_rappel'] = float(res[12] or 0)
            i['precio_coste'] = float(res[13] or 0)
            i['rappel'] = float(res[14] or 0)
            
            i['porc_rappel'] = float(res[15] or 0)
            i['dto'] = float(res[16] or 0)
            i['dto_com'] = float(res[17] or 0)
            i['dto_pp'] = float(res[18] or 0)
            i['contador'] = str(res[19] or '')
            
            i['total'] = float(res[20] or 0)
            i['peso'] = float(res[21] or 0)
            i['delegado_id'] = str(res[22] or '')
            i['delegado__erp'] = str(res[23] or 0)
            i['fecha'] = str(res[24] or '')
            
            i['cliente_id'] = str(res[25] or '')
            i['cliente_erp'] = str(res[26] or '')
            i['cliente'] = str(res[27] or '')
            i['pedido'] = str(res[28] or '')
            i['albaran'] = str(res[29] or '')
            
            i['factura'] = str(res[30] or '')
            # resLista.append(emptyDic)

            sql = "INSERT INTO ventas (unidades,     pvp,     precio,     tarifa,      __articulo__id,      __articulo____erp,      __articulo____descripcion,     __familia__id,     __familia____descripcion,     lote,     precio_pvp,     subtotal,     subtotal_con_rappel,     precio_coste,     rappel,     porc_rappel,     dto,     dto_com,     dto_pp,     contador,     total,     peso,     delegado_id,     delegado__erp,     fecha,     cliente_id,     cliente_erp,     cliente,     pedido,     albaran,     factura ) VALUES (?,?,?,?,?,  ?,?,?,?,?,  ?,?,?,?,?,  ?,?,?,?,?,  ?,?,?,?,?,  ?,?,?,?,?,  ?)"
            val =                  (i['unidades'],i['pvp'],i['precio'],i['tarifa'], i['__articulo__id'], i['__articulo____erp'], i['__articulo____descripcion'],i['__familia__id'],i['__familia____descripcion'],i['lote'],i['precio_pvp'],i['subtotal'],i['subtotal_con_rappel'],i['precio_coste'],i['rappel'],i['porc_rappel'],i['dto'],i['dto_com'],i['dto_pp'],i['contador'],i['total'],i['peso'],i['delegado_id'],i['delegado__erp'],i['fecha'],i['cliente_id'],i['cliente_erp'],i['cliente'],i['pedido'],i['albaran'],i['factura'])
            cursor.execute(sql, val)
            connSQLITE.commit()
            y = y + 1
            # if y > 5:
            #     break


        
        cursor.execute("SELECT __rows__created FROM statistic WHERE id = 1 LIMIT 1")   
        objStatisticNumRows = cursor.fetchall()[0][0] 
        if int(objStatisticNumRows or 0) <= y:
            cursor.execute("UPDATE statistic set __rows__created = " + str(y) + " WHERE id = 1"); connSQLITE.commit()
        else:
            return '<h1>Error, intente otra vez</h1>'    
        
        cursor.close()
        connSQLITE.close()
        web.header('Content-Type', 'text/html')
        return '<a href="/">Inicio</a><b><h3>Base datos actualizada: ' + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '</h3><br>'+str(y)+' lineas'

        web.header('Content-Type', 'application/json')
        result = {'a': 'b1'}
        return json.dumps(result)