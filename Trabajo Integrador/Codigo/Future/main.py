# Programa main.py sistema de gestion inmobiliaria
# Issue : 9 - Alfredo Palacios

from CONTROLADORES.DBFuture import DAO
from os import system


def menuPrincipal(): 
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print ("***********************************************************************")
            print ("*                       - Inmobiliaria - Future -                     *")
            print ("***********************************************************************")
            print ("*                    Sistema de Gestión Inmobiliaria                  *")
            print ("***********************************************************************")
            print ("")                                                                    
            print ("- 1. Ingresar una nueva propiedad ")                                    
            print ("- 2. Modificar datos de prpopiedad            ")                          
            print ("- 3. Eliminar datos de  propiedad             ")                      
            print ("- 4. Listar todas las propiedades              ")                         
            print ("- 5. Listar propiedades disponibles para la venta  ")                      
            print ("- 6. Listar propiedades disponibles para alquiler   ")                 
            print ("- 7. Listar propiedades vendidas                    ")                    
            print ("- 8. Listar propiedades alquiladas                   ")                   
            print (" ")                                                                    
            print ("- 9. Salir  ")                                                           
            print (" ")                                                                 
            print ("***********************************************************************")
            
            try:
                opcion = int(input("Seleccione una opción : "))
            except ValueError:
                continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                system("cls")
                continue
            if opcion < 1 or opcion > 9:
                continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                system("cls")
                continue
            elif opcion == 9:
                continuar = False
                print("\nGracias por usar nuestro sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)
    
def ejecutarOpcion(opcion):
    dao = DAO()
    if opcion == 1:
        print("\nOpcion", opcion)
    elif opcion == 2:
        print("\nOpcion", opcion)
    elif opcion == 3:
        print("\nOpcion", opcion)
    elif opcion == 4:
        print("\nOpcion", opcion)
    elif opcion == 5:
        print("Opcion", opcion)
    elif opcion == 6:
        print("Opcion", opcion)
    elif opcion == 7:
        print("Opcion", opcion)    
    elif opcion == 7:
        print("Opcion", opcion)  
    elif opcion == 8:
        print("Opcion", opcion)
    else:
        print ("Opcion no valida...")

menuPrincipal()
