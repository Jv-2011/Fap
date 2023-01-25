#Con esta libreria contiene una funcion que permite saber la cantidad de dias que tiene un mes dependiendo del año "monthrange(year,month)"
import calendar
#esta libreria contiene funciones para saber la fecha y hora actual "datetime.now()"
from datetime import datetime
#El modulo schedule sirve para programar trabajos cada cierto tiempo
import schedule
#Esta libreria permite utilizar alguna funciones del sistema operativo
import os
#Bajamos la libreria de schedule para programar ciertas acciones cada cierto tiempo
import schedule


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
[cedula]: ["Nombre", edad, contraseña,{'año/mes':['dia hora', ahorro,'dia hora', ahorro]}]'''

socios = {
    1: ["Diego", 15, "diego123", 0, {'2022/10': ['01 22:53:14', 25000]}],
    2: ["Roberto", 15, "roberto123", 0, {'2022/10': ['25 12:56:14', 50000]}],
    3: ["Daniela", 15, "daniela123", 0, {'2022/10': ['25 12:56:14', 150000]}],
    4: ["Lina", 15, "lina123", 0, {'2022/10': ['25 12:56:14', 45000]}],
    5: ["Jaime", 15, "jaime123", 0, {'2022/10': ['25 12:56:14', 25000]}],
    6: ["Diana", 15, "diana123", 0, {'2022/10': ['25 12:56:14', 30000]}]
    1: ["Diego", 15, "diego123", 0, {'2022/10': ['01 22:53:14', 25000]}],
    2: ["Roberto", 15, "roberto123", 0, {'2022/10': ['25 12:56:14', 50000]}],
    3: ["Daniela", 15, "daniela123", 0, {'2022/10': ['25 12:56:14', 150000]}],
    4: ["Lina", 15, "lina123", 0, {'2022/10': ['25 12:56:14', 45000]}],
    5: ["Jaime", 15, "jaime123", 0, {'2022/10': ['25 12:56:14', 25000]}],
    6: ["Diana", 15, "diana123", 0, {'2022/10': ['25 12:56:14', 30000]}]
}

terceros = {

}

#Definimos la fecha actual con variables globales para que puedan ser utilizadas en todo el codigo
year=2022
month=10
day=1

#En esta variable se alamacena el total de dinero ahorrado en el banco
ahorrosTotales = 325000
#Las siguientes tres funciones nos permitiran poder actualizar la fecha automaticamente cada dia hace uso de las variables globales day,month,year

#Esta funcion cambia el año ,se ejecuta cuando la variable month en cambioMes() en el mes 12 haciendo que el mes sea igual a 1, y se pase al año siguiente
def cambioYear():
    global year
    year += 1
#Funcion para actualizar el mes
def cambioMes():
    global month
    if (month == 12):  #si la fecha es el dia 31 del mes 12 la funcion volvera al dia 1ero (Enero)
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
  hora = datetime.now(
  )  #Se obtiene la hora, minuto y segundo con la función datetime.now() de la librería datetime.
  if (day < 10):  #Si el dia es menor al dia 10 del mes
    hora = "0" + str(day) + " " + str(hora.hour) + ":" + str(
      hora.minute
    ) + ":" + str(
      hora.second
    )  #Se añade un 0 al dia y se guarda la informacion de del dia hora:minute:segundo en la variable hora
  else:  #Si el dia es mayor al dia 10 del mes
    hora = str(day) + " " + str(hora.hour) + ":" + str(hora.minute) + ":" + str(
      hora.second
    )  #Se guarda la informacion de del dia hora:minute:segundo en la variable hora
  return (hora)
def imprimirFecha():
    print(str(day)+"/"+str(month)+"/"+str(year))
def menuTiempo():
    borrarPantalla()
    op=0
    while op!=6:
        fap()
        op = int(input("1.fecha/hora Actual \n2.Cambiar fecha \n3.cambio siguiente dia\n4.cambiar siguiente mes\n5.cambiar siguiente año\n6.Atras \nSeleccione una opcion: "))
        if op == 1:
            borrarPantalla()
            print("fecha y la hora actuales:")
            imprimirFecha()
            print(str(horaActual())[2:]+"\n")
        elif op == 2:
            borrarPantalla()
            fijarFecha()
        elif op == 3:
            borrarPantalla()
            print("La fecha y la hora era :")
            imprimirFecha()
            print(str(horaActual())[2:]+"\n")
            cambioDay()
            print("La fecha y la hora actuales es:")
            imprimirFecha()
            print(str(horaActual())[2:]+"\n")
        elif op == 4:
            borrarPantalla()
            print("La fecha y la hora era :")
            imprimirFecha()
            print(str(horaActual())[2:]+"\n")
            cambioMes()
            print("La fecha y la hora actuales es:")
            imprimirFecha()
            print(str(horaActual())[2:]+"\n")
        elif op == 5:
            borrarPantalla()
            print("La fecha y la hora era :")
            imprimirFecha()
            print(str(horaActual())[2:]+"\n")
            cambioYear()
            print("La fecha y la hora actuales es:")
            imprimirFecha()
            print(str(horaActual())[2:]+"\n")
        elif op == 6:
            menuPrincipal()
def fijarFecha():
    global year,month,day
    fap()
    year=int(input("Ingrese el año: "))
    while year<0:
        year=int(input("ingresa de nuevo un valor valido para el año\nIngrese el año: "))
    month=int(input("Ingrese el mes: "))
    while month>12 or month<1:
        month=int(input("ingresa de nuevo un valor valido para el mes\nIngrese el mes: "))
    day=int(input("Ingrese el dia: "))
    while day>(calendar.monthrange(year,month)[1]) and day<1:
        int(input("ingresa de nuevo un valor valido para el dia\nIngrese el dia: "))
#Esta función se encarga de calcular y mostrar la cuota del préstamo que un usuario debe pagar en un mes determinado
cuotaDelmes = 0
gananciaTotal = 0
def cuotasPrestamo(diccionario, usuario):
    fap()
    global ahorrosTotales, cuotaDelmes, gananciaTotal
    fecha = str(year) + "/" + str(month)  #Traemos el año y el mes actual y los almacenamos en la variable fecha
    if (diccionario[usuario][3] == 0):  #Primero, se verifica si el usuario tiene un préstamo asignado.
        borrarPantalla()
        print("\n*No tienes ningun prestamos asignado*\n")
        menu1()
        menuPrincipal()
    else:  #Si tiene un prestamo asignado
        if (fecha in diccionario[usuario][3]):  #Verifica si ya hay un pago
    else:  #Si tiene un prestamo asignado
        if (fecha in diccionario[usuario][3]):  #Verifica si ya hay un pago
            print("Ya pagaste la cuota de este mes")
            if(diccionario == socios):
                menuSocios(usuario)
            elif(diccionario == terceros):
                menuTerceros(usuario)
        else:  #Si no tiene ningun pago
            cuotas = diccionario[usuario][3][1]  #Trae el numero de cuotas del prestamo
            prestamo = diccionario[usuario][3][0]  #Trae la cantidad del prestamo
            interes = diccionario[usuario][3][2] #Trae el interes que tiene que ser aplicado a cada cuota
            cuotas = diccionario[usuario][3][1]  #Trae el numero de cuotas del prestamo
            cuotaPagada = diccionario[usuario][3][4]
            cuotaDelmes = int((prestamo / cuotas) + ((prestamo / cuotas) * interes))
            cuotaCapital = int(prestamo / cuotas)
            cuotaDelMes = int((prestamo / cuotas) + ((prestamo / cuotas) * interes))
            gananciaTotal += cuotaDelmes
            print("¿Desea pagar la cuota del mes?. La cuota de este mes es : $", cuotaDelmes)  #Se muestra el monto de la cuota y se le pregunta al usuario si desea pagarla.
            print("¿Desea pagar la cuota del mes?. La cuota de este mes es : $", cuotaDelMes)  #Se muestra el monto de la cuota y se le pregunta al usuario si desea pagarla.
            cuotaMes = int(input("1.Si\n2.Salir\nSeleccione una opcion: "))
            if (cuotaMes == 1):  #Si la respuesta es afirmativa
                suma = cuotaPagada += 1
                cuotaPagada.insert([4], suma)
                ahorrosTotales += (prestamo / cuotas) + ((prestamo / cuotas) * interes)  #Se actualizan los ahorros totales del fondo sumando el monto de la cuota
                prestamo -= (prestamo / cuotas)  #El préstamo disminuye con el valor de la cuota
                cuotas -= 1
                menuPrincipal()
                diccionario[usuario][3].append(str(year) + "/" + str(month))
                diccionario[usuario][3][4] += 1
                ahorrosTotales += int(cuotaDelMes)  #Se actualizan los ahorros totales del fondo sumando el monto de la cuota
                diccionario[usuario][3][0] -= cuotaCapital  #El préstamo disminuye con el valor de la cuota
                diccionario[usuario][3][1] -= 1
                print(diccionario[usuario][3])
                print(ahorrosTotales)
                if(diccionario == socios):
                    menuSocios(usuario)
                elif(diccionario == terceros):
                    menuTerceros(usuario)
                #Se resta una cuota pendiente
            elif (cuotaMes == 2):  #Sino nos dijirimos al menu de socios
                menuSocios(cedula)
                menuSocios(usuario)
            else:
                print("Digite una opcion correcta")
                cuotasPrestamo(diccionario, usuario)


#Esta funcion nos permite traer la cantidad total que un usuario ha ahorrado
def totalAhorradoSocio(cedula):
  cantidadAhorroTotal = 0
  for i in socios[cedula]:  #Este código recorre una lista de socios
    if (isinstance(
        i, dict)):  #Se comprueba si el elemento actual es un diccionario
      for j in i:  #Si es así, se itera sobre los elementos del diccionario (j)
        for k in range(
            1, len(i[j]), 2
        ):  #Se recorren los elementos del mismo desde la posición 1 hasta la última posición con saltos de 2 en 2 (k)
          cantidadAhorroTotal += int(
            i[j][k])  #se suman los valores a la variable cantidadAhorroTotal
  return cantidadAhorroTotal
    cantidadAhorroTotal = 0
    for i in socios[cedula]:  #Este código recorre una lista de socios
        if (isinstance(i, dict)):  #Se comprueba si el elemento actual es un diccionario
            for j in i:  #Si es así, se itera sobre los elementos del diccionario (j)
                for k in range(1, len(i[j]), 2):  #Se recorren los elementos del mismo desde la posición 1 hasta la última posición con saltos de 2 en 2 (k)
                    cantidadAhorroTotal += int(i[j][k])  #se suman los valores a la variable cantidadAhorroTotal
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
    global ahorrosTotales  #Llamamos la variable que definimos globalmente para usarla dentro de la funcion
    tipoCliente = int(input("Digite el tipo de cliente\n1.Socios\n2.Terceros\nseleccione una opcion: "))  #Se pregunta al usuario el tipo de cliente que desea realizar el préstamo
    if (tipoCliente == 1):  # Si el cliente es un socio
        usuario = int(input("Digite la cedula del socio: "))  #Se le pregunta su cédula
        if (socios[usuario][3] == 0):  #Si el socio no tiene prestamos
            disponible = totalAhorradoSocio(usuario)  #Con esta información se calcula el total ahorrado por el socio para determinar cuanto dinero puede prestar
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
        else:  #Si existe un prestamo
            borrarPantalla()
            print("Esta cuenta ya tiene un prestamo")
            menuAdmin()
    elif (tipoCliente == 2):  #Si el cliente es un tercero
    elif (tipoCliente == 2):  #Si el cliente es un tercero
        cedula = int(input("Digite la cedula del usuario: "))
        nombre = str(input("Digite el nombre del usuario: "))
        edad = int(input("Digite la edad: "))
        password = str(
        input("Digite la contraseña: "))  #Se le piden unos datos para registrarlo en el diccionario de terceros
        password = str(
        input("Digite la contraseña: "))  #Se le piden unos datos para registrarlo en el diccionario de terceros
        print("Hay disponible para prestar: $", str(ahorrosTotales))
        while True:
            cantidadPrestamo = int(input("Digite la cantidad a prestar: "))
            cuotas = int(input("Digite la cantidad de cuotas: "))
            if (cantidadPrestamo <= ahorrosTotales):  #Si la cantidad pedida para el prestamo es menor o igual al total que tiene el fondo
                terceros[cedula] = [nombre, edad, password,[cantidadPrestamo, cuotas, 0.02,str(year) + "/" + str(month)]]  #Añade este prestamos a la posicion 3 del usario del diccionario tercero
                ahorrosTotales -= cantidadPrestamo
                print("PRUEBAA",ahorrosTotales) #borrar despues de prueba
            if (cantidadPrestamo <= ahorrosTotales):  #Si la cantidad pedida para el prestamo es menor o igual al total que tiene el fondo
                terceros[cedula] = [nombre, edad, password,[cantidadPrestamo, cuotas, 0.02,str(year) + "/" + str(month)]]  #Añade este prestamos a la posicion 3 del usario del diccionario tercero
                ahorrosTotales -= cantidadPrestamo
                print("PRUEBAA",ahorrosTotales) #borrar despues de prueba
                print("Usted ha hecho un prestamo por: $" + str(cantidadPrestamo))
                menuAdmin()
                break
            else:#Sino le dira al admin que no puede prestar ese dinero y le pedira de nuevo el valor del prestamo hasta que este sea   valido
            else:#Sino le dira al admin que no puede prestar ese dinero y le pedira de nuevo el valor del prestamo hasta que este sea   valido
                borrarPantalla()
                print("No se puede prestar esa  cantidad de dinero")
cuo = 0
cuoT = 0
proyeccionGanancias = 0
proyeccionTercero = 0
proyeccionSocios = 0
listaT = []
listaS = []
def menuGanancias():
    fap()
    global ahorrosTotales
    global socios
    global cuotaDelmes
    global gananciaTotal
    global cuo
    global cuoT
    global proyeccionGanancias
    global proyeccionSocios
    global proyeccionTercero
    global listaT
    global listaS
    tipoGanancia = int(
    input("Seleccione el tipo de ganancia\n1.Ganancia actual\n2.Proyeccion de la ganancia\n3.Salir\nseleccione una opcion:"))
    if (tipoGanancia == 1):
        print("La ganancia actual es:",gananciaTotal)
        print(terceros)
        menuGanancias()
    if (tipoGanancia == 2):
        for i, value in terceros.items():
            cuoT = 0
            if type(value[3])==list:
                prestamoTerceros = value[3][0]
                cuotasTercero = value[3][1]
                listaT.append(prestamoTerceros)
                print("LISTAAA TERCERO",listaT)
                listaTsuma = (sum(listaT))
                print("LISTA DE TERCEROS",listaTsuma)
                cuoT += cuotasTercero
                proyeccionTercero = ((listaTsuma / cuoT) * (cuoT * 0.02) + listaTsuma)
            print("prestamo tercerooos",prestamoTerceros)
            print("cuotas tercerooos",cuotasTercero)   
        for i, value in socios.items():
            cuo = 0
            proyeccionGanancias = 0
            if type(value[3])==list:
                prestamo = value[3][0]
                cuotas = value[3][1]
                listaS.append(prestamo)
                print("LISTAAA SOCIO",listaS)
                listaSsuma = (sum(listaS))
                #print("LISTA DE SOCIOS",listaT)
                cuo += cuotas
            #print(prestamo)
            #print(cuotas)
                proyeccionSocios = ((listaSsuma / cuo) * (cuo * 0.01) + listaSsuma)
                proyeccionGanancias = proyeccionTercero + proyeccionSocios
                print("proyeccion es",proyeccionGanancias)
        listaS.clear()
        listaT.clear()
        menuGanancias()
    elif (tipoGanancia == 3):
        borrarPantalla()
        menuAdmin() 
def consultaAhorros():
    fap()
    opcion = int(
        input("1.Consultar ahorro de socio\n2.Consultar ahorro total\n3.Salir\nseleccione una opcion: "))
    if(opcion == 1):
        borrarPantalla()
        usuario = int(input("Ingrese la cedula del socio:"))
        total = totalAhorradoSocio(usuario)
        print("el usuario tiene ahorrado",total)
        consultaAhorros()
    elif(opcion == 2):
        print("Los ahorros totales de los socios son:",ahorrosTotales)
        consultaAhorros()
        borrarPantalla()
    elif(opcion == 3):
        borrarPantalla()
        menuAdmin() 
        menuAdmin()
    else:
        print("Ingrese una opcion correcta")
        consultaAhorros()
""" else:   
        borrarPantalla()
        print("no hay datos")
        menuGanancias()
"""
#Menu del administrador
def menuAdmin():
    fap()
    opcion = int(
        input("1.Hacer prestamo\n2.Ganancias\n3.Consultar Ahorros\n4.Configurar fecha\n5.Salir\nseleccione una opcion: "))
    if (opcion == 1):
        borrarPantalla()
        prestamo()
    elif (opcion == 2):
        borrarPantalla()
        menuTiempo()
    elif(opcion == 3):
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
    for i in socios[cedula]:  #Recorre una lista de socios a partir de su cédula
        if isinstance(i, dict):  #Para cada elemento de la lista, se verifica si es un diccionario (Si el usuario ya ha realizado algún ahorro en el mes actual)
    global year, month  #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    for i in socios[cedula]:  #Recorre una lista de socios a partir de su cédula
        if isinstance(i, dict):  #Para cada elemento de la lista, se verifica si es un diccionario (Si el usuario ya ha realizado algún ahorro en el mes actual)
            x = str(i.keys())
            x = x[11:-2].replace("'", "")  #Si lo es, se extrae el año y mes del diccionario y se compara con el año y mes pasados como parámetros
            if (x == (str(year) + "/" + str(month))):  #Si coinciden(Si ya tiene un ahorro ese mes), se ejecuta la función menuSocios()
            x = x[11:-2].replace("'", "")  #Si lo es, se extrae el año y mes del diccionario y se compara con el año y mes pasados como parámetros
            if (x == (str(year) + "/" + str(month))):  #Si coinciden(Si ya tiene un ahorro ese mes), se ejecuta la función menuSocios()
                menuSocios(cedula)
                break
            else:  #De lo contrario(Si ese mes no tiene un ahorro), pide un ahorro (con la función ahorro() con la misma cédula como parámetro.)
                ahorro(cedula)
                break
        else:  #De lo contrario(Si ese mes no tiene un ahorro), pide un ahorro (con la función ahorro() con la misma cédula como parámetro.)
            ahorro(cedula)
            break

#Esta función permite al usuario ahorrar una cantidad determinada de dinero.
def ahorro(cedula):
    global year, month, day, ahorrosTotales  #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    global year, month, day, ahorrosTotales  #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    cantidadAhorrar = int(input("Digite una cantidad para ahorrar: "))
    while cantidadAhorrar < 25000:  #Para ello, se verifica que la cantidad ingresada sea mayor o igual a 25000.
    while cantidadAhorrar < 25000:  #Para ello, se verifica que la cantidad ingresada sea mayor o igual a 25000.
        print("ingrese un monto igual o superior a 25000")
        cantidadAhorrar = int(
        input("Digite una cantidad para ahorrar: ")
        )  #Si el usuario ingresa un monto menor, se le solicitará que vuelva a ingresar un monto válido.
    for i in socios[cedula]:  #Recorre una lista de socios a partir de su cédula
        if isinstance(i, dict):  #Para cada elemento de la lista, se verifica si es un diccionario (Si el usuario ya ha realizado algún ahorro en el mes actual)
        cantidadAhorrar = int(
        input("Digite una cantidad para ahorrar: ")
        )  #Si el usuario ingresa un monto menor, se le solicitará que vuelva a ingresar un monto válido.
    for i in socios[cedula]:  #Recorre una lista de socios a partir de su cédula
        if isinstance(i, dict):  #Para cada elemento de la lista, se verifica si es un diccionario (Si el usuario ya ha realizado algún ahorro en el mes actual)
            x = str(i.keys())
            x = x[11:-2].replace("'", "")  #Si lo es, se extrae el año y mes del diccionario y se compara con el año y mes pasados
            if (x == (str(year) + "/" + str(month))):  #Si es así, se agrega la hora actual y la cantidad ahorrada al diccionario correspondiente.
            x = x[11:-2].replace("'", "")  #Si lo es, se extrae el año y mes del diccionario y se compara con el año y mes pasados
            if (x == (str(year) + "/" + str(month))):  #Si es así, se agrega la hora actual y la cantidad ahorrada al diccionario correspondiente.
                i[x].append(horaActual())
                i[x].append(cantidadAhorrar)
            ahorrosTotales += cantidadAhorrar
        else:  #Si no es así, se creará un nuevo diccionario con la fecha actual, hora actual y la cantidad ahorrada.
            socios[cedula].append(
            {str(year) + "/" + str(month): [horaActual(), cantidadAhorrar]})
            ahorrosTotales += cantidadAhorrar
            break
    borrarPantalla()
    print("Usted ha ahorrado existosamente: $" + str(cantidadAhorrar))
    menuSocios(cedula)

#Esta es el menu para los socios que les permite seleccionar una opción del menú para realizar una acción.
def menuSocios(cedula):
    fap()
    opcionClientes = int(
        input("1.Ahorrar \n2.Informacion de prestamo\n3.Salir \nSeleccione una opcion: "))
    if (opcionClientes == 1):
        ahorro(cedula)
    elif (opcionClientes == 2):
        borrarPantalla()
        menuPrestamo(cedula, socios)
    elif (opcionClientes == 3):
        print("\nEl programa ha finalizado\nAdios")
        menuPrincipal()
    else:
        print("Seleccione una opcion correcta")
        menuSocios(cedula)

#Este es el menu para terceros,  estos debieron haber sidos registrados por el admin cuando este les hizo el prestamo
def menuTerceros(usuario):
    fap()
    opcionTerceros = int(
        input("1.Informacion de prestamo\n2.Salir\nSeleccione una opcion: "))
    if (opcionTerceros == 1):
        menuPrestamo(usuario, terceros)
    elif (opcionTerceros == 2):
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
    ahorros = {
        str(year) + "/" + str(month): [horaActual(), ahorro]
    }  #Es un diccionario que almacena los ahorros de un usuario. El diccionario contiene como clave una cadena de texto formada por el año y el mes actuales, y como valor una lista con dos elementos: la hora actual y el ahorro del usuario.
    ahorrosTotales += ahorro
    return ahorros

'''Esta función muestra un menú con 3 opciones para los clientes. La primera opción es "Registrarme", que al seleccionarla, se le pedirán al usuario los datos de su cédula, nombre, edad y contraseña. Estos datos serán guardados en un diccionario llamado "socios" en el orden [nombre, edad, contraseña, ahorro]. Además se llama a la función "ahorroInicial()" para pedir y almacenar un ahorro inicial igual o mayor a 25000.
La segunda opción es "Iniciar Sesión", que al seleccionarla mostrará un menú con 2 opciones: Socio o Tercero. Si elige Socio se llamará a la función "login()" y si elige Tercero se llamará a la función "loginTerceros()".
La tercera opción es "Salir", que al seleccionarla regresará al menú principal.'''


def menuClientes():
    fap()
    opcionClientes = int(input("1.Registrarme \n2.Iniciar Sesion\n3.Salir \nSeleccione una opcion: "))
    borrarPantalla() #Llamamos la funcion para borrar pantalla de consola cada vez que pasemos de  pagina.
    if (opcionClientes == 1):
        fap()
        cedula = str(input("Digite su cedula: "))
        nombre = str(input("Digite su nombre: "))
        edad = int(input("Digite su edad: "))
        password = str(input("Digite su contraseña: "))
        ahorro = ahorroInicial()  #En esta variable ejecutamos la funcion ahorroInicial para pedir y almacenar en esta misma un ahorro inicial que sea igual o mayor a 25000 en el formato de diccionario definido en la funcion para posteriormente almacenarlo en la posicion 4 del diccionario socios.
        socios[cedula] = [nombre, edad, password, 0, ahorro]  #Almacenamos todos los datos pedidos para hacer el registro dentro del diccionario socios, siguiendo el orden que ya estaba definido.
        menuPrincipal()
    elif (opcionClientes == 2):
        fap()
        tipoCliente = int(
        input("1.Socio\n2.Tercero\n3.Salir\nSeleccione una opcion: "))
        borrarPantalla()  #Llamamos la funcion para borrar pantalla de consola cada vez que pasemos de  pagina.
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
        print("Digite una opcion correcta 6")
        menuPrincipal()
        
        
borrarPantalla()
menuPrincipal()