#Con esta libreria contiene una funcion que permite saber la cantidad de dias que tiene un mes dependiendo del año "monthrange(year,month)"
import calendar

#esta libreria contiene funciones para saber la fecha y hora actual "datetime.now()"
from datetime import datetime

#El modulo schedule sirve para programar trabajos cada cierto tiempo
import schedule

#Esta libreria permite utilizar alguna funciones del sistema operativo
import os

#Funcion que identifica el sistema operativo y limpia la consola cada vez que se ejecuta
def borrarPantalla():
    if (os.name == "posix"):  #si el OS es basado en unix ejecuta "clear"
        os.system("clear")
    elif (os.name == "ce" or os.name == "nt"or os.name == "dos"):  # sie el OS es windows ejecuta "cls"
        os.system("cls")

#Imprime en pantalla una imagen formada con caracteres del banco
def fap():
    print("    ███████╗░█████╗░██████╗░")
    print("    ██╔════╝██╔══██╗██╔══██╗")
    print("    █████╗░░███████║██████╔╝")
    print("    ██╔══╝░░██╔══██║██╔═══╝░")
    print("    ██║░░░░░██║░░██║██║░░░░░")
    print("    ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░\n")
    print("  Fondo de Ahorros y Prestamos\n")

'''Este diccionario cumple la funcion de base de datos, donde vamos a almacenar cada cliente y sus datos correspondientes en un diccionario en el siguiente formato llave = cedula  valor = arreglo con datos [cedula]: [Nombre, edad, contraseña,prestamos, ahorro1,ahorro2,ahorro3...].
Los ahorros se guardan apartir de la cuarta posicion en un diccionario en donde la llave es
el mes y el año actual (año/mes) y su valor es un arreglo en donde se almacena el dia y la hora del ahorro (posiciones pares)
y el valor de del ahorro(posiciones impares) {'año/mes':['dia hora', ahorro, 'dia hora', ahorro]}].
De es esta manera quedara asi un par llave-valor  en el diccionario socios:
[cedula]: ["Nombre", edad, contraseña, [30000, 5, 0.02, mes/año, 0] ,{'año/mes':['dia hora', ahorro,'dia hora', ahorro]}]'''
socios = {
    1: ["Diego", 75, "diego123", 0, {'2022/10': ['01 22:53:14', 25000]}],
    2: ["Roberto", 45, "roberto123", 0, {'2022/10': ['25 12:56:14', 50000]}],
    3: ["Daniela", 33, "daniela123", 0, {'2022/10': ['25 12:56:14', 150000]}],
    4: ["Lina", 28, "lina123", 0, {'2022/10': ['25 12:56:14', 45000]}],
    5: ["Jaime", 60, "jaime123", 0, {'2022/10': ['25 12:56:14', 25000]}],
    6: ["Diana", 54, "diana123", 0, {'2022/10': ['25 12:56:14', 30000]}]
}

terceros = {}

#Definimos la fecha actual con variables globales para que puedan ser utilizadas en todo el codigo
year = 2022
month = 10
day = 1

#En esta variable se alamacena el total de dinero ahorrado en el banco
ahorrosTotales = 325000

listaT = [] # Esta lista va almacenando los prestamos de los terceros junto con sus intereses
listaS = [] # Esta lista va almacenando los prestamos de los socios junto con sus intereses
sumaTotalTerceros = 0 # Esta variable suma el total de los prestamos con los intereses de los terceros
sumaTotalSocios = 0 # Esta variable suma el total de los prestamos con los intereses de los socios
proyeccionGanancias = 0 # Esta variable guarda el monto total de las sumas de los prestamos tanto de socios como de terceros
gananciaTotal = 0 # Esta variable almacena las cuotas que se van pagando tanto de socios como de terceros

#Las siguientes tres funciones nos permitiran poder actualizar la fecha automaticamente cada dia hace uso de las variables globales day,month,year
#Esta funcion cambia el año ,se ejecuta cuando la variable month en cambioMes() en el mes 12 haciendo que el mes sea igual a 1, y se pase al año siguiente
def cambioYear():
    global year
    year += 1

#Funcion para actualizar el mes
def cambioMes():
    global month
    if (month == 12):  #si la fecha es el dia 31 del mes 12 la funcion volvera al dia 1ero (Enero)
        month = 1
        cambioYear()
    else:
        month += 1

#Esta funcion nos indica si es el ultimo dia del mes dependiendo del año,en caso de ser asi el dia sera cambiado a 1 y se pasara al siguiente mes
def cambioDay():
    global day, month, year
    if (day == (calendar.monthrange(year, month)[1])):
        day = 1
        cambioMes()
    else:
        day += 1

#Esta linea de codigo ejecuta cambioDay() cada dia por medio de la libreria schedule para que actualice el dia en la fecha.
schedule.every().day.do(cambioDay)

#Esta función se encarga de obtener la hora actual y devolverla en un formato específico.
def horaActual():
    global day  #Llamamos la variable global day para obtener el dia del mes.
    hora = datetime.now()  #Se obtiene la hora, minuto y segundo con la función datetime.now() de la librería datetime.
    if (day < 10):  #Si el dia es menor al dia 10 del mes
        hora = "0" + str(day) + " " + str(hora.hour) + ":" + str(hora.minute) + ":" + str(hora.second)  #Se añade un 0 al dia y se guarda la informacion de del dia hora:minute:segundo en la variable hora
    else:  #Si el dia es mayor al dia 10 del mes
        hora = str(day) + " " + str(hora.hour) + ":" + str(hora.minute) + ":" + str(hora.second)  #Se guarda la informacion de del dia hora:minute:segundo en la variable hora
    return (hora)

def menuTiempo():
    fap()
    op = int(input("1.fecha/hora Actual\n2.cambiar siguiente mes\n3.Atras\nSeleccione una opcion: "))
    if(op == 1):
        borrarPantalla()
        print("La fecha y hora actual es: " + (str(day)+"/"+str(month)+"/"+str(year)))
        menuTiempo()
    elif(op == 2):
        borrarPantalla()
        cambioMes()
        menuTiempo()
    elif(op == 3):
        borrarPantalla()
        menuAdmin()
    else:
        borrarPantalla()
        print("Digite una opcion correcta")
        menuTiempo()

#Esta función se encarga de calcular y mostrar la cuota del préstamo que un usuario debe pagar en un mes determinado
def cuotasPrestamo(diccionario, usuario):
    fap()
    global ahorrosTotales, gananciaTotal
    fecha = str(year) + "/" + str(month)  #Traemos el año y el mes actual y los almacenamos en la variable fecha
    if (diccionario[usuario][3] == 0):  #Primero, se verifica si el usuario tiene un préstamo asignado.
        borrarPantalla()
        print("\n*No tienes ningun prestamos asignado*\n")
        menuPrincipal()
    else:  #Si tiene un prestamo asignado
        if (fecha in diccionario[usuario][3]):  #Verifica si ya hay un pago
            print("Ya pagaste la cuota de este mes")
            if(diccionario == socios):
                menuSocios(usuario)
            elif(diccionario == terceros):
                menuTerceros(usuario)
        else:  #Si no tiene ningun pagoprestamo = diccionario[usuario][3][0]  #Trae la cantidad del prestamo
            prestamo = diccionario[usuario][3][0]  #Trae la cantidad del prestamo
            interes = diccionario[usuario][3][2] #Trae el interes que tiene que ser aplicado a cada cuota
            cuotas = diccionario[usuario][3][1]  #Trae el numero de cuotas del prestamo
            cuotaCapital = int(prestamo / cuotas)
            cuotaDelMes = int((prestamo / cuotas) + ((prestamo / cuotas) * interes))
            gananciaTotal += cuotaDelMes
            print("¿Desea pagar la cuota del mes?. La cuota de este mes es : $", cuotaDelMes)  #Se muestra el monto de la cuota y se le pregunta al usuario si desea pagarla.
            cuotaMes = int(input("1.Si\n2.Salir\nSeleccione una opcion: "))
            if (cuotaMes == 1):  #Si la respuesta es afirmativa
                diccionario[usuario][3].append(str(year) + "/" + str(month))
                diccionario[usuario][3][4] += 1
                ahorrosTotales += int(cuotaDelMes)  #Se actualizan los ahorros totales del fondo sumando el monto de la cuota
                diccionario[usuario][3][0] -= cuotaCapital  #El préstamo disminuye con el valor de la cuota
                diccionario[usuario][3][1] -= 1
                if(diccionario == socios):
                    menuSocios(usuario)
                elif(diccionario == terceros):
                    menuTerceros(usuario)
                #Se resta una cuota pendiente
            elif (cuotaMes == 2):  #Sino nos dijirimos al menu de socios
                menuSocios(usuario)
            else:
                print("Digite una opcion correcta")
                cuotasPrestamo(diccionario, usuario)


#Esta funcion nos permite traer la cantidad total que un usuario ha ahorrado
def totalAhorradoSocio(cedula):
    cantidadAhorroTotal = 0
    for i in socios[cedula]:  #Este código recorre una lista de socios
        if (isinstance(i, dict)):  #Se comprueba si el elemento actual es un diccionario
            for j in i:  #Si es así, se itera sobre los elementos del diccionario (j)
                for k in range(1, len(i[j]), 2):  #Se recorren los elementos del mismo desde la posición 1 hasta la última posición con saltos de 2 en 2 (k)
                    cantidadAhorroTotal += int(i[j][k])  #se suman los valores a la variable cantidadAhorroTotal
    return cantidadAhorroTotal


#Esta funcion permite al administrador hacer un prestamo a un cliente, ya sea un socio o un tercero
def prestamo():
    fap()
    global ahorrosTotales  #Llamamos la variable que definimos globalmente para usarla dentro de la funcion
    tipoCliente = int(input("Digite el tipo de cliente\n1.Socios\n2.Terceros\nseleccione una opcion: "))  #Se pregunta al usuario el tipo de cliente que desea realizar el préstamo
    if (tipoCliente == 1):  # Si el cliente es un socio
        usuario = int(input("Digite la cedula del socio: "))  #Se le pregunta su cédula
        if (socios[usuario][3] == 0):  #Si el socio no tiene prestamos
            disponible = totalAhorradoSocio(usuario)  #Con esta información se calcula el total ahorrado por el socio para determinar cuanto dinero puede prestar
            disponible *= 0.9
            disponible = int(disponible)
            while True:
                print("Hay disponible para prestar: ", disponible)
                cantidadPrestamo = int(input("Digite la cantidad a prestar: "))
                cuotas = int(input("Digite la cantidad de cuotas: "))
                if (cantidadPrestamo <=disponible):  #Si el monto solicitado es menor al disponible.
                    socios[usuario][3] = [cantidadPrestamo, cuotas, 0.01,str(year) + "/" + str(month), 0]  #Entonces se registra en el diccionario socios en la posicion 3
                    ahorrosTotales -= cantidadPrestamo  #Se resta la cantidad del prestamo al dinero total del fondo.
                    borrarPantalla()
                    print("Usted ha hecho un prestamo por: $" + str(cantidadPrestamo))
                    menuAdmin()
                    break
                else:
                    print("No se puede prestar esta cantidad")
                    prestamo()
        else:  #Si existe un prestamo
            borrarPantalla()
            print("Esta cuenta ya tiene un prestamo")
            menuAdmin()
    elif (tipoCliente == 2):  #Si el cliente es un tercero
        cedula = int(input("Digite la cedula del usuario: "))
        nombre = str(input("Digite el nombre del usuario: "))
        edad = int(input("Digite la edad: "))
        password = str(
        input("Digite la contraseña: "))  #Se le piden unos datos para registrarlo en el diccionario de terceros
        print("Hay disponible para prestar: $", str(ahorrosTotales))
        while True:
            cantidadPrestamo = int(input("Digite la cantidad a prestar: "))
            cuotas = int(input("Digite la cantidad de cuotas: "))
            if (cantidadPrestamo <= ahorrosTotales):  #Si la cantidad pedida para el prestamo es menor o igual al total que tiene el fondo
                terceros[cedula] = [nombre, edad, password,[cantidadPrestamo, cuotas, 0.02,str(year) + "/" + str(month)]]  #Añade este prestamos a la posicion 3 del usario del diccionario tercero
                ahorrosTotales -= cantidadPrestamo
                borrarPantalla()
                print("Usted ha hecho un prestamo por: $" + str(cantidadPrestamo))
                menuAdmin()
                break
            else:#Sino le dira al admin que no puede prestar ese dinero y le pedira de nuevo el valor del prestamo hasta que este sea   valido
                borrarPantalla()
                print("No se puede prestar esa  cantidad de dinero")

#Esta funcion permite al administrador poder ver las ganancias actuales y tambien la proyeccion de las ganancias (cuotas que deben pagar) tanto de los socios como los terceros
def menuGanancias():
    fap()
    global ahorrosTotales, gananciaTotal, proyeccionGanancias, listaT, listaS, sumaTotalTerceros,sumaTotalSocios #Llamamos las variables que definimos globalmente para usarla dentro de la funcion
    tipoGanancia = int(input("Seleccione el tipo de ganancia\n1.Ganancia actual\n2.Proyeccion de la ganancia\n3.Salir\nseleccione una opcion:")) #Se le pregunta al administrador que tipo de ganancia desea ver 
    if (tipoGanancia == 1):  # Si quiere ver la ganancia actual
        borrarPantalla()
        print("La ganancia actual es:",gananciaTotal) #Con esta información se muestra el total de la ganancia que se va guardando de la cuota que va pagando el usuario al mes
        menuGanancias()
    elif (tipoGanancia == 2):  # Si quiere ver la proyeccion de la ganancia
        for i, value in terceros.items(): # Recorremos el diccionario terceros para obtener el identificador (ID)
            if type(value[3])==list: # Esta condicion permite comparar si la posicion en la que está es una lista y asi poder recorrer esa lista dentro del diccionario terceros
                prestamoTercero = value[3][0] # Trae la cantidad del prestamo
                cuotasTercero = value[3][1] # Trae el numero de cuotas del prestamo
                interesesTercero = (prestamoTercero * 0.02) * cuotasTercero # Se calcula los intereses del prestamo por la cantidad de cuotas
                total = int(prestamoTercero + interesesTercero) # Se suman los intereses junto al prestamo inicial
                listaT.append(total) # Se agrega ese prestamo junto con sus intereses en la lista
            sumaTotalTerceros = (sum(listaT)) # Se suma todos los prestamos que hayan en la lista
        for i, value in socios.items(): # Recorremos el diccionario socios para obtener el identificador (ID)
            if type(value[3])==list: # Esta condicion permite comparar si la posicion en la que está es una lista y asi poder recorrer esa lista dentro del diccionario socios
                prestamo = value[3][0] # Trae la cantidad del prestamo
                cuotas = value[3][1] # Trae el numero de cuotas del prestamo
                intereses = (prestamo * 0.01) * cuotas # Se calcula los intereses del prestamo por la cantidad de cuotas
                total = int(prestamo + intereses)  # Se suman los intereses junto al prestamo inicial
                listaS.append(total) # Se agrega ese prestamo junto con sus intereses en la lista
            sumaTotalSocios = (sum(listaS)) # Se suma todos los prestamos que hayan en la lista
            proyeccionGanancias = sumaTotalTerceros + sumaTotalSocios # Se suman todos los prestamos de terceros y socios para mostrar la proyeccion de las ganancias
        listaS.clear() # Limpia la lista cada que termina la condicion
        listaT.clear() # Limpia la lista cada que termina la condicion
        borrarPantalla()
        print("La proyeccion de las ganancias es $:",proyeccionGanancias) # Muestra la proyeccion de las ganancias
        menuGanancias()
    elif (tipoGanancia == 3): # Si quiere volver al menu del administrador
        borrarPantalla()
        menuAdmin()

#Esta funcion permite al administrador poder ver los ahorros que tiene cada socio  y los ahorros totales de todos los socios
def consultaAhorros():
    fap()
    opcion = int(input("1.Consultar ahorro de socio\n2.Consultar ahorro total\n3.Salir\nseleccione una opcion: ")) #Se le pregunta al administrador que tipo de ahorro desea ver 
    if(opcion == 1): # Si quiere ver el monto ahorrado de un socio en especifico
        borrarPantalla()
        usuario = int(input("Ingrese la cedula del socio: ")) #Se le pregunta la cédula
        nombreUsuario = socios[usuario][0] # Busca en el diccionario de socios el nommbre mediante la cedula ingresada y se guarda en la variable
        total = totalAhorradoSocio(usuario) # Trae el ahorro del socio mediante la funcion y pasandole como parametro su cedula
        borrarPantalla()
        print("El usuario", nombreUsuario, "tiene ahorrado: $" + str(total)) # Se muestra el nombre del socio y el monto total que tiene ahorrado
        consultaAhorros() # Se devuelve al menu de los ahorros
    elif(opcion == 2): # Si quiere ver el monto total ahorrado de todos los socios
        borrarPantalla()
        print("Los ahorros totales de los socios son: $" + str(ahorrosTotales)) # Se muestra el monto total de todos los socios
        consultaAhorros()
    elif(opcion == 3): # Si quiere volver al menu del administrador
        borrarPantalla()
        menuAdmin()
    else:
        print("Ingrese una opcion correcta") # Se muestra un mensaje cuando no ingresa una opcion correcta
        consultaAhorros()

#Menu del administrador
def menuAdmin():
    fap()
    opcion = int(
        input("1.Hacer prestamo\n2.Ganancias\n3.Consultar Ahorros\n4.Configurar fecha\n5.Atras\nseleccione una opcion: "))
    if (opcion == 1):
        borrarPantalla()
        prestamo()
    elif (opcion == 2):
        borrarPantalla()
        menuGanancias()
    elif (opcion == 3):
        borrarPantalla()
        consultaAhorros()
    elif (opcion == 4):
        borrarPantalla()
        menuTiempo()
    elif(opcion == 5):
        menuPrincipal()
    else:
        borrarPantalla()
        print("Digite una opcion correcta")
        menuAdmin()

#Este es el login para los admin
def loginAdmin():
    fap()
    usuarioAdmin = "admin"  #Definimos una variable para almacenar el usuario del Admin
    passwordAdmin = "root"  #Definimos una variable para almacenar la contraseña del Admin
    usuario = str(input("Digite su usuario: "))
    password = str(input("Digite la contraseña: "))
    if (usuario == usuarioAdmin and password == passwordAdmin):
        borrarPantalla()
        menuAdmin()
    else:
        borrarPantalla()
        print("Su usuario o su contraseña son incorrectas, digite nuevamente")
        loginAdmin()

'''Esta funcion verifica con la cedula si el cliente tiene un diccionario con ahorros del mes en curso,de ser asi se ejecuta el menu de socios,en caso contrario de que no tenga un diccionario (ahorro ese mes) se le pedira obligatoriamente un ahorro por lo cual se mandara a la funcion "ahorro()"'''
def ahorroProgramado(cedula):
    global year, month  #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    llaves=[]
    for i in socios[cedula]:  #Recorre una lista de socios a partir de su cédula
        if isinstance(i, dict):  #Para cada elemento de la lista, se verifica si es un diccionario (Si el usuario ya ha realizado algún ahorro en el mes actual)
            x = str(i.keys())
            x = x[11:-2].replace("'", "")  #Si lo es, se extrae el año y mes del diccionario y se compara con el año y mes pasados como parámetros
            llaves.append(x)
    if ((str(year) + "/" + str(month))in llaves):  #Si coinciden(Si ya tiene un ahorro ese mes), se ejecuta la función menuSocios()
        menuSocios(cedula)
    else:  #De lo contrario(Si ese mes no tiene un ahorro), pide un ahorro (con la función ahorro() con la misma cédula como parámetro.)
        ahorro(cedula)

#Esta función permite al usuario ahorrar una cantidad determinada de dinero.
def ahorro(cedula):
    global year, month, day, ahorrosTotales  #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    cantidadAhorrar = int(input("Digite una cantidad para ahorrar: "))
    while cantidadAhorrar < 25000:  #Para ello, se verifica que la cantidad ingresada sea mayor o igual a 25000.
        print("ingrese un monto igual o superior a 25000")
        cantidadAhorrar = int(input("Digite una cantidad para ahorrar: "))  #Si el usuario ingresa un monto menor, se le solicitará que vuelva a ingresar un monto válido.
    for i in socios[cedula]:  #Recorre una lista de socios a partir de su cédula
        if isinstance(i, dict):  #Para cada elemento de la lista, se verifica si es un diccionario (Si el usuario ya ha realizado algún ahorro en el mes actual)
            x = str(i.keys())
            x = x[11:-2].replace("'", "")  #Si lo es, se extrae el año y mes del diccionario y se compara con el año y mes pasados
            if (x == (str(year) + "/" + str(month))):  #Si es así, se agrega la hora actual y la cantidad ahorrada al diccionario correspondiente.
                i[x].append(horaActual())
                i[x].append(cantidadAhorrar)
                ahorrosTotales += cantidadAhorrar
                break
            else:  #Si no es así, se creará un nuevo diccionario con la fecha actual, hora actual y la cantidad ahorrada.
                socios[cedula].append({str(year) + "/" + str(month): [horaActual(), cantidadAhorrar]})
                ahorrosTotales += cantidadAhorrar
                break
    borrarPantalla()
    print("Usted ha ahorrado existosamente: $" + str(cantidadAhorrar))
    menuSocios(cedula)

def menuPrestamo(cedula, diccionario):
    fap()
    opcion = int(input("1.Pagar cuota \n2.Ver estado\n3.Atras \nSeleccione una opcion:"))
    if(opcion == 1):
        cuotasPrestamo(socios, cedula)
    elif(opcion == 2):
        prestamo = diccionario[cedula][3]
        if(prestamo != 0):
            borrarPantalla()
            print("Tienes un prestamo asignado")
            cuotas = diccionario[cedula][3][1]
            if(cuotas != 0):
                cuotasPagadass = diccionario[cedula][3][4]
                print("Tus cuotas restantes son", cuotas)
                print("Tus cuotas pagadas son", cuotasPagadass)
                menuPrestamo(cedula, diccionario)
            else:
                print("Ya has acabado de pagar tu prestamo")
                menuPrestamo(cedula, diccionario)
        else:
            borrarPantalla()
            print("No tienes un prestamo asignado")
            menuPrestamo(cedula, diccionario)
    elif(opcion == 3):
        if(diccionario == socios):
            menuSocios(cedula)
        elif(diccionario == terceros):
            menuTerceros(cedula)

#Esta funcion me permite cambiar el nombre de un usuario
def cambiarNombre(diccionario, usuario):
    nombre = input("Digite el nuevo nombre que desea tener: ")
    diccionario[usuario][0] = nombre
    print(diccionario[usuario][0])

#Esta es el menu para los socios que les permite seleccionar una opción del menú para realizar una acción.
def menuSocios(cedula):
    fap()
    opcionClientes = int(input("1.Ahorrar \n2.Informacion de prestamo\n3.Cambiar nombre\n4.Atras\nSeleccione una opcion: "))
    if (opcionClientes == 1):
        ahorro(cedula)
    elif (opcionClientes == 2):
        borrarPantalla()
        menuPrestamo(cedula, socios)
    elif (opcionClientes == 3):
        cambiarNombre(socios, cedula)
        menuSocios(cedula)
    elif (opcionClientes == 4):
        print("\nEl programa ha finalizado\nAdios")
        menuPrincipal()
    else:
        print("Seleccione una opcion correcta")
        menuSocios(cedula)

#Este es el menu para terceros,  estos debieron haber sidos registrados por el admin cuando este les hizo el prestamo
def menuTerceros(usuario):
    fap()
    opcionTerceros = int(input("1.Informacion de prestamo\n2.Cambiar nombre\n3.Atras\nSeleccione una opcion: "))
    if (opcionTerceros == 1):
        menuPrestamo(usuario, terceros)
    elif (opcionTerceros == 2):
        cambiarNombre(terceros, cedula)
        menuTerceros(usuario)
    elif (opcionTerceros == 3):
        print("\nEl programa ha finalizado\nAdios")
        menuPrincipal()
    else:
        print("Digite una opcion correcta")
        menuTerceros(usuario)

#Esta funcion permite al usuario hacer login en la aplicacion y asi poder acceder a las diferentes opciones de su cuenta
def login():
    fap()
    usuario = int(input("Digite su usuario (Es su numero de cedula): "))
    passwordLogin = str(input("Digite su contraseña: "))
    if (
        passwordLogin == socios[usuario][2]
    ):  #Este código comprueba si la contraseña ingresada por el usuario es igual a la contraseña almacenada en un diccionario llamado "socios" para el usuario específico. Si las contraseñas coinciden, se ejecuta el código dentro del bloque if.
        print("Su ingreso ha sido autorizado, bienvenido")
        borrarPantalla()
        ahorroProgramado(usuario)
    else:
        borrarPantalla()
        print("Su usuario o su contraseña son incorrectas, digite nuevamente.")
        login()

#Esta función realiza el proceso de inicio de sesión para un tercero. Solicita al usuario que ingrese su número de cédula como usuario y su contraseña. Luego, comprueba si la contraseña ingresada por el usuario coincide con la contraseña almacenada en un diccionario llamado "terceros" para el usuario específico. Si las contraseñas coinciden, se imprime un mensaje de bienvenida y se ejecuta la función menuTerceros() pasando el número de cédula del usuario como parámetro. Si las contraseñas no coinciden, se imprime un mensaje solicitando al usuario que vuelva a ingresar sus credenciales. El ciclo while permite que esta comprobación se repita hasta que el usuario ingrese correctamente sus credenciales.
def loginTerceros():
    fap()
    while True:
        usuario = int(input("Digite su usuario (Es su numero de cedula): "))
        passwordLogin = str(input("Digite su contraseña: "))
        if (passwordLogin == terceros[usuario][2]):  #Este código comprueba si la contraseña ingresada por el usuario es igual a la contraseña almacenada en un diccionario llamado "terceros" para el usuario específico. Si las contraseñas coinciden, se ejecuta el código dentro del bloque if.
            print("Su ingreso ha sido autorizado, bienvenido")
            menuTerceros(usuario)
            break
        else:
            menuClientes()
            print("Su usuario o su contraseña son incorrectas, digite nuevamente.")

'''Esta función permite al usuario ingresar un valor de ahorro inicial al registrarse, el cual debe ser igual o superior a 25000. Si el valor ingresado es menor, se le solicitará al usuario que ingrese un nuevo valor.
Una vez que el usuario ha ingresado un valor válido, se guardará en la variable "ahorros" como un diccionario con la fecha (año/mes) y la hora actual como clave y el valor del ahorro como valor.
También se sumará el valor del ahorro a la variable "ahorrosTotales". Finalmente, se devolverá el diccionario "ahorros". '''
def ahorroInicial():
    global year, month, day, ahorrosTotales  #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    ahorro = int(input("Ingrese el valor del ahorro: "))
    while ahorro < 25000:
        print("ingrese un monto igual o superior a 25000")
        ahorro = int(input("Ingrese el valor del ahorro: "))
    ahorros = {str(year) + "/" + str(month): [horaActual(), ahorro]}  #Es un diccionario que almacena los ahorros de un usuario. El diccionario contiene como clave una cadena de texto formada por el año y el mes actuales, y como valor una lista con dos elementos: la hora actual y el ahorro del usuario.
    ahorrosTotales += ahorro
    return ahorros

'''Esta función muestra un menú con 3 opciones para los clientes. La primera opción es "Registrarme", que al seleccionarla, se le pedirán al usuario los datos de su cédula, nombre, edad y contraseña. Estos datos serán guardados en un diccionario llamado "socios" en el orden [nombre, edad, contraseña, ahorro]. Además se llama a la función "ahorroInicial()" para pedir y almacenar un ahorro inicial igual o mayor a 25000.
La segunda opción es "Iniciar Sesión", que al seleccionarla mostrará un menú con 2 opciones: Socio o Tercero. Si elige Socio se llamará a la función "login()" y si elige Tercero se llamará a la función "loginTerceros()".
La tercera opción es "Salir", que al seleccionarla regresará al menú principal.'''
def menuClientes():
    fap()
    opcionClientes = int(input("1.Registrarme \n2.Iniciar Sesion \n3.Atras \nSeleccione una opcion:"))
    borrarPantalla()  #Llamamos la funcion para borrar pantalla de consola cada vez que pasemos de  pagina.
    if (opcionClientes == 1):
        fap()
        cedula = str(input("Digite su cedula: "))
        nombre = str(input("Digite su nombre: "))
        edad = int(input("Digite su edad: "))
        password = str(input("Digite su contraseña: "))
        ahorro = ahorroInicial()  #En esta variable ejecutamos la funcion ahorroInicial para pedir y almacenar en esta misma un ahorro inicial que sea igual o mayor a 25000 en el formato de diccionario definido en la funcion para posteriormente almacenarlo en la posicion 4 del diccionario socios.
        socios[cedula] = [nombre, edad, password, 0, ahorro]  #Almacenamos todos los datos pedidos para hacer el registro dentro del diccionario socios, siguiendo el orden que ya estaba definido.
        borrarPantalla()
        menuPrincipal()
    elif (opcionClientes == 2):
        fap()
        tipoCliente = int(
        input("1.Socio\n2.Tercero\n3.Salir\nSeleccione una opcion: "))
        borrarPantalla()  #Llamamos la funcion para borrar pantalla de consola cada vez que pasemos de  pagina.
        if (tipoCliente == 1):
            login()
        elif (tipoCliente == 2):
            loginTerceros()
        elif (tipoCliente == 3):
            menuPrincipal()
        else:
            print("Digite una opcion correcta")
            menuClientes()
    elif (opcionClientes == 3):
        borrarPantalla()
        menuPrincipal()
    else:
        print("Digite una opcion correcta")
        menuClientes()

#Funcion que ejecuta el menu principal de la aplicacion de acuerdo al rol que se quiera ingresar
def menuPrincipal():
    fap()
    opcion = int(
    input("1.Cliente\n2.Administrador\n3.Salir\nseleccione una opcion: "))
    borrarPantalla()  #Llamamos la funcion para borrar pantalla de consola cada vez que pasemos de  pagina.
    if (opcion == 1):
        menuClientes()
    elif (opcion == 2):
        loginAdmin()
    elif (opcion == 3):
        print("\nEl programa ha finalizado\nAdios  ")
    else:
        print("Digite una opcion correcta 6")
        menuPrincipal()

borrarPantalla()
menuPrincipal()