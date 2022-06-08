# Module Imports

import mysql.connector as mariadb
import sys
import os

mariadb_connection = mariadb.connect(                                           #Datos de Conexión con MariaDB
    user = "admin",
    password = "2296",
    host = "127.0.0.1",
    port = "3306"
)

create_cursor = mariadb_connection.cursor(buffered=True)


file = open("/home/ronaldo/Escritorio/BasesdeDatos2/Proyecto3/part-00000", "r")

lineas = file.readlines()
splitedLines = []

for linea in lineas:
    print(">>>>")
    print("Insertando en Tabla: Word")
    create_cursor.execute("INSERT INTO web.Word (name, amount) VALUES ( '" +  str(linea.split()[0]) + "', '" + str(linea.split()[1]) + "');")
    mariadb_connection.commit()
    create_cursor

'''
sql_insert = "INSERT INTO web.Page (name) VALUES ('Hola'); "
create_cursor.execute(sql_insert)
mariadb_connection.commit()'''