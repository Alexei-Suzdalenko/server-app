import mysql.connector

class InternalConnect:
    @staticmethod
    def start_database_connect():
        mydb = mysql.connector.connect(host="192.168.1.7", user="usuario", password="Toshiba123", database="platform_froxa") # 126555.0
        return mydb