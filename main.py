import json
from functools import reduce

'''TODO: 
    Repartición de Tareas:
        - Agus Goldberg: 5 y 6
<<<<<<< HEAD
        - Samu: 7 y 8
        - Benja: 3 y 4
        - Agus Lopez: 1 y 2

    Ideas mejoras:
    -Agregar una funcion que quite saldo al usuario y se use en las otras funciones como transferencias o inversiones
        se le pasaria como argumento usuario (para ubicar en la DB), monto (para saber cuanto quitar) y motivo (para saber que tipo de transaccion es)
    - Quizas posibiliadad de comprar Stocks/Crypto
=======
        - Samu:
        - Benja:
        - Agus Lopez: 1 / 2 ../
>>>>>>> fdbfec926a18c54a1beb79776ba2075a95de4fbd

    Tareas:
        1. Agregar validaciones del nuevo usuario (Funciones creadas dentro de la funcion nuevo_usuario)
            - En la funcion "nuevo usuario" crear logica para validar los datos que ingresa el usuario.
            - Las funciones ya estan prehechas, agregar mas de ser necesario.

        2. Crear funcion para ingresar dinero
            - Crear logica para agregar dinero a la cuenta del usuario en la funcion "ingresar_dinero".
            - Tener en cuenta que habria que agregar una transaccion en el usuario por cada ingreso.
            - Que se agregue el ingreso al saldo del usuario.
            - IMPORTANTE: Tener en cuenta que la parte de las transacciones es una matriz.

        3. Crear funcion para realizar transferencia.
            - Crear logica para realizar transferencia entre cuentas dentro de la funcion "realizar_transferencia"
            - Tener en cuenta que esta funcion usa dos parametros, uno es alias porque vamos a buscar el usuario a transferir en nuestro diccionario de usuarios
            - Tener en cuenta que el monto que se transfiere se resta del saldo del usuario que transfiere y se agregan las transacciones pertinentes.
        
        4. Crear funcion para mostrar resumen de cuenta
            - Crear logica en funcion "resumen_cuenta"
            - Por defecto mostrar transacciones del mes en curso o el mes anterior (a definir)
            - Luego de mostrar resumen, crear menu para preguntar si quiere:
                1-Mostrar resumen de transacciones entre un rango de fechas
                2-Mostrar ultimos 5 transacciones (aca aplicamos slicing de la lista)
                3-Mostrar primeras 5 transacciones del mes.
        
        5 - Crear funcion de Control de Gastos.
            - Crear logica donde se muestre gastos total del mes y estilo de gastos basado en las etiquetas de las transacciones de egreso, ejemplo:
                "Se gasto un 20% en comida"
        
        6 - Crear funcion de objetivos de ahorro
            - Permitir al usuario ingresar cuanto desea ahorrar y cuando gana por su sueldo.
            - Basado en eso mostrar cuanto debe ahorrar por dia (o semana, a definir)
            - Basado en los gastos de las etiquetas de gastos donde se deberia recortar mas para cumplir la meta. Ejemplo:
                Reduciendo en x% los gastos de "comida" puees cumplir esta meta.
            
        7 - A checkear, crear funcion para hacer inversiones.
            - Ingresar monto a invertir y crear algoritmo que calcule la ganancia estimada.
        
        8 - Crear funcion para funcion de Gastos compartidos.
            - Permitir al usuario ingresar cantidad de personas a repartir el gasto
            - Ingresar Monto a pagar.
            - Mostar cuanto debe pagar cada persona.

    - FALTA AGREGAR:
        1 - Matrices: Usar en lista de transacciones.               LISTO   - en Gastos Compartidos y Control Gastos
        2 - Listas y sus funciones: ver en que parte usar.          REVISAR - Ingresar Dinero (al menos un append)
        3 - Comprension de Listas:                                  LISTO   - en Gastos Compartidos
        4 - Funciones Lambda y metodos (Map, Filter, Reduce)        LISTO   - en Gastos Compartidos
        5 - Slicing: Podemos usarlo cuando mostremos las transacciones hacer un "mostrar ultimas transacciones" o "mostrar primeras transacciones" siendo la misma lista volteandola con slicing
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
                ["ingreso","deposito","2025-09-02",2000,"ARS","Comida"],
                ["egreso", "pago"    ,"2025-05-22",5000,"ARS","Comida"]
                 ],
            "saldo": 7000
        }
        }
    }
    return db_datos

def nuevo_usuario(db_datos):
    '''Funcion para crear nuevo usuario con validaciones basicas'''
    nombre = input("Ingrese nombre completo: ")
    dni = input("Ingrese DNI: ")

    # validación de nombre de usuario
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

    # validación de contraseña
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

    # validación de email
    valido_email = False
    while valido_email == False:
        email = input("Ingrese email: ")
        if "@" not in email or "." not in email:
            print("El email no es valido")
        else:
            valido_email = True

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

    monto_valido = False
    while monto_valido == False:
        montoo_  = input("Ingrese monto a depositar: ")

        es_numero = True
        if montoo_ == "":
            es_numero = False
        else:
            for c in montoo_:
                if c < "0" or c > "9":
                    es_numero = False

        if es_numero == False:
            print("Monto invalido, ingrese solo numeros")
        else:
            monto = int(montoo_)
            if monto <= 0:
                print("El monto debe ser mayor a 0")
            else:
                monto_valido = True

    fecha = input("Ingrese fecha (AAAA-MM-DD): ")
    etiqueta = input("Ingrese etiqueta (ej: Sueldo, Comida): ")
    if etiqueta == "":
        etiqueta = "Varios"

    transaccion = ["ingreso", "deposito", fecha, monto, "ARS", etiqueta]

    usuario["transacciones"].append(transaccion)
    usuario["saldo"] = usuario["saldo"] + monto

    print("Deposito registrado. Nuevo saldo:", usuario["saldo"])

def realizar_transferencia(alias, monto):
    '''Funcion para realizar transferencia entre cuentas'''
    pass

def control_gatos(fecha_inicio, fecha_final, usuario):  


    '''punto 5'''
    total = 0      
    categorias = {} #ver diccionario para poner categorias

    for i in usuario["transacciones"]: #es usuario o usuarioS?? VER
        tipo = i[0]       # ingreso/egreso
        fecha = i[2]      
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

<<<<<<< HEAD
=======

def objetivo_ahorro(usuario):
        while True:
            monto = input('Ingrese el monto que desea ahorrar (o escriba "salir" para volver): ').lower()
        
            if monto == "salir":
                print("Volviendo al menú anterior...")
                return  
        
            if monto.isdigit():            # chequeo si son solo números
                objetivo = int(monto)
                if objetivo > 0:
                    print("Objetivo registrado:", objetivo)
                    break                  # sale del while, valor correcto
                else:
                    print("El monto debe ser mayor a 0")
            else:
                print("Monto inválido, ingrese solo números o escriba 'salir' ") 
        
        motivo = input("Ingrese el motivo de este ahorro (ejemplo: viaje): ")

        while True:
            periodo = input('¿En cuántos días quiere lograrlo? (o escriba "salir" para volver): ').lower()
            if periodo == "salir":
                print("Volviendo al menú...")
                return
            if periodo.isdigit():
                dias = int(periodo)
                if dias > 0:
                    break
                else:
                    print("Los días deben ser mayor a 0.")
            else:
                print("Valor inválido, ingrese solo números o escriba 'salir'.")

        #calculo cuanto debe ahorra
        saldo_actual = usuario["saldo"]
        restante = objetivo - saldo_actual
        if restante < 0:
            print("\nFelicitaciones! Tienes el dinero disponible para cumplir el objetivo ")
            print("Motivo: ", motivo)
            print("Monto objetivo: ", objetivo)
            print("Saldo actual: ", saldo_actual)
            return 
        ahorro_diario = restante / dias

        #muestro resultados
        print("\n### OBJETIVO DE AHORRO ###")
        print("Motivo:", motivo)
        print("Monto objetivo:", objetivo)
        print("Días para lograrlo:", dias)
        print("Saldo actual:", saldo_actual)
        print("Monto restante:", restante)
        print("Debes ahorrar por día:", ahorro_diario)


        
        

>>>>>>> fdbfec926a18c54a1beb79776ba2075a95de4fbd
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
             
def inversiones(inversion, db_datos, usuario):
    '''Funcion para hacer inversiones a plazo fijo
    TOOD: Agregar cantidad de dias para el plazos fijo y calcular el interes basado en esto(30 dias, 60 dias)'''
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
        db_datos['usuarios'][usuario['nombre_usuario']]['saldo'] -= inversion
        print("Operación confirmada")
    elif opcion == "n":
        print("Operación cancelada")

def menu():
    '''Funcion para mostrar menu'''
    opcion = int(input('''##### MENU ##### \n
    1. Ingresar dinero\n
    2. Realizar transferencia\n
    3. Resumen de cuenta\n
    4. Control de Gastos\n
    5. Calculo de Gastos Compartidos\n
    6. Inversión a Plazo Fijo\n
    7. Salir'''))
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

<<<<<<< HEAD
    menu_opcion = 0
    while menu_opcion != 7:
        menu_opcion = menu()
        if menu_opcion == 1:
            ingresar_dinero()
        elif menu_opcion == 2:
            realizar_transferencia()
        elif menu_opcion == 3:
            resumen_cuenta()
        elif menu_opcion == 4:
            fecha_inicio = int(input('Ingrese fecha inicial de periodo: '))
            fecha_final = int(input('Ingrese fecha final de periodo: '))
            control_gatos(fecha_inicio, fecha_final, usuario)
        elif menu_opcion == 5:
            gastos_compartidos()
        elif menu_opcion == 6:
            print(f"Su saldo es {usuario['saldo']}")
            inversion = 0
            while inversion <= 0 or inversion > usuario['saldo']:
                inversion = int(input("Ingrese monto a invertir: "))
                if inversion <= 0 or inversion > usuario['saldo']:
                    print(f"Monto invalido, ingrese monto mayor a 0 y menor a su saldo actual que es {usuario['saldo']}")
            inversiones(inversion, db_datos, usuario)
            print(db_datos['usuarios'][usuario['nombre_usuario']]['saldo'])
        elif menu_opcion == 7:
            print("Gracias por usar el servicio")
=======

    opcion = menu()
    if opcion == 1:
        ingresar_dinero(usuario)
    elif opcion == 2:
        realizar_transferencia(usuario)
    elif opcion == 3:
        resumen_cuenta(usuario)
    elif opcion == 4:
        fecha_inicio = int(input('Ingrese fecha inicial de periodo: '))
        fecha_final = int(input('Ingrese fecha final de periodo: '))
        control_gatos(fecha_inicio, fecha_final, usuario)
    elif opcion == 5:
        print("Gracias por usar el servicio")
        return

>>>>>>> fdbfec926a18c54a1beb79776ba2075a95de4fbd

main()