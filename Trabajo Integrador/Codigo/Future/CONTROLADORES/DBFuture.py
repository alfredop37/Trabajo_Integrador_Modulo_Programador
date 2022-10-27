# Programa DBFuture.py - conexion base de datos
# Issue : 10 - Alfredo Palacios

import mysql.connector
from mysql.connector import Error

from CLASES.Propietario import Propietario

class DAO():
    def __init__(self):
        try:
            self.connection=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='',  #'',
                db='future'
            )
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))