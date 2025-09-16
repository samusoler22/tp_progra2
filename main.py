import json
from functools import reduce
from datetime import datetime

'''TODO: 
    Repartición de Tareas:
        - Agus Goldberg: 5 y 6
        - Samu: 7 y 8
        - Benja: 3 y 4
        - Agus Lopez: 1 y 2

    Ideas mejoras:
    -Agregar una funcion que quite saldo al usuario y se use en las otras funciones como transferencias o inversiones
        se le pasaria como argumento usuario (para ubicar en la DB), monto (para saber cuanto quitar) y motivo (para saber que tipo de transaccion es)
    - Quizas posibiliadad de comprar Stocks/Crypto

    Tareas:
        1. Agregar validaciones del nuevo usuario (Funciones creadas dentro de la funcion nuevo_usuario)
            - En la funcion "nuevo usuario" crear logica para validar los datos que ingresa el usuario.
            - Las funciones ya estan prehechas, agregar mas de ser necesario.
            LISTO

        2. Crear funcion para ingresar dinero
            - Crear logica para agregar dinero a la cuenta del usuario en la funcion "ingresar_dinero".
            - Tener en cuenta que habria que agregar una transaccion en el usuario por cada ingreso.
            - Que se agregue el ingreso al saldo del usuario.
            - IMPORTANTE: Tener en cuenta que la parte de las transacciones es una matriz.
            LISTO/REVISAR: CAMBIAR FORMATO FECHA SEGUN CRITERIO FUNCION CONTROL DE GASTOS

        3. Crear funcion para realizar transferencia.
            - Crear logica para realizar transferencia entre cuentas dentro de la funcion "realizar_transferencia"
            - Tener en cuenta que esta funcion usa dos parametros, uno es alias porque vamos a buscar el usuario a transferir en nuestro diccionario de usuarios
            - Tener en cuenta que el monto que se transfiere se resta del saldo del usuario que transfiere y se agregan las transacciones pertinentes.
            REVISAR BENJA

        4. Crear funcion para mostrar resumen de cuenta
            - Crear logica en funcion "resumen_cuenta"
            - Por defecto mostrar transacciones del mes en curso o el mes anterior (a definir)
            - Luego de mostrar resumen, crear menu para preguntar si quiere:
                1-Mostrar resumen de transacciones entre un rango de fechas
                2-Mostrar ultimos 5 transacciones (aca aplicamos slicing de la lista)
                3-Mostrar primeras 5 transacciones del mes.
            REVISAR BENJA
        
        5 - Crear funcion de Control de Gastos.
            - Crear logica donde se muestre gastos total del mes y estilo de gastos basado en las etiquetas de las transacciones de egreso, ejemplo:
                "Se gasto un 20% en comida"
            REVISAR: VER FORMATO FECHA
        
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

    - FALTA AGREGAR:
        1 - Matrices: Usar en lista de transacciones.               LISTO   - en Gastos Compartidos y Control Gastos
        2 - Listas y sus funciones: ver en que parte usar.          LISTO   - Ingresar Dinero
        3 - Comprension de Listas:                                  LISTO   - en Gastos Compartidos
        4 - Funciones Lambda y metodos (Map, Filter, Reduce)        LISTO   - en Gastos Compartidos
        5 - Slicing:                                                LISTO   - en Resumen de Cuenta
    - Crear o funcion (o no) para validar que el numero ingresado en el input este dentro de las opciones (menu por ejemplo)
    - '''

def cargar_db():
    '''Funcion para cargar en memoria los datos del archivo que se usa como DB optimizando los tiempos de ejecución'''
    #with open('db.json', 'r') as archivo:
    #    db_datos = json.load(archivo)
    #return db_datos

    db_datos = {
        "usuarios":{
            "uade_samuel": {
            "nombre": "Samuel Soler",
            "dni": "95918716",
            "nombre_usuario": "uade_samuel",
            "contrasena": "test",
            "email": "ssoler@test.com",
            "alias": "s_mp",
            "transacciones": [ 
                ["egreso","pago","2025-09-02",2000,"ARS","Comida"],
                ["egreso", "pago"    ,"2025-05-22",5000,"ARS","Comida"],
                ["egreso", "pago"    ,"2025-05-23",5000,"ARS","Entretenimiento"],
                ["egreso", "pago"    ,"2025-05-24",5000,"ARS","Facultad"],
                ["egreso", "pago"    ,"2025-05-25",5000,"ARS","Laburo"],
                ["egreso", "pago"    ,"2025-05-26",5000,"ARS","Laburo"],
                ["egreso", "pago"    ,"2025-05-26",5000,"ARS","Comida"]
                 ],
            "saldo": 7000
        }
        }
    }
    return db_datos

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

    print("#### CREANDO NUEVO USUARIO ####")
    nombre = input("Ingrese nombre completo: ")
    dni = input("Ingrese DNI: ")
    nombre_usuario = validar_usuario_unico()
    contrasena = validar_contrasena_usuario()
    email = validar_email()
    alias = input("Ingrese alias: ")

    usuario = {
        "nombre": nombre,
        "dni": dni,
        "nombre_usuario": nombre_usuario,
        "contrasena": contrasena,
        "email": email,
        "alias": alias,
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

    fecha = input("Ingrese fecha (AAAA-MM-DD): ")
    etiqueta = input("Ingrese etiqueta (ej: Sueldo, Comida): ")
    if etiqueta == "":
        etiqueta = "Varios"

    transaccion = ["ingreso", "deposito", fecha, montoo_, "ARS", etiqueta]
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

    
    # Al no poder utilizar la libreria datetime por no ser parte de lo visto en clases
    #solicitamos el ingres de la fecha de forma manual
    fecha = input("Ingrese fecha (AAAA-MM-DD): ")

    # Restar del usuario emisor
    usuario["saldo"] -= monto
    transaccion_emisor = ["egreso", "transferencia", fecha, monto, "ARS", "Transferencia a " + usuario_destino["nombre_usuario"]]
    usuario["transacciones"].append(transaccion_emisor)

    # Sumar al usuario receptor
    usuario_destino["saldo"] += monto
    transaccion_destino = ["ingreso", "transferencia", fecha, monto, "ARS", "Transferencia de " + usuario["nombre_usuario"]]
    usuario_destino["transacciones"].append(transaccion_destino)

    print(f"Transferencia realizada con éxito. Nuevo saldo: {usuario['saldo']}")

def control_gatos(fecha_inicio, fecha_final, usuario):  #Fix
    '''Funcion para hacer analisis de gastos'''
    print("#### CONTROL DE GASTOS ####")
    total = 0      
    categorias = {} #ver diccionario para poner categorias

    for i in usuario["transacciones"]:
        tipo = i[0]       # ingreso/egreso
        fecha = i[2]      #"2025-09-02" 
        monto = i[3]      
        categoria = i[5]  

        if tipo != "egreso":
            continue  # ignoramos ingresos

        if fecha >= fecha_inicio and fecha <= fecha_final:
            total += monto
            if categoria not in categorias:
                categorias[categoria] = 0
            categorias[categoria] += monto

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
    hoy = datetime.today().strftime("%Y-%m")
    trans_mes = [t for t in usuario["transacciones"] if t[2].startswith(hoy)]

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
        f_inicio = input("Ingrese fecha de inicio (AAAA-MM-DD): ")
        f_final = input("Ingrese fecha final (AAAA-MM-DD): ")
        trans_rango = [t for t in usuario["transacciones"] if f_inicio <= t[2] <= f_final]
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
        registro_inversion = ["egreso", "inversion", fecha, inversion, "ARS", "inversion a plazo fijo"]
        usuario['transacciones'].append(registro_inversion)
        print("Operación confirmada")
    elif opcion == "n":
        print("Operación cancelada")

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
        8. Salir'''))
        if opcion < 1 or opcion > 8:
            print("Opcion no valida, ingrese una opcion correcta del menú")
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

    menu_opcion = 1
    while menu_opcion > 0 and menu_opcion < 9:
        menu_opcion = menu()
        if menu_opcion == 1:
            ingresar_dinero(usuario)
        elif menu_opcion == 2:
            realizar_transferencia(usuario, db_datos)
        elif menu_opcion == 3:
            resumen_cuenta(usuario)
        elif menu_opcion == 4:
            fecha_inicio = int(input('Ingrese fecha inicial de periodo (AAAA-MM-DD): '))
            fecha_final = int(input('Ingrese fecha final de periodo (AAAA-MM-DD): '))
            control_gatos(fecha_inicio, fecha_final, usuario)
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
            print(db_datos)
            menu_opcion = 100

main()