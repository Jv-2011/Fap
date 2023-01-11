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