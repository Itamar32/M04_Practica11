def parimpar(): #Esta función te dice si un número es par o impar
    a= int(input('Por favor introduce un número : '))  #Este input actúa como un escaner para leer un valor introducido
    if(a%2 ==0):
        mensaje='{a} es un número par'.format(a=a)
    else:
        mensaje='{a} es un número impar'.format(a=a)
    return mensaje
#Esta es la prueba de si la función devuelve una respuesta correcta
print(parimpar())
