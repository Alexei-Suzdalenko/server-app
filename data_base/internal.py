import mysql.connector

class InternalConnect:
    @staticmethod
    def start_database_connect():
        mydb = mysql.connector.connect(host="192.168.1.131", user="usuario", password="Toshiba123", database="backend_froxa")
        return mydb