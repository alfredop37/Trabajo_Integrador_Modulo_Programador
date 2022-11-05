# Programa DBFuture.py - conexion base de datos
# Issue : 10 - Alfredo Palacios

#from multiprocessing import connection
from distutils.log import error
import mysql.connector
from mysql.connector import Error
import time

#from CLASES.Propietario import Propietario

class DAO():
    def __init__(self):
        try:
            self.connection=mysql.connector.connect(
                host='localhost',
                port=3306,
                user='root',
                password='ISPCProgramador',  #'',
                db='future'
            )            
        except Error as ex:
            print("Error al intentar la conexion: {0}".format(ex))
    
    #Desconectar BBDD   
    def desconectar(self):          
        try:
            if self.connection.is_connected():
                self.connection.close()
                print('Conexión cerrada ' +
                      time.strftime("%x") + 
                      '  ' + time.strftime("%X"))
        except mysql.connector.Error as err:
            print('Error al conectar a la Base de Datos')
            print(err)

    def listarPropiedades(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT propiedad.*, propietario.Nombre, estado.Nombre_Estado, tipo.Nombre_Tipo, operatoriacomercial.Nombre_OperatoriaComercial from propiedad INNER JOIN propietario on propietario.Id_Propietario = propiedad.Id_Propietario INNER JOIN estado on estado.Id_Estado = propiedad.Id_Estado INNER JOIN tipo on tipo.Id_Tipo = propiedad.Id_Tipo INNER JOIN operatoriacomercial on operatoriacomercial.Id_OperatoriaComercial = propiedad.Id_OperatoriaComercial ORDER BY Id_Propiedad")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")
    
                
    
    def listarTipo(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM tipo ORDER BY Id_Tipo")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")       

    def listarEstado(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM estado ORDER BY Id_Estado")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")  

    def listarPropietario(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM propietario")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")       

    def listarOperatoriaComercial(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                query.execute("SELECT * FROM operatoriacomercial ORDER BY Id_OperatoriaComercial")
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")                  

    def registrarPropiedad(self, Propiedad):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "INSERT INTO propiedad (Id_Tipo, Id_Estado, Id_OperatoriaComercial,Id_Propietario,Nombre,Direccion,Contacto) VALUES ('{0}', '{1}', '{2}','{3}','{4}','{5}','{6}')"
                cursor.execute(sql.format(Propiedad[0], Propiedad[1], Propiedad[2],Propiedad[3],Propiedad[4],Propiedad[5],Propiedad[6]))
                self.connection.commit()
                print("CARGANDO...\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))        


    def modificarPropiedad(self, propiedad):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()

                sql = "UPDATE propiedad SET Id_Tipo = '{0}', Id_Estado = '{1}', Id_OperatoriaComercial = '{2}', Id_Propietario = '{3}', Nombre = '{4}', Direccion = '{5}', Contacto = '{6}' WHERE Id_Propiedad = {7}"
                cursor.execute(sql.format(propiedad[0], propiedad[1], propiedad[2], propiedad[3], propiedad[4], propiedad[5], propiedad[6], propiedad[7]))

                self.connection.commit()
                print("CARGANDO...\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))
                
    def eliminarPropiedad(self, Id_Propiedad):        
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                sql = "DELETE FROM propiedad WHERE Id_Propiedad = '{0}'"
                cursor.execute(sql.format(Id_Propiedad))
                self.connection.commit()
            except Error as ex:
                print("Error al intentar la conexión: {0}\n".format(ex))  

    # Metodo para buscar todoas las propiedades que estan a la Venta
    def listarPropiedadesDPV(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                sql = "SELECT propiedad.*, propietario.Nombre, estado.Nombre_Estado, tipo.Nombre_Tipo, operatoriacomercial.Nombre_OperatoriaComercial "
                sql = sql + " from propiedad INNER JOIN propietario on propietario.Id_Propietario = propiedad.Id_Propietario INNER JOIN estado on estado.Id_Estado = propiedad.Id_Estado "
                sql = sql + " INNER JOIN tipo on tipo.Id_Tipo = propiedad.Id_Tipo INNER JOIN operatoriacomercial on operatoriacomercial.Id_OperatoriaComercial = propiedad.Id_OperatoriaComercial "
                sql = sql + " WHERE estado.Nombre_Estado like 'Venta' and operatoriacomercial.Nombre_OperatoriaComercial LIKE 'Pendiente' "
                sql = sql + " ORDER BY  propiedad.Nombre ASC"
                query.execute(sql)
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}\n".format(ex))        
        else:
            print("error")

    # Metodo para buscar todoas las propiedades que estan en Alquiler
    def listarPropiedadesDPA(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                sql = "SELECT propiedad.*, propietario.Nombre, estado.Nombre_Estado, tipo.Nombre_Tipo, operatoriacomercial.Nombre_OperatoriaComercial "
                sql = sql + " from propiedad INNER JOIN propietario on propietario.Id_Propietario = propiedad.Id_Propietario INNER JOIN estado on estado.Id_Estado = propiedad.Id_Estado "
                sql = sql + " INNER JOIN tipo on tipo.Id_Tipo = propiedad.Id_Tipo INNER JOIN operatoriacomercial on operatoriacomercial.Id_OperatoriaComercial = propiedad.Id_OperatoriaComercial "
                sql = sql + " WHERE estado.Nombre_Estado like 'Alquiler' and operatoriacomercial.Nombre_OperatoriaComercial LIKE 'Pendiente' "
                sql = sql + " ORDER BY  propiedad.Nombre ASC"
                query.execute(sql)
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")

    # Metodo que permite buscar en la base todaas las propiedades que estando en estado de Venta
    # fueron vendidas
    def listarPropiedadesVEN(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                sql = "SELECT propiedad.*, propietario.Nombre, estado.Nombre_Estado, tipo.Nombre_Tipo, operatoriacomercial.Nombre_OperatoriaComercial "
                sql = sql + " from propiedad INNER JOIN propietario on propietario.Id_Propietario = propiedad.Id_Propietario INNER JOIN estado on estado.Id_Estado = propiedad.Id_Estado "
                sql = sql + " INNER JOIN tipo on tipo.Id_Tipo = propiedad.Id_Tipo INNER JOIN operatoriacomercial on operatoriacomercial.Id_OperatoriaComercial = propiedad.Id_OperatoriaComercial "
                sql = sql + " WHERE estado.Nombre_Estado like 'Venta' and operatoriacomercial.Nombre_OperatoriaComercial LIKE 'Vendida' "
                sql = sql + " ORDER BY  propiedad.Nombre ASC"
                query.execute(sql)
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")

    # Metodo que permite buscar en la base todas las propiedades que estando en estado de Alquiler
    # se encuentra alquiladas.
    def listarPropiedadesALQ(self):
        if self.connection.is_connected():
            try:
                query=self.connection.cursor()
                sql = "SELECT propiedad.*, propietario.Nombre, estado.Nombre_Estado, tipo.Nombre_Tipo, operatoriacomercial.Nombre_OperatoriaComercial "
                sql = sql + " from propiedad INNER JOIN propietario on propietario.Id_Propietario = propiedad.Id_Propietario INNER JOIN estado on estado.Id_Estado = propiedad.Id_Estado "
                sql = sql + " INNER JOIN tipo on tipo.Id_Tipo = propiedad.Id_Tipo INNER JOIN operatoriacomercial on operatoriacomercial.Id_OperatoriaComercial = propiedad.Id_OperatoriaComercial "
                sql = sql + " WHERE estado.Nombre_Estado like 'Alquiler' and operatoriacomercial.Nombre_OperatoriaComercial LIKE 'Alquilada' "
                sql = sql + " ORDER BY  propiedad.Nombre ASC"
                query.execute(sql)
                result= query.fetchall()                
                return result
            except Error as ex:
                print("Error al intentar la conexion: {0}".format(ex))        
        else:
            print("error")