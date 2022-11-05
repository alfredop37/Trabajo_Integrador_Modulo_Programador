# Programa main.py sistema de gestion inmobiliaria
# Issue : 9 - Alfredo Palacios

from distutils.log import error
from CONTROLADORES.DBFuture import DAO
from os import system
from CONTROLADORES import funciones
import time


def menuPrincipal(): 
    system("cls")
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            funciones.color_verde()
            print ("***********************************************************************")
            print ("*                       - Inmobiliaria - Future -                     *")
            print ("***********************************************************************")
            print ("*                    Sistema de Gestión Inmobiliaria                  *")
            print ("***********************************************************************\n")    
            funciones.color_blanco()                                                             
            print ("- 1. Ingresar una nueva propiedad ")                                    
            print ("- 2. Modificar datos de propiedad ")                          
            print ("- 3. Eliminar datos de propiedad ")                      
            print ("- 4. Listar todas las propiedades ")                         
            print ("- 5. Listar propiedades disponibles para la Venta  ")                      
            print ("- 6. Listar propiedades disponibles para Alquiler   ")                 
            print ("- 7. Listar propiedades vendidas  ")                    
            print ("- 8. Listar propiedades alquiladas \n")                                                                                      
            print ("- 0. Salir  \n")   
            funciones.color_verde()                                                                                                                       
            print ("***********************************************************************")
            funciones.color_blanco()
            try:
                opcion = int(input("Seleccione una opción : "))
            except ValueError:
                funciones.mensaje_incorrecto()
                system("cls")
                continue
            if opcion > 8:
                funciones.mensaje_incorrecto()
                system("cls")
                continue
            elif opcion == 0:
                continuar = False
                funciones.color_verde()
                print("\nGracias por usar nuestro sistema!")
                funciones.color_blanco()
                dao = DAO()
                dao.desconectar()
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)
    
def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:  
        try:
            print("\n Ingresar datos de propiedad")
            print(" ===========================")
            oPropiedad=funciones.pedirDatosRegistro()           
            if not oPropiedad is None:
                dao.registrarPropiedad(oPropiedad)   
                funciones.color_verde()
                print("Propiedad registrada con exito...\n")
                funciones.color_blanco()
                time.sleep(3)
                menuPrincipal()
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))

    elif opcion == 2:
        try:
            prop = dao.listarPropiedades()
            if len(prop) > 0:
                print("\n Modificar datos de propiedad")
                print("============================")
                propi = funciones.modificarPropiedad(prop)
                if not propi is None:
                    dao.modificarPropiedad(propi)
                    funciones.color_verde()
                    print("Propiedad Modificada con exito...\n")
                    funciones.color_blanco()
                    time.sleep(3)
                    menuPrincipal()
                else:
                    print("Propiedad a modificar no encontrada...\n")
            else:
                print("No se encontraron PROPIEDADES...")
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))

    elif opcion == 3:
        try:
            prop = dao.listarPropiedades()
            if len(prop) > 0:
                print("\nEliminar datos de propiedad")
                print("===========================")
                Id_Propiedad = funciones.pedirDatosEliminacion(prop)

                if ( Id_Propiedad !=0):
                    dao.eliminarPropiedad(Id_Propiedad)
                    funciones.color_verde()
                    print("Propiedad Eliminada con exito...\n")
                    funciones.color_blanco()
                    time.sleep(3)
                    print("")
                    menuPrincipal()
                else:
                    print("Propiedad a eliminar no encontrada.....\n")
            else:
                print("No se encontraron PROPIEDADES...")
                time.sleep(3)
        except error as ex:
            print("Ocurrió un error...".format(ex))
            
    elif opcion == 4:
        try:
            propiedad = dao.listarPropiedades()
            if not propiedad is None:
                print("\nListar todas las propiedades")
                print("============================")
                funciones.listarPropiedades(propiedad)
                funciones.pausa()
#                time.sleep(3)
            else:
                print("No se encontraron PROPIEDADES...")  
                time.sleep(3)         
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))

    elif opcion == 5:
        try:
            propiedad = dao.listarPropiedadesDPV()
            if not propiedad is None:
                print("\nPropiedades disponibles para la Venta")
                print("=====================================")
                funciones.listarPropiedades(propiedad)
                funciones.pausa()
#                time.sleep(3)
            else:
                print("\nNo se encontraron PROPIEDADES para la Venta\n")  
                time.sleep(3)         
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))
    elif opcion == 6:
        try:
            propiedad = dao.listarPropiedadesDPA()
            if not propiedad is None:
                print("\n Propiedades disponibles para el Alquiler")
                print(" ========================================")
                funciones.listarPropiedades(propiedad)
                funciones.pausa()
#                time.sleep(3)
            else:
                print("\nNo se encontraron PROPIEDADES para el Alquiler\n ")  
                time.sleep(3)         
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))
    elif opcion == 7:
        try:
            propiedad = dao.listarPropiedadesVEN()
            if not propiedad is None:
                print("\nPropiedades Vendidas")
                print("====================\n")
                funciones.listarPropiedades(propiedad)
                funciones.pausa()
            else:
                print("\nNo se encontraron PROPIEDADES vendidas\n ")  
                time.sleep(3)         
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))
    elif opcion == 8:
        try:
            propiedad = dao.listarPropiedadesALQ()
            if not propiedad is None:
                print("\nPropiedades Alquiladas")
                print("======================\n")
                funciones.listarPropiedades(propiedad)
                funciones.pausa()
            else:
                print("\nNo se encontraron PROPIEDADES vendidas\n ")  
                time.sleep(3)         
        except error as ex:
            print("Ocurrió un error...{0}".format(ex))
      

# def cargarDatosPropiedad():
#        print("Elija un tipo de propiedad")       

menuPrincipal()
