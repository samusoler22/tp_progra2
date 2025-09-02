def nuevo_usuario():
    '''Funcion para crear nuevo usuario'''
    def validar_usuario_unico(usuario):
        '''Funcion para validar que el usuario ingresado sea unico'''
        pass
    def validar_contraseña_usuario(contraseña):
        '''Funcion para validar que la contraseña ingresada cumpla los requisitos de seguridad:
            Una letra mayuscula, Al menos un numero, Minimo de 8 caracteres'''
        pass
    def guardar_nuevo_usuario(datos_usuario):
        '''Funcion para guardar los datos del nuevo usuario en la base de datos'''
        pass

    print("#### GENERAR NUEVO USUARIO ####")
    nombre_personal = input("Por favor ingrese nombre completo")
    dni = input("Por favor ingrese numero de DNI")
    usuario = input("Por favor ingrese nombre de usuario")
    contraseña = input('''Por favor ingrese una contraseña que cumpla las siguientes caractesticas:
                            \n - Una letra mayuscula
                            \n - Al menos un numero 
                            \n - Minimo de 8 caracteres''')
    email = input("Ingrese un correo electronico")

    #Guardar los datos en un Dictionario (Payload) y luego subirlos a un excel (DB)

def resumen_cuenta():
    '''Funcion para descargar resumen de cuenta'''


def main():
    '''Funcion principal que ejecuta el codigo'''

main()