import json

'''TODO: 
    - FALTA AGREGAR: MATRICES, 
    - Crear o funcion (o no) para validar que el numero ingresado en el input este dentro de las opcioneS (menu por ejemplo)
    - '''

def cargar_db():
    '''Funcion para cargar en memoria los datos del archivo que se usa como DB optimizando los tiempos de ejecución'''
    #with open('db.json', 'r') as archivo:
    #    db_datos = json.load(archivo)
    #return db_datos

    db_datos = {
        "usuarios":{}
    }
    return db_datos

def nuevo_usuario(db_datos):
    '''Funcion para crear nuevo usuario'''
    def validar_usuario_unico(usuario):
        '''Funcion para validar que el usuario ingresado sea unico'''
        #TODO: El usuario no puede ser "salir"
        pass
    def validar_contraseña_usuario(contraseña):
        '''Funcion para validar que la contraseña ingresada cumpla los requisitos de seguridad:
            Una letra mayuscula, Al menos un numero, Minimo de 8 caracteres'''
        pass
    def validar_email(email):
        '''Funcion para validar que el correo electronico ingresado sea valido'''
        pass 
    def guardar_nuevo_usuario(datos_usuario):
        '''Funcion para guardar los datos del nuevo usuario en la base de datos'''
        pass

    print("#### GENERAR NUEVO USUARIO ####")
    nombre = input("Por favor ingrese nombre completo")
    dni = input("Por favor ingrese numero de DNI")
    nombre_usuario = input("Por favor ingrese nombre de usuario")
    contrasena = input('''Por favor ingrese una contraseña que cumpla las siguientes caractesticas:
                            \n - Una letra mayuscula
                            \n - Al menos un numero 
                            \n - Minimo de 8 caracteres''')
    email = input("Ingrese un correo electronico")
    alias = input(" Por favor ingrese un alias para su cuenta")

    usuario = {
        "nombre": nombre,
        "dni":dni,
        "nombre_usuario":nombre_usuario,
        "contrasena":contrasena,
        "email":email,
        "alias":alias,
        "transacciones": [],
        "saldo":0
    }

    db_datos["usuarios"][nombre_usuario] = usuario

def ingresar_dinero(usuario):
    '''Funcion para ingresar dinero a una cuenta'''
    pass

def realizar_transferencia(alias, monto):
    '''Funcion para realizar transferencia entre cuentas'''
    pass

def resumen_cuenta(fecha_inicio, fecha_final, categoria):
    '''Funcion para descargar resumen de cuenta'''
    pass

def log_in(db_datos):
    '''Funcion para hacer login en una cuenta'''
    print("### INICIO DE SESION ###")
    usuario_retry = 0
    while usuario_retry < 5:
        usuario = input("Ingrese nombre de usuario o 'salir' para cancelar:\n")
        if usuario == "salir":
            print("Inicio de Sesion cancelado")
            return 
        #si el usuario existe en la DB
        elif usuario in db_datos["usuarios"].keys():
            contrasena_retry = 0
            while contrasena_retry < 5:
                contrasena = input("Ingrese su contraseña:\n")
                #si la contraseña es correcta
                if contrasena == db_datos["usuarios"][usuario]['contrasena']:
                    print(f"Bienvenido {db_datos['usuarios'][usuario]['nombre']}")
                    return db_datos['usuarios'][usuario]
                #si no es correcta, lo notificamos y se repite el bucle
                else:
                    print("Contraseña Erronea, Reintente nuevamente")
                    contrasena_retry += 1
                if contrasena_retry == 5:
                    print("Cantidad maxima de intentos superado, cuenta bloqueada")
                    return
        #Si no existe, notificamos que no existe y se repite el bucle
        else:
            print(f"El Usuario {usuario} no existe, reintente nuevamente")
        print(f"Cantidad de intentos restantes ({usuario_retry}/5)")
        usuario_retry += 1

def menu():
    '''Funcion para mostrar menu'''
    opcion = int(input('''##### MENU ##### \n
    1. Ingresar dinero\n
    2. Realizar transferencia\n
    3. Resumen de cuenta\n
    4. Salir'''))
    return opcion


def main():
    '''Funcion principal que ejecuta el codigo'''
    db_datos = cargar_db()
    log_in_opcion = int(input('''Desea Crear usuario o Iniciar sesion? \n
    1. Crear Usuario\n
    2. Iniciar Sesion'''))

    if log_in_opcion == 1:
        nuevo_usuario(db_datos)
        seguir = int(input('''Desea Iniciar sesion? \n
        1. Si\n
        2. No'''))
        if seguir == 1:
            usuario = log_in(db_datos)
            if usuario == None:
                print("Gracias por usar el servicio")
                return
            
        elif seguir == 2:
            print("Gracias por usar el servicio")
            return
    elif log_in_opcion == 2:
        usuario = log_in(db_datos)
        if usuario == None:
                print("Gracias por usar el servicio")
                return


    opcion = menu()
    if opcion == 1:
        ingresar_dinero()
    elif opcion == 2:
        realizar_transferencia()
    elif opcion == 3:
        resumen_cuenta()
    elif opcion == 4:
        print("Gracias por usar el servicio")
        return
main()