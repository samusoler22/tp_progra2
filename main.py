import json

def cargar_db():
    '''Funcion para cargar en memoria los datos del archivo que se usa como DB optimizando los tiempos de ejecución'''
    with open('db.json', 'r') as archivo:
        db_datos = json.load(archivo)
    return db_datos

def nuevo_usuario():
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
    usuario = input("Por favor ingrese nombre de usuario")
    contraseña = input('''Por favor ingrese una contraseña que cumpla las siguientes caractesticas:
                            \n - Una letra mayuscula
                            \n - Al menos un numero 
                            \n - Minimo de 8 caracteres''')
    email = input("Ingrese un correo electronico")
    alias = input(" Por favor ingrese un alias para su cuenta")

    #Guardar los datos en un Dictionario (Payload) y luego subirlos a la DB (probablemente un JSON o Excel)

def ingresar_dinero(usuario):
    '''Funcion para ingresar dinero a una cuenta'''
    pass

def realizar_transferencia(alias, monto):
    '''Funcion para realizar transferencia entre cuentas'''
    pass

def realizar_pago():
    '''Funcion para realizar un pago
    CHECK: probablemente sea lo mismo que realizar transferencia, ver si vale la pena hacer dos funciones'''
    pass

def resumen_cuenta():
    '''Funcion para descargar resumen de cuenta'''

def log_in(db_datos):
    '''Funcion para hacer login en una cuenta'''
    print("### INICIO DE SESION ###")
    while True:
        usuario = input("Ingrese nombre de usuario o 'salir' para cancelar:\n")
        if usuario == "salir":
            print("Inicio de Sesion cancelado")
            return 
        #si el usuario existe en la DB
        elif usuario in db_datos["usuarios"].keys():
            while True:
                contrasena = input("Ingrese su contraseña:\n")
                #si la contraseña es correcta
                if contrasena == db_datos["usuarios"][usuario]['contrasena']:
                    print(f"Bienvenido {db_datos['usuarios'][usuario]['nombre']}")
                    return db_datos['usuarios'][usuario]
                #si no es correcta, lo notificamos y se repite el bucle
                else:
                    print("Contraseña Erronea, Reintente nuevamente")
        #Si no existe, notificamos que no existe y se repite el bucle
        else:
            print(f"El Usuario {usuario} no existe, reintente nuevamente")

    


def main():
    '''Funcion principal que ejecuta el codigo'''
    db_datos = cargar_db()
    usuario_logeado = log_in(db_datos)

main()