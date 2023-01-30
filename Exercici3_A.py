"""aquest arxiu s’hi crearà una funció la qual li demanarà al client que indiqui un número entre 0 i 100.
He añadido el juego de contadores para darle algo de gracia. """

import random
def numeros():
    numbers= random.randrange(0,100)
    print('Adivina el numero que va de 0 a 100, tienes 7 intentos.')
    contador=7
    while(contador>0):
        intento= int(input(f'Tienes {contador} intentos, que numero crees que es?: '))
        if (intento<numbers):
            contador-=1
            print(f'El numero buscas es mayor, te quedan {contador} intentos.')
        if (intento>numbers):
            contador -= 1
            print(f'El numero que buscas es menor, te quedan {contador} intentos.')
        if(intento==numbers):
            print(f'Enhorabuena!! {numbers} era el numero que buscabas!')
            print(f'Te han sobrado {contador} intentos')
            break
        if(contador==0):
            print('Oooh te has quedado sin intentos :(')

