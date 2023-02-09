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
    print('El dado ha sido lanzado: "Que comience el Juego"')
    print("Dispones de 3 Vidas es la regla de todos los juegos mala suerte")
    print("Cada fallo te restara una vida, a continuacion se te dara una pista")
    print(caras[caraRandom])

dados()