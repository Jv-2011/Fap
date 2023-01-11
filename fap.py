#Esta libreria permite utilizar alguna funciones del sistema operativo
import os

#Funcion que identifica el sistema operativo y limpia la consola cada vez que se ejecuta
def borrarPantalla():
    if (os.name == "posix"): #si el OS es basado en unix ejecuta "clear"
        os.system ("clear")
    elif (os.name == "ce" or os.name == "nt" or os.name == "dos"):# sie el OS es windows ejecuta "cls"
        os.system ("cls")

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
    1 : ["Diego", 15, "diego123", 0 ,{'2022/10':['01 22:53:14', 25000]}],
    2 : ["Roberto", 15, "roberto123", 0 ,{'2022/10':['25 12:56:14', 50000]}],
    3 : ["Daniela", 15, "daniela123", 0 ,{'2022/10':['25 12:56:14', 150000]}],
    4 : ["Lina", 15, "lina123", 0 ,{'2022/10':['25 12:56:14', 45000]}],
    5 : ["Jaime", 15, "jaime123", 0 ,{'2022/10':['25 12:56:14', 25000]}],
    6 : ["Diana", 15, "diana123", 0 ,{'2022/10':['25 12:56:14', 30000]}]
}

#En esta variable se alamacena el total de dinero ahorrado en el banco
ahorrosTotales = 325000

def prestamo():
    fap()
    global ahorrosTotales #Llamamos la variable que definimos globalmente para usarla dentro de la funcion
    tipoCliente = int(input("Digite el tipo de cliente\n1.Socios\n2.Terceros\nseleccione una opcion: ")) #Se pregunta al usuario el tipo de cliente que desea realizar el préstamo
    if (tipoCliente == 1): # Si el cliente es un socio
        usuario = int(input("Digite la cedula del socio: "))  #Se le pregunta su cédula
        if (socios[usuario][3] == 0): #Si el socio no tiene prestamos
            disponible = totalAhorradoSocio(usuario) #Con esta información se calcula el total ahorrado por el socio para determinar cuanto dinero puede prestar
            disponible *= 0.9
            disponible = int(disponible)
            while True:
                print("Hay disponible para prestar: ", disponible)
                cantidadPrestamo = int(input("Digite la cantidad a prestar: "))
                cuotas = int(input("Digite la cantidad de cuotas: "))
                if (cantidadPrestamo <= disponible): #Si el monto solicitado es menor al disponible.
                    socios[usuario][3] = [cantidadPrestamo, cuotas, 0.01, str(year) + "/" + str(month)] #Entonces se registra en el diccionario socios en la posicion 3
                    ahorrosTotales -= cantidadPrestamo #Se resta la cantidad del prestamo al dinero total del fondo.
                    borrarPantalla()
                    print("Usted ha hecho un prestamo por: $" + str(cantidadPrestamo))
                    menuAdmin()
                    break
                else:
                    print("No se puede prestar esta cantidad")
                    prestamo()
        else: #Si existe un prestamo
            borrarPantalla()
            print("Esta cuenta ya tiene un prestamo")
            menuAdmin()
    elif (tipoCliente == 2): #Si el cliente es un tercero
        cedula = int(input("Digite la cedula del usuario: "))
        nombre = str(input("Digite el nombre del usuario: "))
        edad = int(input("Digite la edad: "))
        password = str(input("Digite la contraseña: ")) #Se le piden unos datos para registrarlo en el diccionario de terceros
        print("Hay disponible para prestar: $", str(ahorrosTotales))
        while True:
            cantidadPrestamo = int(input("Digite la cantidad a prestar: "))
            cuotas = int(input("Digite la cantidad de cuotas: "))
            if (cantidadPrestamo <= ahorrosTotales): #Si la cantidad pedida para el prestamo es menor o igual al total que tiene el fondo
                terceros[cedula] = [nombre, edad, password, [cantidadPrestamo, cuotas, 0.02, str(year) + "/" + str(month)]] #Añade este prestamos a la posicion 3 del usario del diccionario tercero
                print("Usted ha hecho un prestamo por: $" + str(cantidadPrestamo))
                menuAdmin()
                break
            else: #Sino le dira al admin que no puede prestar ese dinero y le pedira de nuevo el valor del prestamo hasta que este sea valido
                borrarPantalla()
                print("No se puede prestar esa  cantidad de dinero")    

#Menu del administrador
def menuAdmin():
    fap()
    opcion = int(input("1.Hacer prestamo\n2.Salir\nseleccione una opcion: "))
    if (opcion == 1):
        borrarPantalla()
        prestamo()
    elif (opcion == 2):
        borrarPantalla()
        menuPrincipal()
    else:
        borrarPantalla()
        print("Digite una opcion correcta")
        menuAdmin()

#Este es el login para los admin
def loginAdmin():
    fap()
    usuarioAdmin = "admin" #Definimos una variable para almacenar el usuario del Admin
    passwordAdmin = "root" #Definimos una variable para almacenar la contraseña del Admin
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
    global year,month #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    for i in socios[cedula]: #Recorre una lista de socios a partir de su cédula
        if isinstance(i,dict): #Para cada elemento de la lista, se verifica si es un diccionario (Si el usuario ya ha realizado algún ahorro en el mes actual)
            x = str(i.keys())
            x = x[11:-2].replace("'", "") #Si lo es, se extrae el año y mes del diccionario y se compara con el año y mes pasados como parámetros
            if (x == (str(year) + "/" + str(month))): #Si coinciden(Si ya tiene un ahorro ese mes), se ejecuta la función menuSocios()
                menuSocios(cedula)
                break
            else: #De lo contrario(Si ese mes no tiene un ahorro), pide un ahorro (con la función ahorro() con la misma cédula como parámetro.)
                ahorro(cedula)
                break

#Esta función permite al usuario ahorrar una cantidad determinada de dinero.
def ahorro(cedula):
    global year,month,day, ahorrosTotales #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    cantidadAhorrar = int(input("Digite una cantidad para ahorrar: "))
    while cantidadAhorrar < 25000: #Para ello, se verifica que la cantidad ingresada sea mayor o igual a 25000.
        print("ingrese un monto igual o superior a 25000")
        cantidadAhorrar = int(input("Digite una cantidad para ahorrar: ")) #Si el usuario ingresa un monto menor, se le solicitará que vuelva a ingresar un monto válido.
    for i in socios[cedula]: #Recorre una lista de socios a partir de su cédula
        if isinstance(i,dict): #Para cada elemento de la lista, se verifica si es un diccionario (Si el usuario ya ha realizado algún ahorro en el mes actual)
            x = str(i.keys())
            x = x[11:-2].replace("'", "") #Si lo es, se extrae el año y mes del diccionario y se compara con el año y mes pasados
            if (x == (str(year) + "/" + str(month))): #Si es así, se agrega la hora actual y la cantidad ahorrada al diccionario correspondiente.
                i[x].append(horaActual())
                i[x].append(cantidadAhorrar)
                ahorrosTotales += cantidadAhorrar
            else: #Si no es así, se creará un nuevo diccionario con la fecha actual, hora actual y la cantidad ahorrada.
                socios[cedula].append({str(year)+"/"+str(month):[horaActual(),cantidadAhorrar]})
                ahorroTotales += cantidadAhorrar
                break
    borrarPantalla()
    print("Usted ha ahorrado existosamente: $" + str(cantidadAhorrar))
    menuSocios(cedula)

#Esta es el menu para los socios que les permite seleccionar una opción del menú para realizar una acción.
def menuSocios(cedula):
    fap()
    opcionClientes = int(input("1.Ahorrar \n2.Pagar cuota\n3.Salir \nSeleccione una opcion: "))
    if (opcionClientes == 1):
        ahorro(cedula)
    elif (opcionClientes == 2):
        cuotasPrestamo(socios, cedula)
    elif (opcionClientes == 3):
        print("\nEl programa ha finalizado\nAdios")
    else:
        print("Seleccione una opcion correcta")
        menuSocios(cedula)

#Este es el menu para terceros,  estos debieron haber sidos registrados por el admin cuando este les hizo el prestamo
def menuTerceros(usuario):
    fap()
    opcionTerceros = int(input("1.Pagar cuota\n2.Salir\nSeleccione una opcion: "))
    if (opcionTerceros == 1):
        cuotasPrestamo(terceros, usuario)
    elif (opcionTerceros == 2):
        menuPrincipal()
    else:
        print("Digite una opcion correcta")
        menuTerceros(usuario)

#Esta funcion permite al usuario hacer login en la aplicacion y asi poder acceder a las diferentes opciones de su cuenta
def login():
    fap()
    usuario = int(input("Digite su usuario (Es su numero de cedula): "))
    passwordLogin = str(input("Digite su contraseña: "))
    if (passwordLogin == socios[usuario][2]):#Este código comprueba si la contraseña ingresada por el usuario es igual a la contraseña almacenada en un diccionario llamado "socios" para el usuario específico. Si las contraseñas coinciden, se ejecuta el código dentro del bloque if.
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
        if (passwordLogin == terceros[usuario][2]): #Este código comprueba si la contraseña ingresada por el usuario es igual a la contraseña almacenada en un diccionario llamado "terceros" para el usuario específico. Si las contraseñas coinciden, se ejecuta el código dentro del bloque if.
            print("Su ingreso ha sido autorizado, bienvenido")
            menuTerceros(usuario)
            break
        else:
            print("Su usuario o su contraseña son incorrectas, digite nuevamente.")

'''Esta función permite al usuario ingresar un valor de ahorro inicial al registrarse, el cual debe ser igual o superior a 25000. Si el valor ingresado es menor, se le solicitará al usuario que ingrese un nuevo valor.
Una vez que el usuario ha ingresado un valor válido, se guardará en la variable "ahorros" como un diccionario con la fecha (año/mes) y la hora actual como clave y el valor del ahorro como valor.
También se sumará el valor del ahorro a la variable "ahorrosTotales". Finalmente, se devolverá el diccionario "ahorros". '''
def ahorroInicial():
    global year,month,day, ahorrosTotales #Llamamos la variables que definimos globalmente para usarlas dentro de la funcion
    ahorro=int(input("Ingrese el valor del ahorro: "))
    while ahorro < 25000:
        print("ingrese un monto igual o superior a 25000")
        ahorro = int(input("Ingrese el valor del ahorro: "))
    ahorros={str(year)+"/"+str(month):[horaActual(),ahorro]} #Es un diccionario que almacena los ahorros de un usuario. El diccionario contiene como clave una cadena de texto formada por el año y el mes actuales, y como valor una lista con dos elementos: la hora actual y el ahorro del usuario.
    ahorrosTotales += ahorro
    return ahorros

'''Esta función muestra un menú con 3 opciones para los clientes. La primera opción es "Registrarme", que al seleccionarla, se le pedirán al usuario los datos de su cédula, nombre, edad y contraseña. Estos datos serán guardados en un diccionario llamado "socios" en el orden [nombre, edad, contraseña, ahorro]. Además se llama a la función "ahorroInicial()" para pedir y almacenar un ahorro inicial igual o mayor a 25000.

La segunda opción es "Iniciar Sesión", que al seleccionarla mostrará un menú con 2 opciones: Socio o Tercero. Si elige Socio se llamará a la función "login()" y si elige Tercero se llamará a la función "loginTerceros()".

La tercera opción es "Salir", que al seleccionarla regresará al menú principal.'''
def menuClientes():
    fap()
    opcionClientes = int(input("1.Registrarme \n2.Iniciar Sesion \n3.Salir \nSeleccione una opcion: "))
    borrarPantalla() #Llamamos la funcion para borrar pantalla de consola cada vez que pasemos de  pagina.
    if (opcionClientes == 1):
        fap()
        cedula = int(input("Digite su cedula: "))
        nombre = str(input("Digite su nombre: "))
        edad = int(input("Digite su edad: "))
        password = str(input("Digite su contraseña: "))
        ahorro = ahorroInicial() #En esta variable ejecutamos la funcion ahorroInicial para pedir y almacenar en esta misma un ahorro inicial que sea igual o mayor a 25000 en el formato de diccionario definido en la funcion para posteriormente almacenarlo en la posicion 4 del diccionario socios.
        socios[cedula] = [nombre, edad, password, 0, ahorro] #Almacenamos todos los datos pedidos para hacer el registro dentro del diccionario socios, siguiendo el orden que ya estaba definido.
    if (opcionClientes == 2):
        fap()
        tipoCliente = int(input("1.Socio\n2.Tercero\n3.Salir\nSeleccione una opcion: "))
        borrarPantalla() #Llamamos la funcion para borrar pantalla de consola cada vez que pasemos de  pagina.
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
    opcion = int(input("1.Cliente\n2.Administrador\n3.Salir\nseleccione una opcion: "))
    borrarPantalla() #Llamamos la funcion para borrar pantalla de consola cada vez que pasemos de  pagina.
    if (opcion == 1):
        menuClientes()
    elif (opcion == 2):
        loginAdmin()
    elif (opcion == 3):
        print("\nEl programa ha finalizado\nAdios  ")
    else:
        print("Digite una opcion correcta")
        menuPrincipal()

borrarPantalla()
menuPrincipal()