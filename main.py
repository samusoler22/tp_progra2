import os
import json
from functools import reduce
from datetime import datetime

'''TODO: 
    Repartición de Tareas:
        - Agus Goldberg: 40% (5, 6) 80% (11 L, 19L  , 20L  , 21L)
        - Samu:          40% (7, 8) 80% (12 L, 13  , 14  , 24, 25 L)
        - Benja:         40% (3, 4) 80% (9  L, 15 L, 16 L, 22 L)
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
            LISTO - LINEA 718

        10 - Solicitar al crear usuario que ingrese fecha de nacimiento y guardarlo en la DB
            LISTO - LINEA 258

        11 - Crear Funcion donde a partir de la fecha de nacimiento ya sabemos el cumpleaños del usuario, comparamos
            la fecha del dia de hoy usando datetime y en caso de que sea su cumpleaños printeamos una felicitacion al hacer login.
            LISTO - LINEA 546
        
        12 - Implementar Datetime: Cambiar el formato de fecha anterior por valor datetime y adaptar las funciones que los usan para que funcione.
            checkear funcion: solicitud_dia para que sea compatible con Datetime.
            NOTA: Al final como en JSON no se permite guardar tuplas ni objetos datetime decidimos crear una funcion que transforme los valores segun conveniencia.
            LISTO - LINEA 141

        13 - Crear funcion para sacar saldo de una cuenta para poder usarla en las distintas funciones que tengan esta funcionalidad
            como: realizar transferencia, inversiones

        14 - checkear si vale la pena modificar la funcion "realizar transferencia" y que solo llame dos funciones universales, (Que serian sacar saldo de cuenta e ingresar saldo de cuenta)
            14.1 - Crear funcion para añadir saldo a una cuenta y usarla en las distintas funciones que tengan esta funcionalidad

        15 - Modificar print de funcion "Resumen de Cuenta" para que se vea mas estetico
            LISTO

        16 - Resumen de Cuenta: Validar que cuando el usuario ingrese las fechas de inicio tiene que ser menor o igual al dia de la fecha (Para esto aprovechamos que es Datetime).
            LISTO - LINEA 515
        
        Funciones de Administrador
        17 - Agregar a los usuarios una key "es_admin" al diccionario que usamos como base de datos con valor booleano
            Esto va a representar si el usuario es Administrador de la aplicacion o no
            LISTO - LINEA 295
        
        18 - Al crear una cuenta nueva preguntar si es una cuenta de Administrador, en caso que si, debera ingresar la contraseña de Administrador
            y si coincide entonces el booleando de Admin es True
            LISTO - LINEA 285
        
        19 - Agregar Menú especial para administradores
            LISTO - LINEA 266

        20 - Agregar funcion para obtener comision de las tranferencias (1%)
        20.1 - Hay que crear una cuenta principal para el banco como usuario
        LISTO - LINEA 381

        Funciones de Administrador
        21 - Agregar funcion para ver cantidad de dinero depositado en todas las cuentas en X fecha

        22 - Agregar funcion para ver cantidad de usuarios registrados
            LISTO - LINEA 684

        23 - Agregar funcion para ver cantidad de dinero depositado en todas las cuentas
            LISTO - LINEA 678

        24 - Agregar funcion para ver dinero que gano el banco por comisiones
            LISTO - LINEA 687

        25 - Lectura de base de datos desde archivo db.json
            LISTO - LINEA 133

        26 - Crear funcion para guardar cambios realizados y que persistan en el archivo db.json
            LISTO - LINEA 148

        RECURSIVIDAD = Linea 238.
        TUPLAS = FECHAS DE LOS CUMPLEAÑOS
        SETS / CONJUNTOS = AGREGADOS EN VALIDACION DE USUARIOS UNICOS
        TRY / EXCEPT = AGREGADO EN VALIDACIONES DE LECTURA DE DB (Archivo JSON) E INPUTS


'''

def cargar_db():
    '''Funcion para cargar en memoria los datos del archivo que se usa como DB optimizando los tiempos de ejecución'''
    
    try:
        with open(os.path.abspath('db.json'), 'r') as archivo:
            db_datos = json.load(archivo)
    except FileNotFoundError:
        print("Error: No se pudo conectar a la base de datos")
    except json.JSONDecodeError:
        print("Error: Formato incorrecto en la base de datos")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else:
        return db_datos

def persistir_datos(db_datos):
    '''Funcion para guardar los datos en el archivo db.json'''
    try:
        with open('db.json', 'w') as archivo:
            json.dump(db_datos, archivo)
    except Exception as e:
        print(f"Error inesperado: {e}")

def cambiar_formato_fechas(value, to):
    '''Funcion para pasar tuplas a datetime y viceversa'''
    if to == "datetime":
        if type(value) == tuple:
            return datetime(value[0], value[1], value[2])
        elif type(value) == str:
            return datetime.strptime(value, "%Y-%m-%d")
    elif to == "tuple":
        if type(value) == datetime:
            values = value.strftime("%Y-%m-%d").split("-")
            return int(values[0]), int(values[1]), int(values[2])
        elif type(value) == str:
            values = value.split("-")
            return int(values[0]), int(values[1]), int(values[2])
    elif to == "str":
        if type(value) == tuple:
            return "-".join(map(str, value))
        elif type(value) == datetime:
            return value.strftime("%Y-%m-%d")

def solicitud_dia(mensaje, dt=False):
    '''Funcion para solicitar al usuario el ingreso del dia
       parametro dt, define si se retorna un objeto datetime o tupla'''
    def checkear_formato(fecha):
        '''Funcion para checkear que el string tiene el formato AAAA-MM-DD'''
        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
            return fecha
        except ValueError:
            return False

    mensaje += " | Formato: (AAAA-MM-DD)"
    if dt:
        while True:
            fecha_str = input(mensaje)
            fecha_datetime = checkear_formato(fecha_str)
            if fecha_datetime:
                return fecha_datetime
            print("Fecha inválida. Intente nuevamente con el formato AAAA-MM-DD.")
    else:
        while True:
            fecha_str = input(mensaje)
            fecha_datetime = checkear_formato(fecha_str)
            if fecha_datetime:
                anio, mes, dia = fecha_datetime.strftime("%Y-%m-%d").split("-")
                return int(anio), int(mes), int(dia)
            print("Fecha inválida. Intente nuevamente con el formato AAAA-MM-DD.")

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

def nuevo_usuario(db_datos, usuarios_set):
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
            elif nombre_usuario in usuarios_set:
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
        valido_admin = False
        pregunta = input("¿Tiene acceso de administrador? (s/n): ")
        if pregunta.lower() == "s":
            while valido_admin == False:
                contrasena = input("Ingrese contraseña de administrador: ")
                if contrasena in db["administradores"]["llaves"]:
                    valido_admin = True
                else:
                    print("La contraseña no es correcta")
        elif pregunta.lower() == "n":
            return False
        else:
            print("Opción inválida, seleccione s para Sí, n para No")
            valido_admin = check_admin(db)
        return valido_admin

    def validacion_vacio(mensaje):
        '''Funcion para validar que el input no esta vacio'''
        flag = True
        while flag:
            input_ = input(mensaje)
            if input_.strip():
                flag = False
            else:
                print("valor vacio, ingrese nuevamente")
        
        return input_

    print("#### CREANDO NUEVO USUARIO ####")
    nombre = validacion_vacio("Ingrese nombre completo: ")
    dni = validacion_vacio("Ingrese DNI: ")
    nombre_usuario = validar_usuario_unico()
    contrasena = validar_contrasena_usuario()
    email = validar_email()
    fecha_nacimiento = solicitud_dia("Ingrese fecha de nacimiento:", True)
    while fecha_nacimiento > datetime.now():
        print("La fecha de nacimiento no puede ser posterior a la fecha actual. Ingrese nuevamente")
        fecha_nacimiento = solicitud_dia("Ingrese fecha de nacimiento:", True)
    fecha_nacimiento = cambiar_formato_fechas(fecha_nacimiento, "str")
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
    usuarios_set.add(nombre_usuario)
    print("Usuario creado correctamente")
    persistir_datos(db_datos)

def ingresar_dinero(usuario):
    '''Funcion para ingresar dinero a una cuenta'''
    print("#### INGRESANDO DINERO ####")
    monto_valido = True
    while monto_valido:
        try:
            montoo_  = int(input("Ingrese monto a depositar: "))
            if montoo_ <= 0:
                print("El monto debe ser mayor a 0")
            else:
                monto_valido = False
        except ValueError:
            print("El monto debe ser un numero")

    fecha = datetime.now()
    anio = int(fecha.year)
    mes = int(fecha.month)
    dia = int(fecha.day)

    etiqueta = input("Ingrese etiqueta (ej: Sueldo, Comida): ")
    if etiqueta == "":
        etiqueta = "Varios"

    transaccion = ["ingreso", "deposito", anio, mes, dia, montoo_, "ARS", etiqueta]
    usuario['transacciones'].append(transaccion)
    usuario['saldo'] += montoo_

    print(f"Deposito registrado. Nuevo saldo: {usuario['saldo']} pesos")

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
        try:
            monto = int(input("Ingrese monto a transferir: "))
        except ValueError:
            print("El monto debe ser un numero valido.")
        if monto <= 0:
            print("El monto debe ser mayor a 0.")
        elif usuario["saldo"] < monto:
            print("Saldo insuficiente para realizar la transferencia.")

    fecha = datetime.now()
    anio = int(fecha.year)
    mes = int(fecha.month)
    dia = int(fecha.day)

    # calculo comisión (1%)
    comision = int(monto * 0.01)
    monto_final = monto - comision

    # resto monto del usuario emisor
    usuario["saldo"] -= monto
    transaccion_emisor = ["egreso", "transferencia", anio, mes, dia, monto, "ARS", f"Transferencia a {usuario_destino['nombre_usuario']} (comisión: {comision} ARS)"]
    usuario["transacciones"].append(transaccion_emisor)

    # calculo lo que le llega al usuario receptor
    usuario_destino["saldo"] += monto_final
    transaccion_destino = ["ingreso", "transferencia", anio, mes, dia, monto_final, "ARS", f"Transferencia de {usuario['nombre_usuario']}"]
    usuario_destino["transacciones"].append(transaccion_destino)
    db_datos["usuarios"]["banco"]["saldo"] += comision
    transaccion_banco = ["ingreso", "comision", anio, mes, dia, comision, "ARS", f"Comisión de transferencia de {usuario['nombre_usuario']}"]
    db_datos["usuarios"]["banco"]["transacciones"].append(transaccion_banco)

    print(f"Transferencia realizada con éxito. Nuevo saldo: {usuario['saldo']}")
    print(f"Comisión cobrada: {comision} ARS. El destinatario recibe: {monto_final} ARS")

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
    while True:
        try:
            monto = int(input('Ingrese el monto que desea ahorrar (o escriba -1 para salir):'))
            if monto == -1:
                print("Volviendo al menú...")
                return
            elif monto <= 0:
                print('Monto invalido, debe ser mayor a 0. Intente nuevamente.')
            else:
                break
        except ValueError:
            print("El monto debe ser un número válido. Intente nuevamente.")
    
    motivo = input("Ingrese el motivo de este ahorro (ejemplo: viaje): ")

    while True:
        try:
            periodo = int(input('¿En cuántos días quiere lograrlo? (o escriba -1 para "salir"): '))
            if periodo == -1:
                print("Volviendo al menú...")
                return
            elif periodo <= 0 or periodo > 36500:
                print('Periodo inválido, debe ser mayor a 0 y menor o igual a 36500. Ingrese nuevamente.')
            else:
                break
        except ValueError:
            print("El período debe ser un número válido. Intente nuevamente.")

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

def imprimir_tabla(transacciones, titulo="Transacciones"):
    """Imprime las transacciones en formato tabular y legible"""
    print(f"\n### {titulo} ###")
    print("-" * 70)
    print(f"{'Tipo':<10}{'Detalle':<15}{'Fecha':<12}{'Monto':<10}{'Etiqueta':<15}")
    print("-" * 70)
    for t in transacciones:
        tipo, detalle, anio, mes, dia, monto, moneda, etiqueta = t
        fecha = f"{anio}-{mes:02d}-{dia:02d}"
        print(f"{tipo.capitalize():<10}{detalle:<15}{fecha:<12}${monto:<9}{etiqueta:<15}")
    print("-" * 70)
    print(f"Total de transacciones: {len(transacciones)}")

def resumen_cuenta(usuario):
    """Muestra resumen de cuenta con formato tabular y validación de fechas"""
    print("#### RESUMEN DE CUENTA ####")
    print(f"Saldo actual: {usuario['saldo']} ARS")

    # Fecha actual
    hoy = datetime.now()

    # Mostrar transacciones del mes actual
    trans_mes = []
    for t in usuario["transacciones"]:
        tipo, detalle, anio, mes, dia, monto, moneda, etiqueta = t
        if anio == hoy.year and mes == hoy.month:
            trans_mes.append(t)

    if len(trans_mes) != 0:
        imprimir_tabla(trans_mes, "Transacciones del mes actual")
        print("\nOpciones:")
        print("1 - Mostrar transacciones entre rango de fechas")
        print("2 - Mostrar últimas 5 transacciones")
        print("3 - Mostrar primeras 5 transacciones del mes")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            fecha_inicio = solicitud_dia("Ingrese fecha de inicio", dt=True)
            fecha_final  = solicitud_dia("Ingrese fecha final", dt=True)

            # Validaciones
            while fecha_inicio > fecha_final or fecha_final > datetime.now():
                if fecha_inicio > fecha_final:
                    print("La fecha de inicio no puede ser posterior a la fecha final. Ingrese nuevamente")
                elif fecha_final > datetime.now():
                    print("La fecha final no puede ser posterior a la fecha actual. Ingrese nuevamente")
                fecha_inicio = solicitud_dia("Ingrese fecha de inicio", dt=True)
                fecha_final  = solicitud_dia("Ingrese fecha final", dt=True)

            trans_rango = []
            for t in usuario["transacciones"]:
                tipo, detalle, anio, mes, dia, monto, moneda, etiqueta = t
                fecha_trans = datetime(anio, mes, dia)
                if fecha_inicio <= fecha_trans <= fecha_final:
                    trans_rango.append(t)

            if len(trans_rango) == 0:
                print("No hay transacciones en ese rango.")
            else:
                imprimir_tabla(trans_rango, "Transacciones en el rango seleccionado")

        elif opcion == "2":
            ultimas = usuario["transacciones"][-5:]
            if len(ultimas) == 0:
                print("No hay transacciones registradas.")
            else:
                imprimir_tabla(ultimas, "Últimas 5 transacciones")

        elif opcion == "3":
            if len(trans_mes) == 0:
                print("No hay transacciones este mes.")
            else:
                primeras = trans_mes[:5]
                imprimir_tabla(primeras, "Primeras 5 transacciones del mes")

        else:
            print("Opción inválida.")
    else:
        print("No hay transacciones este mes.")

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
        print(f"Cantidad de intentos restantes ({usuario_retry+1}/5)")
        usuario_retry += 1

def gastos_compartidos():
    '''Funcion para basado en un gasto, calcular cuanto debe pagar cada persona
    - Permitir al usuario ingresar cantidad de personas a repartir el gasto
    - Ingresar Monto a pagar.
    - Mostar cuanto debe pagar cada persona.'''

    print("#### Gastos Compartidos ####")
    monto_valido = True
    cant_personas_valido = True
    while monto_valido:
        try:
            monto = int(input("Ingrese monto a repartir"))
            if monto > 0:
                monto_valido =False
            else:
                print("El Monto debe ser mayor a 0, Ingrese nuevamente")
        except ValueError:
            print("Monto invalido, ingrese un numero correcto")
    while cant_personas_valido:
        try:
            cant_personas = int(input("Ingrese cantidad de personas a repartir el gasto"))
            if cant_personas > 0:
                cant_personas_valido = False
            else:
                print("La Cantidad de personas debe ser mayor a 0, Ingrese nuevamente")
        except ValueError:
            print("Cantidad de personas invalida, ingrese un numero correcto")
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
    print("#### INVERSION A PLAZO FIJO (1 AÑO) ####")

    if usuario['saldo'] == 0:
        print("Su saldo es de 0, no puede invertir")
        return
        
    print(f"Su saldo es {usuario['saldo']}")
    inversion = 0
    while inversion <= 0 or inversion > usuario['saldo']:
        try:
            inversion = int(input("Ingrese monto a invertir: "))
        except ValueError:
            inversion = -1
        if inversion <= 0 or inversion > usuario['saldo']:
            print(f"Monto invalido, ingrese monto mayor a 0 y menor a su saldo actual que es {usuario['saldo']}")

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
        fecha = datetime.now()
        anio = int(fecha.year)
        mes = int(fecha.month)
        dia = int(fecha.day)
        
        usuario['saldo'] -= inversion
        registro_inversion = ["egreso", "inversion", anio, mes, dia, inversion, "ARS", "inversion a plazo fijo"] # type: ignore
        usuario['transacciones'].append(registro_inversion)
        print("Operación confirmada")
    elif opcion == "n":
        print("Operación cancelada")

def checkear_cumpleanos(usuario):
    """Funcion para checkear si es el cumpleaños del usuario""" 
    fecha_nacimiento = cambiar_formato_fechas(usuario['fecha_nacimiento'], "datetime")
    fecha_hoy = datetime.now()

    if fecha_nacimiento.month == fecha_hoy.month and fecha_nacimiento.day == fecha_hoy.day:
        return True
    else:
        return False

#Funciones de Administrador
def ver_dinero_depositado_en_banco(db_datos):
    '''Funcion para ver cantidad de dinero depositado en todas las cuentas'''
    dinero_depositado = reduce(lambda acumulador, usuario: acumulador + db_datos['usuarios'][usuario]['saldo'], db_datos['usuarios'], 0)
    print("El dinero depositado en las cuentas del banco es: ", dinero_depositado)

def ver_cantidad_usuarios(db_datos):
    """Muestra la cantidad de usuarios registrados en la base de datos"""
    cantidad = len(db_datos["usuarios"])
    print(f"Actualmente hay {cantidad} usuarios registrados.")

def ganancia_banco(db_datos):
    '''Funcion para calcular la ganancia del banco'''
    print("#### GANANCIA DEL BANCO ####")
    banco = db_datos["usuarios"]["banco"]
    saldo_banco = banco["saldo"]
    print("Las ganancias del banco son de: ", saldo_banco)
    
def ver_dinero_disponible_en_fecha(db_datos):
    '''Funcion para ver cantidad de dinero disponible en todas las cuentas en una fecha específica'''
    print("#### DINERO DISPONIBLE EN FECHA ####")
    fecha = input("Ingrese la fecha a consultar (AAAA-MM-DD): ")
    try:
        fecha_str = datetime.strptime(fecha, "%Y-%m-%d")
    except ValueError:
        print("Fecha inválida. Intente nuevamente.")
        return
    total = 0
    for usuario in db_datos["usuarios"]:
        saldo = db_datos["usuarios"][usuario]["saldo"]
        total += saldo
    print(f"El dinero disponible en todas las cuentas al día {fecha_str} es: {total} ARS")

def menu_administrador():
    '''Funcion para mostrar menu admin'''
    opcion = 0
    while opcion < 1 or opcion > 11:
        try:
            opcion = int(input('''##### MENU ADMINISTRADOR ##### \n
            1.  Ingresar dinero\n
            2.  Realizar transferencia\n
            3.  Resumen de cuenta\n
            4.  Control de Gastos\n
            5.  Calculo de Gastos Compartidos\n
            6.  Inversión a Plazo Fijo\n
            7.  Planificacion de Ahorro\n
            8.  Ver Dinero en todas las Cuentas\n
            9.  Ver Cantidad Usuarios Registrados\n
            10. Ganancias del banco\n
            11. Salir\n'''))
        except ValueError:
            opcion = -1
        if opcion < 1 or opcion > 11:
            print("Opcion no valida, ingrese una opcion correcta del menú")
    return opcion

def menu():
    '''Funcion para mostrar menu'''
    opcion = 0
    while opcion < 1 or opcion > 8:
        try:
            opcion = int(input('''##### MENU ##### \n
            1. Ingresar dinero\n
            2. Realizar transferencia\n
            3. Resumen de cuenta\n
            4. Control de Gastos\n
            5. Calculo de Gastos Compartidos\n
            6. Inversión a Plazo Fijo\n
            7. Planificacion de Ahorro\n
            8. Salir\n'''))
        except ValueError:
            opcion = -1
        if opcion < 1 or opcion > 8:
            print("Opcion no valida, ingrese una opcion correcta del menú")
    return opcion

def main():
    '''Funcion principal que ejecuta el codigo'''
    db_datos = cargar_db()
    usuarios_set = set(db_datos["usuarios"].keys())
    log_in_opcion = 0
    while log_in_opcion < 1 or log_in_opcion > 2:
        try:
            log_in_opcion = int(input('''Desea Crear usuario o Iniciar sesion? \n
            1. Crear Usuario\n
            2. Iniciar Sesion\n'''))
        except ValueError:
            print("Opcion no valida, ingrese una opcion correcta del menú")
    if log_in_opcion == 1:
        nuevo_usuario(db_datos, usuarios_set)
        seguir = None
        while seguir not in [1,2]:
            try:
                seguir = int(input('''Desea Iniciar sesion? \n
                1. Si\n
                2. No\n'''))
            except ValueError:
                print("Opcion no valida, ingrese una opcion correcta del menú")
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
    if usuario['es_admin']:
        while menu_opcion > 0 and menu_opcion < 11:
            menu_opcion = menu_administrador()
            if menu_opcion == 1:
                ingresar_dinero(usuario)
                persistir_datos(db_datos)
            elif menu_opcion == 2:
                realizar_transferencia(usuario, db_datos)
                persistir_datos(db_datos)
            elif menu_opcion == 3:
                resumen_cuenta(usuario)
            elif menu_opcion == 4:
                control_gatos(usuario)
            elif menu_opcion == 5:
                gastos_compartidos()
            elif menu_opcion == 6:
                inversiones(usuario)
                persistir_datos(db_datos)
            elif menu_opcion == 7:
                objetivo_ahorro(usuario)
            elif menu_opcion == 8:
                ver_dinero_depositado_en_banco(db_datos)
            elif menu_opcion == 9:
                ver_cantidad_usuarios(db_datos)
            elif menu_opcion == 10:
                ganancia_banco(db_datos)
            elif menu_opcion == 11:
                print("Gracias por usar el servicio")
            seguir = input("Desea hacer alguna otra operacion? s/n ")
            if seguir == "n":
                print("Gracias por usar el servicio")
                menu_opcion = 100
    else:
        while menu_opcion > 0 and menu_opcion < 9:
            menu_opcion = menu()
            if menu_opcion == 1:
                ingresar_dinero(usuario)
                persistir_datos(db_datos)
            elif menu_opcion == 2:
                realizar_transferencia(usuario, db_datos)
                persistir_datos(db_datos)
            elif menu_opcion == 3:
                resumen_cuenta(usuario)
            elif menu_opcion == 4:
                control_gatos(usuario)
            elif menu_opcion == 5:
                gastos_compartidos()
            elif menu_opcion == 6:
                inversiones(usuario)
                persistir_datos(db_datos)
            elif menu_opcion == 7:
                objetivo_ahorro(usuario)
            elif menu_opcion == 8:
                print("Gracias por usar el servicio")
            seguir = input("Desea hacer alguna otra operacion? s/n ")
            if seguir == "n":
                print("Gracias por usar el servicio")
                menu_opcion = 100

main()