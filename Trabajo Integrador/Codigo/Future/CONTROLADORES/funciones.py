from CONTROLADORES.DBFuture import DAO
from colorama import  init, Fore, Back, Style

dao= DAO()

def listarPropiedades(propiedad):
    print("+----+------------------------------+------------------------------+------------------------------+-------------------------+------------+--------------------+---------------+")    
    color_verde()
    print("| Id.| Propiedad                    | Direccion                    | Contacto                     | Propietario             | Estado     | Tipo Propiedad     | Operatoria    |")  
    color_blanco()
    print("+----+------------------------------+------------------------------+------------------------------+-------------------------+------------+--------------------+---------------+")   
    con = 0
    for prop in propiedad:
        
        cadena = "|{:>4}|{:<30}|{:<30}|{:<30}|{:<25}|{:<12}|{:<20}|{:<15}|".format(prop[0], prop[5], prop[6], prop[7], prop[8], prop[9], prop[10], prop[11])
        print(cadena)
        print("+----+------------------------------+------------------------------+------------------------------+-------------------------+------------+--------------------+---------------+")
        con = con + 1
        if con == 20:
            pausa = input("\nPresione una tecla p/Continuar: ")
            con = 1
    if con == 0:
        print("No se encontraron propiedades ...")

def listarTiposPropiedades(tipo):
    print(" ")
    print("+----+------------------------------+")    
    print("| Id.| Tipos Propiedades            |")  
    print("+----+------------------------------+")    
    for tip in tipo:
       # datos = "{0}. Id_Tipo: {1} | Nombre_Tipo: {2})"
       # print(datos.format(contador, tip[0], tip[1]))
       # contador = contador + 1   
        cadena = "|{:>4}|{:<30}|".format(tip[0], tip[1])
        print(cadena)
    print("+----+------------------------------+")   
    print(" ")

def listarEstadosPropiedades(estado):
    print(" ")
    print("+----+------------------------------+")    
    print("| Id.| Estados Propiedades          |")  
    print("+----+------------------------------+")       
    for est in estado:      
        cadena = "|{:>4}|{:<30}|".format(est[0], est[1])
        print(cadena)
    print("+----+------------------------------+")   
    print(" ")  

def listarPropietariosPropiedades(propietario):
    print(" ")
    print("+----+------------------------------+")    
    print("| Id.| Propietarios                 |")  
    print("+----+------------------------------+")       
    for pro in propietario:     
        cadena = "|{:>4}|{:<30}|".format(pro[0], pro[1])
        print(cadena)
    print("+----+------------------------------+")   
    print(" ")   

def listarOperatoriaComercialPropiedades(operatoriaComercial):  
    print(" ")
    print("+----+------------------------------+")    
    print("| Id.| Operatoria Comercial         |")  
    print("+----+------------------------------+")
    for opc in operatoriaComercial:
        cadena = "|{:>4}|{:<30}|".format(opc[0], opc[1])
        print(cadena)
    print("+----+------------------------------+")   
    print(" ")           

# Metodo para armar insercion en tabla propiedades
def pedirDatosRegistro():
    propiedad = None
    continuar = True
    tipoCorrecto = False
    while(not tipoCorrecto):
        tipo = dao.listarTipo()
        listarTiposPropiedades(tipo)
        idTipo = input("Seleccione un tipo de propiedad [0 P/Salir] : ")
        try:
            idTipo = int(idTipo)
            if idTipo == 0:
                continuar = False
                break
            else:
                for tip in tipo:
                    if tip[0] == idTipo:
                        tipoCorrecto = True
                        break

            if(tipoCorrecto == False):
                color_rojo()
                continua = input('\nTipo Ingresado Incorrecto... Presione una tecla p/continuar...')
                color_blanco
                continue
                
        except ValueError:
            mensaje_incorrecto()
            continue 

    if (continuar):      

        estadossCorrecto = False
        conDatos = False
        while(not estadossCorrecto):
            estado = dao.listarEstado()

            listarEstadosPropiedades(estado)
            idestado = input("Seleccione un estado de propiedad: ")  
            try:
                idestado = int(idestado)
                for est in estado:
                    if est[0]==idestado:
                        conDatos = True
                        break

                if(conDatos==False):
                    color_rojo()
                    continua = input('\nEstado Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                    color_blanco()
                    continue
                else:
                    estadossCorrecto = True
            except ValueError:
                mensaje_incorrecto()
                continue    

        operatoriaCorrecto = False
        conDatos = False
        while(not operatoriaCorrecto):
            operatoria = dao.listarOperatoriaComercial()

            listarOperatoriaComercialPropiedades(operatoria)
            idoperatoria = input("Seleccione una Operatoria Comercial de propiedad: ")
            try:
                idoperatoria = int(idoperatoria)
                for ope in operatoria:
                    if ope[0]==idoperatoria:
                        conDatos = True
                        break
                
                if (conDatos==False):
                    color_rojo()
                    continua = input('\nOperatoria Ingresada Incorrecta... Presione una tecla p/continuar...\n')
                    color_blanco()
                    continue
                else:
                    operatoriaCorrecto = True
            except ValueError:
                mensaje_incorrecto()
                continue          

        propietariosCorrecto = False
        while(not propietariosCorrecto):
            propietario = dao.listarPropietario()

            listarPropietariosPropiedades(propietario)
            idpropietario = input("Seleccione un propietario de propiedad: ")   
            try:
                idpropietario = int(idpropietario)
                for prop in propietario:
                    if prop[0]==idpropietario:
                        conDatos = True
                        break

                if (conDatos==False):
                    color_rojo()
                    continua = input('\nPropietario Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                    color_blanco()
                    continue
                else:
                    propietariosCorrecto = True
            except ValueError:
                mensaje_incorrecto()
                continue      

        nombreCorrecto = False
        while(not nombreCorrecto):       
            nombre = str(input("Ingrese Nombre de la propiedad: "))   
            if(nombre==""):
                continua = input("Debe ingresar un nombre para la propiedad.")
                continue
            else:
                nombreCorrecto = True

        direccionCorrecto = False
        while(not direccionCorrecto):       
            direccion = str(input("Ingrese direccion de la propiedad: "))   
            if(direccion==""):
                continua = input("Debe ingresar una direccion para la propiedad.")
                continue
            else:
                direccionCorrecto = True

        contactoCorrecto = False
        while(not contactoCorrecto):       
            contacto = str(input("Ingrese contacto de la propiedad: "))   
            if(contacto==""):
                continua = input("Debe ingresar un contacto para la propiedad.")
                continue
            else:
                contactoCorrecto = True                

        propiedad = None
        confirma = str(input('\n Confirma los datos ingresados S/N : '))
        confirma = confirma.upper()
        if (confirma == 'S'):
            propiedad = (idTipo,idestado,idoperatoria,idpropietario,nombre,direccion,contacto)

        return propiedad  

# Metodo para armar modificacion en tabla propiedades
def modificarPropiedad(propiedades):
    propiedad=listarPropiedades(propiedades)
    existeIdprop = False  
    propi= None  
    
    IdpropEditar = input("\nIngrese el Id de la propiedad a modificar [0 P/Salir] : ")   
    try:
        IdpropEditar = int(IdpropEditar)
        while(IdpropEditar != 0):
            for prop in propiedades:
                if prop[0] == IdpropEditar:
                    existeIdprop = True
                    propi= prop
                    break

            if existeIdprop == False:
                IdpropEditar = 0
                continua = input('\nId Propiedad inexistente... Presione una tecla p/continuar...\n')
                continue 
            else:
                color_amarillo()
                print("\n+----+------------------------------+------------------------------+------------------------------+-------------------------+------------+--------------------+---------------+")
                cadena = "|{:>4}|{:<30}|{:<30}|{:<30}|{:<25}|{:<12}|{:<20}|{:<15}|".format(prop[0], prop[5], prop[6], prop[7], prop[8], prop[9], prop[10], prop[11])
                print(cadena)           
                print("+----+------------------------------+------------------------------+------------------------------+-------------------------+------------+--------------------+---------------+\n")          
                color_blanco()
                nombreCorrecto = False
                while(not nombreCorrecto):       
                    nombre = str(input("Ingrese Nombre de la propiedad a editar : "))   
                    if(nombre==""):
                        continua = input("\nDebe ingresar un nombre para la propiedad.\n")
                        continue
                    else:
                        nombreCorrecto = True

                direccionCorrecto = False
                while(not direccionCorrecto):       
                    direccion = str(input("Ingrese direccion de la propiedad a editar: "))   
                    if(direccion==""):
                        continua = input("\nDebe ingresar una direccion para la propiedad.\n")
                        continue
                    else:
                        direccionCorrecto = True

                contactoCorrecto = False
                while(not contactoCorrecto):       
                    contacto = str(input("Ingrese contacto de la propiedad a editar: "))   
                    if(contacto==""):
                        continua = input("\nDebe ingresar un contacto para la propiedad.\n")
                        continue
                    else:
                        contactoCorrecto = True               
            
                tipoCorrecto = False
                conDatos = False
                while(not tipoCorrecto):
                    tipo = dao.listarTipo()
                    listarTiposPropiedades(tipo)
                    idTipo = input("Seleccione un tipo de propiedad: ")
                    try:
                        idTipo = int(idTipo)
                        for tip in tipo:
                            if tip[0] == idTipo:
                                conDatos = True
                                break

                        if(conDatos == False):
                            color_rojo()
                            continua = input('\nTipo Ingresado Incorrecto... Presione una tecla p/continuar...')
                            color_blanco()
                            continue
                        else:
                            tipoCorrecto = True
                            
                    except ValueError:
                        mensaje_incorrecto()
                        continue   

                estadossCorrecto = False
                conDatos = False
                while(not estadossCorrecto):
                    estado = dao.listarEstado()

                    listarEstadosPropiedades(estado)
                    idestado = input("Seleccione un estado de propiedad: ")  
                    try:
                        idestado = int(idestado)
                        for est in estado:
                            if est[0]==idestado:
                                conDatos = True
                                break

                        if(conDatos==False):
                            color_rojo()
                            continua = input('\nEstado Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                            color_blanco()
                            continue
                        else:
                            estadossCorrecto = True
                    except ValueError:
                        mensaje_incorrecto()
                        continue     

                operatoriaCorrecto = False
                conDatos = False
                while(not operatoriaCorrecto):
                    operatoria = dao.listarOperatoriaComercial()

                    listarOperatoriaComercialPropiedades(operatoria)
                    idoperatoria = input("Seleccione una OperatoriaComercial de propiedad: ")
                    try:
                        idoperatoria = int(idoperatoria)
                        for ope in operatoria:
                            if ope[0]==idoperatoria:
                                conDatos = True
                                break
                        
                        if (conDatos==False):
                            color_rojo()
                            continua = input('\nOperatoria Ingresada Incorrecta... Presione una tecla p/continuar...\n')
                            color_blanco()
                            continue
                        else:
                            operatoriaCorrecto = True
                    except ValueError:
                        mensaje_incorrecto()
                        continue          

                propietariosCorrecto = False
                conDatos = False
                while(not propietariosCorrecto):
                    propietario = dao.listarPropietario()

                    listarPropietariosPropiedades(propietario)
                    idpropietario = input("Seleccione un propietario de propiedad: ")   
                    try:
                        idpropietario = int(idpropietario)
                        for prop in propietario:
                            if prop[0]==idpropietario:
                                conDatos = True
                                break

                        if (conDatos==False):
                            color_rojo()
                            continua = input('\nPropietario Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                            color_blanco()
                            continue
                        else:
                            propietariosCorrecto = True
                    except ValueError:
                        mensaje_incorrecto()
                        continue       
                
                propiedad = None
                confirma = str(input('\n Confirma los datos modificados S/N : '))
                if (confirma == 'S' or confirma == 's'):
                    propiedad = (idTipo, idestado, idoperatoria, idpropietario, nombre, direccion, contacto, IdpropEditar)

                return propiedad

    except ValueError:
        propiedad = None
        mensaje_incorrecto()

def pedirDatosEliminacion(propiedades):
    propiedad=listarPropiedades(propiedades)
    existeIdprop = False  
    propi= None  
    
    IdpropEditar = input("\n Ingrese el Id de la propiedad a eliminar [0 P/Salir] : ")
    try:
        IdpropEditar = int(IdpropEditar)
        while(IdpropEditar !=0):   
            for prop in propiedades:
                if prop[0] == IdpropEditar:
                    propi= prop
                    existeIdprop = True
                    break            

            if existeIdprop == False:
                IdpropEditar =0
                color_rojo()
                continua = input('\nId Propiedad inexistente... Presione una tecla p/continuar...\n')
                color_blanco()
                continue
            else:        
                color_amarillo()
                print("\n+----+------------------------------+------------------------------+------------------------------+-------------------------+------------+--------------------+---------------+")
                cadena = "|{:>4}|{:<30}|{:<30}|{:<30}|{:<25}|{:<12}|{:<20}|{:<15}|".format(prop[0], prop[5], prop[6], prop[7], prop[8], prop[9], prop[10], prop[11])
                print(cadena)           
                print("+----+------------------------------+------------------------------+------------------------------+-------------------------+------------+--------------------+---------------+\n")          
                color_blanco()             
                               
                continua = str(input("\nConfirmar la eliminacion de la propiedad S/N ? : "))
                if (continua =="S" or continua == "s"):   
                    return IdpropEditar
                else:
                    IdpropEditar = 0
                    return IdpropEditar

    except ValueError:
        mensaje_incorrecto()

def color_blanco():
    try:
        init()
        print(Fore.WHITE,end="")
    except  (ValueError) as e:
            print("Ocurri?? un error cargar el color BLANCO ", e)
    return

def color_verde():
    try:
        init()
        print(Fore.GREEN,end="")
    except  (ValueError) as e:
            print("Ocurri?? un error cargar el color VERDE ", e)
    return

def color_rojo():
    try:
        init()
        print(Fore.RED,end="")
    except  (ValueError) as e:
            print("Ocurri?? un error cargar el color ROJO ", e)
    return

def color_amarillo():
    try:
        init()
        print(Fore.YELLOW,end="")
    except  (ValueError) as e:
            print("Ocurri?? un error cargar el color AMARILLO ", e)
    return

def mensaje_incorrecto():
    try:
        color_rojo()
        continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n') 
        color_blanco()
    except  (ValueError) as e:
            print("Ocurri?? un error cargar el color ROJO ", e)
    return

def pausa():
    pausa = input("\nPresione una tecla p/Finalizar: ")


