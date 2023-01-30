def hacienda():
    '''Esta función te dice si es necesario que hagas o no la declaración de la renta en función
    de la edad y el salario'''
    edad = int(input('Por favor introduce tu edad: ')) #Estos input actúna como un escaner para leer un valor introducido
    salario = int(input('Por favor introduce tu salario: '))
    if(edad>=18 and salario>1200):
       mensaje=('Es necesario que hagas la declaración de la renta ')
    else:
        mensaje=('Aún no puedes hacer la declaración renta')
    return mensaje
#Esta es la prueba de si la función devuelve una respuesta correcta
print(hacienda())
