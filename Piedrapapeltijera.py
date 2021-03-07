import time

import random


n= input("Introduce tu Nickname: ")

time.sleep(3)

def main():

    
    menu()
    
    seleccion()


def menu():


    print("Bienvenido " + n + "\r\n")

    time.sleep(2.5)

    print("Piedra-Papel-Tijeras \r\n")  
   
    print("1-Jugar")

    print("2-Salir del juego")

    global sel
    sel= int(input("Selecciona una opción con el número que indica: "))

def opcion1():

    print("¡Suerte!")

    x= "Piedra"
    y= "Tijeras"
    z= "Papel"

    print(x)
    print(y)
    print(z)

    resp= input("Elije tu respuesta tal como esta en el menú:  ")

    resp.title()

    while resp!=x and resp!=y and resp!=z:

          resp= input("Elije tu respuesta:  ")

    rspts=["Piedra", "Papel", "Tijeras"]

    v=random.choice(rspts)

    if resp==v:
        print("EMPATE")

        print("El bot a elegido: " + v)

        main()
    
    elif resp==x and v==y:

        print("¡GANASTE!")

        print("El bot a elegido: " + v)

        main()
   
    elif resp==x and v==z:

        print("HAS PERDIDO")

        print("El bot a elegido: " + v)

        main()

    elif resp==y and v==x:

        print("HAS PERDIDO")

        print("El bot a elegido: " + v)

        main()

    elif resp==y and v==z:

        print("HAS GANADO")

        print("El bot a elegido: " + v)

        main()

    elif resp==z and v==x:

        print("El bot a elegido: " + v)

        print("HAS GANADO")

        main()

    elif resp==z and v==y:
         print("HAS PERDIDO")

         print("El bot a elegido: " + v)

         main()

def seleccion():
    if sel == 1:
        opcion1()

    elif sel== 2:

        exit

main()