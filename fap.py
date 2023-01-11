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