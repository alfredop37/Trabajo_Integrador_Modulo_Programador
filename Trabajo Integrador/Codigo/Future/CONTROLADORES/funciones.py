from CONTROLADORES.DBFuture import DAO
dao= DAO()

def listarPropiedades(propiedad):
    print("+----+------------------------------+------------------------------+------------------------------+--------------------+------------+---------------+---------------+")    
    print("| Id.| Propiedad                    | Direccion                    | Contacto                     | Propietario        | Estado     | Tipo Propiedad| Operatoria    |")  
    print("+----+------------------------------+------------------------------+------------------------------+--------------------+------------+---------------+------------.--+")
    con = 0
    for prop in propiedad:
        
        cadena = "|{:>4}|{:<30}|{:<30}|{:<30}|{:<20}|{:<12}|{:<15}|{:<15}|".format(prop[0], prop[5], prop[6], prop[7], prop[8], prop[9], prop[10], prop[11])
        print(cadena)
        print("+----+------------------------------+------------------------------+------------------------------+--------------------+------------+---------------+-------.-------+")
        con = con + 1
        if con == 20:
            pausa = input("\nPresione una tecla p/Continuar: ")
            con = 1

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
            if(idTipo > len(tipo)):
                continua = input('\nTipo Ingresado Incorrecto... Presione una tecla p/continuar...')
                continue
            elif idTipo == 0:
                continuar = False
                print(continuar)
                break
            else:
                tipoCorrecto = True
                
        except ValueError:
            continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...')
            continue 

    if (continuar):      

        estadossCorrecto = False
        while(not estadossCorrecto):
            estado = dao.listarEstado()

            listarEstadosPropiedades(estado)
            idestado = input("Seleccione un estado de propiedad: ")  
            try:
                idestado = int(idestado)
                if(idestado<1 or idestado > len(estado)):
                    continua = input('\nEstado Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                    continue
                else:
                    estadossCorrecto = True
            except ValueError:
                continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                continue    

        operatoriaCorrecto = False
        while(not operatoriaCorrecto):
            operatoria = dao.listarOperatoriaComercial()

            listarOperatoriaComercialPropiedades(operatoria)
            idoperatoria = input("Seleccione una Operatoria Comercial de propiedad: ")
            try:
                idoperatoria = int(idoperatoria)
                if(idoperatoria<1 or idoperatoria > len(operatoria)):
                    continua = input('\nOperatoria Ingresada Incorrecta... Presione una tecla p/continuar...\n')
                    continue
                else:
                    operatoriaCorrecto = True
            except ValueError:
                continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                continue          

        propietariosCorrecto = False
        while(not propietariosCorrecto):
            propietario = dao.listarPropietario()

            listarPropietariosPropiedades(propietario)
            idpropietario = input("Seleccione un propietario de propiedad: ")   
            try:
                idpropietario = int(idpropietario)
                if(idpropietario<1 or idpropietario > len(propietario)):
                    continua = input('\nPropietario Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                    continue
                else:
                    propietariosCorrecto = True
            except ValueError:
                continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
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
                cadena = "|{:>4}|{:<30}|{:<30}|{:<30}|{:<20}|{:<12}|{:<15}|{:<15}|".format(prop[0], prop[5], prop[6], prop[7], prop[8], prop[9], prop[10], prop[11])
                print(cadena)           
                print("")            
                nombreCorrecto = False
                while(not nombreCorrecto):       
                    nombre = str(input("Ingrese Nombre de la propiedad a modificar: "))   
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
                while(not tipoCorrecto):
                    tipo = dao.listarTipo()
                    listarTiposPropiedades(tipo)
                    idTipo = input("Seleccione un tipo de propiedad: ")
                    try:
                        idTipo = int(idTipo)
                        if(idTipo<1 or idTipo > len(tipo)):
                            continua = input('\nTipo Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                            continue
                        else:
                            tipoCorrecto = True
                    except ValueError:
                        continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                        continue   
                
                estadossCorrecto = False
                while(not estadossCorrecto):
                    estado = dao.listarEstado()

                    listarEstadosPropiedades(estado)
                    idestado = input("Seleccione un estado de propiedad: ")  
                    try:
                        idestado = int(idestado)
                        if(idestado<1 or idestado > len(estado)):
                            continua = input('\nEstado Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                            continue
                        else:
                            estadossCorrecto = True
                    except ValueError:
                        continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                        continue    

                operatoriaCorrecto = False
                while(not operatoriaCorrecto):
                    operatoria = dao.listarOperatoriaComercial()

                    listarOperatoriaComercialPropiedades(operatoria)
                    idoperatoria = input("Seleccione una OperatoriaComercial de propiedad: ")
                    try:
                        idoperatoria = int(idoperatoria)
                        if(idoperatoria<1 or idoperatoria > len(operatoria)):
                            continua = input('\nOperatoria Ingresada Incorrecta... Presione una tecla p/continuar...\n')
                            continue
                        else:
                            operatoriaCorrecto = True
                    except ValueError:
                        continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                        continue          

                propietariosCorrecto = False
                while(not propietariosCorrecto):
                    propietario = dao.listarPropietario()

                    listarPropietariosPropiedades(propietario)
                    idpropietario = input("Seleccione un propietario de propiedad: ")   
                    try:
                        idpropietario = int(idpropietario)
                        if(idpropietario<1 or idpropietario > len(propietario)):
                            continua = input('\nPropietario Ingresado Incorrecto... Presione una tecla p/continuar...\n')
                            continue
                        else:
                            propietariosCorrecto = True
                    except ValueError:
                        continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
                        continue      
                
                propiedad = None
                confirma = str(input('\n Confirma los datos modificados S/N : '))
                if (confirma == 'S'):
                    propiedad = (nombre, direccion, contacto, IdpropEditar, idTipo)

                return propiedad

    except ValueError:
        propiedad = None
        continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n') 

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
                continua = input('\nId Propiedad inexistente... Presione una tecla p/continuar...\n')
                continue
            else:        
                cadena = "|{:>4}|{:<30}|{:<30}|{:<30}|{:<20}|{:<12}|{:<15}|{:<15}|".format(prop[0], prop[5], prop[6], prop[7], prop[8], prop[9], prop[10], prop[11])
                print(cadena)          
                print("")              
                continua = str(input("\nConfirmar la eliminacion de la propiedad S/N ? : "))
                if continua =="S":   
                    return IdpropEditar
                else:
                    IdpropEditar = None
                    return IdpropEditar 
    except ValueError:
        continua = input('\nOpcion incorrecta... Presione una tecla p/continuar...\n')
        
 

