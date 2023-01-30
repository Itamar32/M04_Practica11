def granpeq(): #Esta función te dice que número es mayor que otro
    a = input('Por favor introduce un número : ' )#Estos input actúan como un escaner para leer un valor introducido
    b = input('Por favor introduze otro número : ')
    if(a==b):
        # Si los números son iguales la función no devolverá nada
        mensaje=''
    elif(a>b):
        mensaje='El número mayor es {a} y el menor es {b} '.format(b=b,a=a)
    else:
        mensaje='El número mayor es {b} y el menor es {a} '.format(a=a,b=b)
    return mensaje

#Esta es la prueba de si la función devuelve una respuesta correcta
print(granpeq())