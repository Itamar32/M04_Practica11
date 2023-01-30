""" aquest arxiu s’hi crearà una funció on demanarà que insereixin un nom dels 5 que es proposin.ç
 Depenent del nom que indiqui s’hi mostrarà, per consola, un missatge diferent."""

def decide():
    word1='Halabusa'
    word2='Python'
    word3='Oximoron'
    action= 'Correr'
    action2='Muerte'
    question= input(f'Escoge una de estas palabras:\n{word1} {word2} {word3} {action} {action2}\nEscribe una de ellas '
                    f'y acepta tu destino: ')
    if(question==word1):
        print('Que fiestero eres bribon!\n')
    elif(question==word2):
        print('Que el buen código te acompañe\n!')
    elif(question==word3):
        print('Oximoron: Dicese cuando un juego de palabras genera un significado nuevo aunque contradictorio a primera vista.'
              'Por ejemplo: Luz oscura\n')
    elif(question==action):
        print('A salir a correr toca!\n')
    elif(question==action2):
        print('Que turbio eres poniendo eso o.O\n')
    else:
        print('No has escrito nada que me sirva, vuelve a probarlo.\n')


