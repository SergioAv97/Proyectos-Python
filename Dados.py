'''
Esto es un ejercicio de aprendizaje
Consta de 3 partes:
 - Lanzar un dado con 6 caras
 - Adivinar el resultado, acercando al usuario al resultado si se equivoca
 - Restar una vida, volver a preguntar al usuario hasta que acierte o muera.

Hasta aqui diriamos que el ejercicio te seria util para comprender lo basico sobre el
metodo de bucle "while" y el metodo condicional "if".

Acontinuacion como buen programador debes de pensar que el usuario puede equivocarse
en cualquier cosa, asi que para hacer el ejercicio de 10 debemos de:
 - Controlar que no se introduzca un numero superior a 6 ni inferior a 1
 - Controlar que se introduzca un numero entero
'''

import random

def dados ():
    caras = [1,2,3,4,5,6]
    caraRandom = caras[random.randint(0,5)]
    repetimos = True
    vidas = 3
    print('El dado de 6 caras ha sido lanzado: "Que comience el Juego"')
    print("Dispones de 3 Vidas es la regla de todos los juegos mala suerte")
    print("Cada fallo te restara una vida, a continuacion se te dara una pista")
    print("===================================================================")

    while repetimos:

        print("Introduzca el numero que piensa que ha salido:")
        try:
            numeroUser = int(input())
            if numeroUser > 6:
                print('Humano un dado de 6 cara solo contiene hasta el numero 6')
                print('se coherente he intentalo otra vez')
            else:
                print("numero introducido =", numeroUser )
                print('numero dado', caraRandom)

                if numeroUser == caraRandom:
                    print('MUY BIEN HAS GANADO A LA MAQUINA SOBREVIVES')
                    repetimos = False

                elif(numeroUser != caraRandom):
                    if vidas > 1:
                        vidas = vidas -1
                        print('Vidas:',vidas)
                        if caraRandom < numeroUser:
                            print('Prueba con algo mas pequeño')
                        elif caraRandom > numeroUser:
                            print('prueba con algo mas grande')
                    else:
                        print('La Maquina gana y tu MUERES')
                        repetimos = False

        except ValueError:
            print('Humano si aprecia su vida introduzca una cara del dado')
dados()