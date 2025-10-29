import json
from functools import reduce
from datetime import datetime

'''TODO: 
    Repartición de Tareas:
        - Agus Goldberg: 40% (5, 6) 80% (11 L, 19  , 20  , 21)
        - Samu:          40% (7, 8) 80% (12 L, 13  , 14  , 24, 25 L)
        - Benja:         40% (3, 4) 80% (9   , 15  , 16  , 22)
        - Agus Lopez:    40% (1, 2) 80% (10 L, 17 L, 18 L, 23 L)

    Ideas mejoras:
    - Quizas posibiliadad de comprar Stocks/Crypto
    - Posibilidad de agregar pagos de servicios (Agua, luz, internet, Disney etc) agregando fecha de pago
      a la data en lista y luego compara si ya es el dia de pago (un mes despues de la fecha en la DB)

    Tareas:
        Entrega 40%
        1. Agregar validaciones del nuevo usuario (Funciones creadas dentro de la funcion nuevo_usuario)
            - En la funcion "nuevo usuario" crear logica para validar los datos que ingresa el usuario.
            - Las funciones ya estan prehechas, agregar mas de ser necesario.
            LISTO

        2. Crear funcion para ingresar dinero
            - Crear logica para agregar dinero a la cuenta del usuario en la funcion "ingresar_dinero".
            - Tener en cuenta que habria que agregar una transaccion en el usuario por cada ingreso.
            - Que se agregue el ingreso al saldo del usuario.
            - IMPORTANTE: Tener en cuenta que la parte de las transacciones es una matriz.
            LISTO

        3. Crear funcion para realizar transferencia.
            - Crear logica para realizar transferencia entre cuentas dentro de la funcion "realizar_transferencia"
            - Tener en cuenta que esta funcion usa dos parametros, uno es alias porque vamos a buscar el usuario a transferir en nuestro diccionario de usuarios
            - Tener en cuenta que el monto que se transfiere se resta del saldo del usuario que transfiere y se agregan las transacciones pertinentes.
            LISTO

        4. Crear funcion para mostrar resumen de cuenta
            - Crear logica en funcion "resumen_cuenta"
            - Por defecto mostrar transacciones del mes en curso o el mes anterior (a definir)
            - Luego de mostrar resumen, crear menu para preguntar si quiere:
                1-Mostrar resumen de transacciones entre un rango de fechas
                2-Mostrar ultimos 5 transacciones (aca aplicamos slicing de la lista)
                3-Mostrar primeras 5 transacciones del mes.
            LISTO
        
        5 - Crear funcion de Control de Gastos.
            - Crear logica donde se muestre gastos total del mes y estilo de gastos basado en las etiquetas de las transacciones de egreso, ejemplo:
                "Se gasto un 20% en comida"
            LISTO
        
        6 - Crear funcion de objetivos de ahorro
            - Permitir al usuario ingresar cuanto desea ahorrar y cuando gana por su sueldo.
            - Basado en eso mostrar cuanto debe ahorrar por dia (o semana, a definir)
            - Basado en los gastos de las etiquetas de gastos donde se deberia recortar mas para cumplir la meta. Ejemplo:
                Reduciendo en x% los gastos de "comida" puees cumplir esta meta.
            LISTO
            
        7 - Crear funcion para hacer inversiones.
            - Ingresar monto a invertir y crear algoritmo que calcule la ganancia estimada.
            LISTO
        
        8 - Crear funcion para funcion de Gastos compartidos.
            - Permitir al usuario ingresar cantidad de personas a repartir el gasto
            - Ingresar Monto a pagar.
            - Mostar cuanto debe pagar cada persona.
            LISTO
        
        Entrega 80%
        9 - Añadir funcionalidad donde se crea un set con los nombres de los usuarios y al momento de crear un nuevo serio
            se verifica a partir de ese set si el usuario ya existe o no

        10 - Solicitar al crear usuario que ingrese fecha de nacimiento y guardarlo en la DB
            LISTO

        11 - Crear Funcion donde a partir de la fecha de nacimiento ya sabemos el cumpleaños del usuario, comparamos
            la fecha del dia de hoy usando datetime y en caso de que sea su cumpleaños printeamos una felicitacion al hacer login.
            LISTO
        
        12 - Implementar Datetime: Cambiar el formato de fecha anterior por valor datetime y adaptar las funciones que los usan para que funcione.
            checkear funcion: solicitud_dia para que sea compatible con Datetime
            NO CAMBIADO, OK!

        13 - Crear funcion para sacar saldo de una cuenta para poder usarla en las distintas funciones que tengan esta funcionalidad
            como: realizar transferencia, inversiones

        14 - checkear si vale la pena modificar la funcion "realizar transferencia" y que solo llame dos funciones universales, (Que serian sacar saldo de cuenta e ingresar saldo de cuenta)
            14.1 - Crear funcion para añadir saldo a una cuenta y usarla en las distintas funciones que tengan esta funcionalidad

        15 - Modificar print de funcion "Resumen de Cuenta" para que se vea mas estetico

        16 - Resumen de Cuenta: Validar que cuando el usuario ingrese las fechas de inicio tiene que ser menor o igual al dia de la fecha (Para esto aprovechamos que es Datetime).

        Funciones de Administrador
        17 - Agregar a los usuarios una key "es_admin" al diccionario que usamos como base de datos con valor booleano
            Esto va a representar si el usuario es Administrador de la aplicacion o no
            LISTO
        
        18 - Al crear una cuenta nueva preguntar si es una cuenta de Administrador, en caso que si, debera ingresar la contraseña de Administrador
            y si coincide entonces el booleando de Admin es True
        
        19 - Agregar Menú especial para administradores

        20 - Agregar funcion para obtener comision de las tranferencias (1%)
        20.1 - Hay que crear una cuenta principal para el banco como usuario

        Funciones de Administrador
        21 - Agregar funcion para ver cantidad de dinero depositado en todas las cuentas en X fecha

        22 - Agregar funcion para ver cantidad de usuarios registrados

        23 - Agregar funcion para ver cantidad de dinero depositado en todas las cuentas
            LISTO

        24 - Agregar funcion para ver dinero que gano el banco por comisiones 

        25 - Lectura de base de datos desde archivo db.json
            LISTO

        26 - Crear funcion para guardar cambios realizados y que queden registrados en el archivo db.json

    - FALTA AGREGAR:
        1 - Agregar Tuplas (Tuple) 
        2 - Agregar Conjuntos (Set) - Agregar en Tarea 9
        3 - Agregar Try/Except - Agregar en Validaciónes
    - Crear o funcion (o no) para validar que el numero ingresado en el input este dentro de las opciones (menu por ejemplo)
    - '''

def cargar_db():
    '''Funcion para cargar en memoria los datos del archivo que se usa como DB optimizando los tiempos de ejecución'''
    with open('db.json', 'r') as archivo:
        db_datos = json.load(archivo)
    return db_datos

    # db_datos = {
    #     "usuarios":{
    #         "uade_samuel": {
    #         "nombre": "Samuel Soler",
    #         "dni": "95918716",
    #         "nombre_usuario": "uade_samuel",
    #         "contrasena": "test",
    #         "email": "ssoler@test.com",
    #         "fecha_nacimiento": "28/10/1997",
    #         "alias": "s_mp",
    #         "es_admin":True,
    #         "transacciones": [ 
    #             ["egreso","pago"  ,2025,2,21,2000,"ARS","Comida"],
    #             ["egreso", "pago" ,2025,5,22,5000,"ARS","Comida"],
    #             ["egreso", "pago" ,2025,5,23,5000,"ARS","Entretenimiento"],
    #             ["egreso", "pago" ,2025,5,24,5000,"ARS","Facultad"],
    #             ["egreso", "pago" ,2025,5,25,5000,"ARS","Laburo"],
    #             ["egreso", "pago" ,2025,5,26,5000,"ARS","Laburo"],
    #             ["egreso", "pago" ,2025,5,26,5000,"ARS","Comida"]
    #              ],
    #         "saldo": 7000},
    #     "administradores":{
    #         "llaves":["seleccion"]
    #     }
    #     }
    # }
    # return db_datos

def solicitud_dia(mensaje):
    '''Funcion para solicitar al usuario el ingreso del dia
        Nota: Temporal hasta que se defina si se puede usar Datetime'''
    mensaje += " | Formato: (AAAA-MM-DD)"
    fecha = input(mensaje)
    anio  = int(fecha[0:4])   #2025
    mes   = int(fecha[5:7])   # 09
    dia   = int(fecha[8:10]) 
    return anio, mes, dia

def checkear_fecha_en_rango(anio_inicio, mes_inicio, dia_inicio, anio_final, mes_final, dia_final, anio, mes, dia):
    '''Funcion para checkear que la fecha ingresada este dentro del rango de fechas'''
    if (anio > anio_inicio and anio < anio_final):
        valido = True
    elif anio == anio_inicio:
        if (mes > mes_inicio) or (mes == mes_inicio and dia >= dia_inicio):
            valido = True
        else:
            valido = False
    elif anio == anio_final:
        if (mes < mes_final) or (mes == mes_final and dia <= dia_final):
            valido = True
        else:
            valido = False
    else:
        valido = False
    
    return valido

def nuevo_usuario(db_datos):
    '''Funcion para crear nuevo usuario con validaciones basicas'''
    def validar_usuario_unico():
        '''Funcion para validar que el usuario ingresado sea unico'''
        valido = False
        while valido == False:
            nombre_usuario = input("Ingrese nombre de usuario: ")
            # no puede estar vacío ni ser "salir"
            if nombre_usuario == "" or nombre_usuario == "salir" or nombre_usuario == "SALIR":
                print("El usuario no puede estar vacio ni ser 'salir'")
                valido = False
            # no puede repetirse
            elif nombre_usuario in db_datos["usuarios"]:
                print("El usuario ya existe")
                valido = False
            else:
                valido = True
        return nombre_usuario

    def validar_contrasena_usuario():
        '''Funcion para validar que la contraseña ingresada cumpla los requisitos de seguridad:
            Una letra mayuscula, Al menos un numero, Minimo de 8 caracteres'''
        valida_contra = False
        while valida_contra == False:
            contrasena = input("Ingrese contraseña (min 8, una mayuscula y un numero): ")

            if len(contrasena) < 8:
                print("La contraseña debe tener al menos 8 caracteres")
            else:
                tiene_mayus = 0
                tiene_numero = 0
                for c in contrasena:
                    if c >= "A" and c <= "Z":
                        tiene_mayus = 1
                    if c >= "0" and c <= "9":
                        tiene_numero = 1
                if tiene_mayus == 0:
                    print("Debe tener al menos una mayuscula")
                elif tiene_numero == 0:
                    print("Debe tener al menos un numero")
                else:
                    valida_contra = True
        return contrasena

    def validar_email():
        '''Funcion para validar que el correo electronico ingresado sea valido'''
        # validación de email
        valido_email = False
        while valido_email == False:
            email = input("Ingrese email: ")
            if "@" not in email or "." not in email:
                print("El email no es valido")
            else:
                valido_email = True
        return email

    def check_admin(db):
        '''Funcion para dar acceso de administrador a la cuenta creada''' 
        contrasena = input("Ingrese contraseña de administrador:")
        if contrasena in db["administradores"]["llaves"]:
            return True
        else:
            return False

    print("#### CREANDO NUEVO USUARIO ####")
    nombre = input("Ingrese nombre completo: ")
    dni = input("Ingrese DNI: ")
    nombre_usuario = validar_usuario_unico()
    contrasena = validar_contrasena_usuario()
    email = validar_email()
    fecha_nacimiento = "/".join(solicitud_dia("Ingrese fecha de nacimiento:"))
    alias = input("Ingrese alias: ")
    es_admin = check_admin(db_datos)

    usuario = {
        "nombre": nombre,
        "dni": dni,
        "nombre_usuario": nombre_usuario,
        "contrasena": contrasena,
        "email": email,
        "fecha_nacimiento": fecha_nacimiento,
        "alias": alias,
        "es_admin": es_admin,
        "transacciones": [],
        "saldo": 0
    }

    db_datos["usuarios"][nombre_usuario] = usuario
    print("Usuario creado correctamente")

def ingresar_dinero(usuario):
    '''Funcion para ingresar dinero a una cuenta'''
    print("#### INGRESANDO DINERO ####")
    monto_valido = False
    while monto_valido == False:
        montoo_  = int(input("Ingrese monto a depositar: "))
        if montoo_ <= 0:
            print("El monto debe ser mayor a 0")
        else:
            monto_valido = True

    anio, mes, dia = solicitud_dia("Ingrese fecha de hoy")

    etiqueta = input("Ingrese etiqueta (ej: Sueldo, Comida): ")
    if etiqueta == "":
        etiqueta = "Varios"

    transaccion = ["ingreso", "deposito", anio, mes, dia, montoo_, "ARS", etiqueta]
    usuario['transacciones'].append(transaccion)
    usuario['saldo'] += montoo_

    print("Deposito registrado. Nuevo saldo:", usuario['saldo'])

def realizar_transferencia(usuario, db_datos):
    '''Funcion para realizar transferencia entre cuentas'''
    print("#### TRANSFERENCIA ####")
    flag = True
    while flag:
        alias_destino = input("Ingrese alias del destinatario: ")
        # Buscar usuario destino por alias
        usuario_destino = None
        for u in db_datos["usuarios"]:
            if db_datos["usuarios"][u]['alias'] == alias_destino and usuario['alias'] != alias_destino:
                usuario_destino = db_datos["usuarios"][u]
                flag = False
        
        if usuario['alias'] == alias_destino:
            print("No se puede transferir a la misma cuenta de donde se hace la transferencia")
        elif usuario_destino is None:
            print("El alias ingresado no existe. Ingreselo nuevamente")
    
    monto = 0
    while monto <= 0 or usuario["saldo"] < monto:
        monto = int(input("Ingrese monto a transferir: "))
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
        elif usuario["saldo"] < monto:
            print("Saldo insuficiente para realizar la transferencia.")

    anio, mes, dia = solicitud_dia("Ingrese fecha de hoy")

    # Restar del usuario emisor
    usuario["saldo"] -= monto
    transaccion_emisor = ["egreso", "transferencia", anio, mes, dia, monto, "ARS", "Transferencia a " + usuario_destino["nombre_usuario"]]
    usuario["transacciones"].append(transaccion_emisor)

    # Sumar al usuario receptor
    usuario_destino["saldo"] += monto
    transaccion_destino = ["ingreso", "transferencia", anio, mes, dia, monto, "ARS", "Transferencia de " + usuario["nombre_usuario"]]
    usuario_destino["transacciones"].append(transaccion_destino)

    print(f"Transferencia realizada con éxito. Nuevo saldo: {usuario['saldo']}")

def control_gatos(usuario):
    '''Funcion para hacer analisis de gastos'''
    print("#### CONTROL DE GASTOS ####")

    anio_inicio, mes_inicio, dia_inicio = solicitud_dia("Ingrese fecha de inicio")
    anio_final, mes_final, dia_final = solicitud_dia("Ingrese fecha de final")
    total = 0      
    categorias = {} #ver diccionario para poner categorias

    for i in usuario["transacciones"]:
        tipo = i[0]       # ingreso/egreso
        anio = i[2]
        mes = i[3]
        dia = i[4]
        monto = i[5]      
        categoria = i[7]  

        if tipo != "egreso":
            continue  # ignoramos ingresos

        registro_valido = checkear_fecha_en_rango(anio_inicio, mes_inicio, dia_inicio, anio_final, mes_final, dia_final, anio, mes, dia)
    
        if registro_valido:
            total += monto
            if categoria not in categorias:
                categorias[categoria] = 0
            categorias[categoria] += monto


    fecha_inicio = str(anio_inicio)+"_"+str(mes_inicio)+"_"+str(dia_inicio)
    fecha_final = str(anio_final)+"_"+str(mes_final)+"_"+str(dia_final)
    
    if total == 0:
        print(f"No hubo egresos entre {fecha_inicio} y {fecha_final}.")
    else:
        print(f"\nGASTOS desde {fecha_inicio} hasta {fecha_final}")
        print(f"Total gastado: ${total}")
        for cat, monto in categorias.items():
            porcentaje = (monto / total) * 100
            print(f"- {cat}: ${monto} ({porcentaje:.2f}%)")

def objetivo_ahorro(usuario):
    '''Funcion para crear objetivo de ahorro'''
    print("#### PLANIFICACION DE AHORRO ####") 
    monto = int(input('Ingrese el monto que desea ahorrar (o escriba -1 para salir):'))
    if monto == -1:
            print("Volviendo al menú...")
            return
    while monto <= 0:
        monto = int(input('Monto invalido, debe ser mayor a 0. Ingrese nuevamente'))
    
    motivo = input("Ingrese el motivo de este ahorro (ejemplo: viaje): ")

    periodo = int(input('¿En cuántos días quiere lograrlo? (o escriba -1 para"salir"): '))
    if periodo == -1:
            print("Volviendo al menú...")
            return
    while periodo <= 0 or periodo > 36500:
            periodo = int(input('Periodo invalido, debe ser mayor a 0. Ingrese nuevamente'))

    #calculo cuanto debe ahorra
    saldo_actual = usuario['saldo']
    restante = monto - saldo_actual
    if restante < 0:
        print("\nFelicitaciones! Tienes el dinero disponible para cumplir el objetivo ")
        print("Motivo: ", motivo)
        print("Monto objetivo: ", monto)
        print("Saldo actual: ", saldo_actual)
    else:
        ahorro_diario = restante / periodo

        print("\n### OBJETIVO DE AHORRO ###")
        print("Motivo:", motivo)
        print("Monto objetivo:", monto)
        print("Días para lograrlo:", periodo)
        print("Saldo actual:", saldo_actual)
        print("Monto restante:", restante)
        print("Debes ahorrar por día:", ahorro_diario)

def resumen_cuenta(usuario):
    '''Funcion para mostrar resumen de cuenta'''
    print("#### RESUMEN DE CUENTA ####")
    print(f"Saldo actual: {usuario['saldo']} ARS")
    print("Transacciones del mes actual:\n")

    # Mostrar las transacciones del mes actual
    anio, mes, dia = solicitud_dia("Ingrese fecha de hoy")
    trans_mes = [t for t in usuario["transacciones"] if t[2] == anio and t[3] == mes]

    if len(trans_mes) == 0:
        print("No hay transacciones este mes.")
    else:
        for t in trans_mes:
            print(t)

    print("\nOpciones:")
    print("1 - Mostrar transacciones entre rango de fechas")
    print("2 - Mostrar últimas 5 transacciones")
    print("3 - Mostrar primeras 5 transacciones del mes")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        anio_inicio, mes_inicio, dia_inicio = solicitud_dia("Ingrese fecha de inicio")
        anio_final,  mes_final, dia_final = solicitud_dia("Ingrese fecha final")
        trans_rango = [t for t in usuario["transacciones"] if checkear_fecha_en_rango(anio_inicio, mes_inicio, dia_inicio, anio_final, mes_final, dia_final, t[2], t[3], t[4])]
        if len(trans_rango) == 0:
            print("No hay transacciones en ese rango.")
        else:
            for t in trans_rango:
                print(t)

    elif opcion == "2":
        ultimas = usuario["transacciones"][-5:]
        for t in ultimas:
            print(t)

    elif opcion == "3":
        primeras = trans_mes[:5]
        for t in primeras:
            print(t)

    else:
        print("Opción inválida.")

def log_in(db_datos):
    '''Funcion para hacer login en una cuenta'''
    print("#### INICIO DE SESION ####")
    usuario_retry = 0
    while usuario_retry < 5:
        usuario = input("Ingrese nombre de usuario o 'salir' para cancelar:\n")
        if usuario == "salir":
            print("Inicio de Sesion cancelado")
            return 
        #si el usuario existe en la DB
        elif usuario in db_datos["usuarios"]:
            contrasena_retry = 0
            while contrasena_retry < 5:
                contrasena = input("Ingrese su contraseña:\n")
                #si la contraseña es correcta
                if contrasena == db_datos["usuarios"][usuario]['contrasena']:
                    cumpleanos = checkear_cumpleanos(db_datos['usuarios'][usuario])
                    if cumpleanos:
                        print(f"Bienvenido {db_datos['usuarios'][usuario]['nombre']}, Feliz Cumpleaños!!")
                    else:
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

def gastos_compartidos():
    '''Funcion para basado en un gasto, calcular cuanto debe pagar cada persona
    - Permitir al usuario ingresar cantidad de personas a repartir el gasto
    - Ingresar Monto a pagar.
    - Mostar cuanto debe pagar cada persona.'''

    print("#### Gastos Compartidos ####")
    monto = int(input("Ingrese monto a repartir"))
    cant_personas = int(input("Ingrese cantidad de personas a repartir el gasto"))
    opcion = ""
    while opcion != "s" and opcion != "n":
        opcion = input("Desea que el gasto se divida equitativamente? s/n: ")
        if opcion != "s" and opcion != "n":
            print("Opción inválida, seleccione s para Sí, n para No")
    if opcion == "n":
        datos = [[input(f"Nombre de la persona {persona+1}"), int(input(f"Ingrese porcentaje que debe abonar (Solo el numero)"))] for persona in range(cant_personas)]
        porcentajes = [dato[1] for dato in datos]
        porcentaje_total = reduce(lambda acumulador, porcentaje: acumulador + porcentaje[1], datos, 0)
        while porcentaje_total != 100:
            print("El Porcentaje de reparticion no es 100%, de quien desea modificar el porcentaje a pagar?")
            for persona in range(len(datos)):
                print(f"Persona {persona+1}: {datos[persona][0]} - {datos[persona][1]}%")
            opcion = 0
            while opcion < 1 or opcion > cant_personas:
                opcion = int(input("Ingrese numero de persona: "))
                if opcion < 1 or opcion > cant_personas:
                    print("Opcion no valida, ingrese un numero correcto")
            nuevo_porcentaje = int(input("Ingrese nuevo porcentaje: "))
            datos[opcion-1][1] = nuevo_porcentaje
            porcentaje_total = reduce(lambda acumulador, porcentaje: acumulador + porcentaje[1], datos, 0)
        for persona in range(len(datos)):
            print(f"{datos[persona][0]} debe abonar el {datos[persona][1]}% que es ${monto*datos[persona][1]/100}")
    elif opcion == "s":
           print(f"Cada persona debe abonar ${monto/cant_personas}")    
             
def inversiones(usuario):
    '''Funcion para hacer inversiones a plazo fijo
    TOOD: Agregar cantidad de dias para el plazos fijo y calcular el interes basado en esto(30 dias, 60 dias)'''
    print("#### INVERSION A PLAZO FIJO ####")

    print(f"Su saldo es {usuario['saldo']}")
    inversion = 0
    while inversion <= 0 or inversion > usuario['saldo']:
        inversion = int(input("Ingrese monto a invertir: "))
        if inversion <= 0 or inversion > usuario['saldo']:
            print(f"Monto invalido, ingrese monto mayor a 0 y menor a su saldo actual que es {usuario['saldo']}")

    dias = int(input("Ingrese cantidad de dias para el plazo fijo: "))
    TASA_ANUAL = 0.50
    tasa_mensual = TASA_ANUAL/12
    monto = inversion
    print("Resumen inversion a final del año\nMes / Monto acumulado:")
    for mes in range(1,13):
        interes = monto * tasa_mensual
        monto += interes
        print(f"{mes} / {monto}")
    
    opcion = ""
    while opcion != "s" and opcion != "n":
        opcion = input("Desea Confirmar la operación? s/n: ")
        if opcion != "s" and opcion != "n":
            print("Opción inválida, seleccione s para Sí, n para No")
    if opcion == "s":
        #TODO: Agregar funcion universal para quitar saldo
        usuario['saldo'] -= inversion
        registro_inversion = ["egreso", "inversion", fecha, inversion, "ARS", "inversion a plazo fijo"] # type: ignore
        usuario['transacciones'].append(registro_inversion)
        print("Operación confirmada")
    elif opcion == "n":
        print("Operación cancelada")

def checkear_cumpleanos(usuario):
    '''Funcion para checkear si es el cumpleaños del usuario''' 
    fecha_nacimiento = datetime.strptime(usuario['fecha_nacimiento'], "%d/%m/%Y")
    fecha_hoy = datetime.now()
    print(fecha_nacimiento)
    print(fecha_hoy)
    if fecha_nacimiento.month == fecha_hoy.month and fecha_nacimiento.day == fecha_hoy.day:
        return True
    else:
        return False

#Funciones de Administrador
def ver_dinero_depositado_en_banco(db_datos):
    '''Funcion para ver cantidad de dinero depositado en todas las cuentas'''
    dinero_depositado = reduce(lambda acumulador, usuario: acumulador + db_datos['usuarios'][usuario]['saldo'], db_datos['usuarios'], 0)
    print("El dinero depositado en las cuentas del banco es: ", dinero_depositado)

def menu():
    '''Funcion para mostrar menu'''
    opcion = 0
    while opcion < 1 or opcion > 8:
        opcion = int(input('''##### MENU ##### \n
        1. Ingresar dinero\n
        2. Realizar transferencia\n
        3. Resumen de cuenta\n
        4. Control de Gastos\n
        5. Calculo de Gastos Compartidos\n
        6. Inversión a Plazo Fijo\n
        7. Planificacion de Ahorro\n
        8. Salir\n'''))
        if opcion < 1 or opcion > 8:
            print("Opcion no valida, ingrese una opcion correcta del menú")
    return opcion

def main():
    '''Funcion principal que ejecuta el codigo'''
    db_datos = cargar_db()
    log_in_opcion = int(input('''Desea Crear usuario o Iniciar sesion? \n
    1. Crear Usuario\n
    2. Iniciar Sesion\n'''))

    if log_in_opcion == 1:
        nuevo_usuario(db_datos)
        seguir = int(input('''Desea Iniciar sesion? \n
        1. Si\n
        2. No\n'''))
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

    menu_opcion = 1
    while menu_opcion > 0 and menu_opcion < 9:
        if usuario['es_admin']:
            print("ADMINISTRADOR")
        else:
            menu_opcion = menu()
        if menu_opcion == 1:
            ingresar_dinero(usuario)
        elif menu_opcion == 2:
            realizar_transferencia(usuario, db_datos)
        elif menu_opcion == 3:
            resumen_cuenta(usuario)
        elif menu_opcion == 4:
            control_gatos(usuario)
        elif menu_opcion == 5:
            gastos_compartidos()
        elif menu_opcion == 6:
            inversiones(usuario)
        elif menu_opcion == 7:
            objetivo_ahorro(usuario)
        elif menu_opcion == 8:
            print("Gracias por usar el servicio")
        seguir = input("Desea hacer alguna otra operacion? s/n")
        if seguir == "n":
            print("Gracias por usar el servicio")
            menu_opcion = 100

main()