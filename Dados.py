'''
Esto es un ejercicio de aprendizaje
Consta de 3 partes:
 - Lanzar un dado con 6 caras
 - Adivinar el resultado, acercando al usuario al resultado si se equivoca
 - Restar una vida, volver a preguntar al usuario hasta que acierte o muera.
'''
import random

def dados ():
    caras = [1,2,3,4,5,6]
    caraRandom = random.randint(0,5)
    repetimos = False
    vidas = 3
    print('El dado ha sido lanzado: "Que comience el Juego"')
    print("Dispones de 3 Vidas es la regla de todos los juegos mala suerte")
    print("Cada fallo te restara una vida, a continuacion se te dara una pista")
    print("===================================================================")
    while repetimos == False:

        print("Introduzca el numero que piensa que ha salido:")
        numeroUser = int(input())
        print("numero introducido =", numeroUser )
        print('numero dado', caraRandom)
        if numeroUser == caraRandom:
            print('MUY BIEN HAS GANADO A LA MAQUINA SOBREVIVES')
            repetimos == True
        elif(numeroUser != caraRandom):
            if vidas != 0:
                vidas = vidas -1
                print('Vidas:',vidas)
                print('Otro Intento')
        elif vidas == 0:
            print('La Maquina gana y tu MUERES')

    print('salida del bucle')
dados()