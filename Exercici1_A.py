"""aquest arxiu s’hi crearà una funció on demanarà a l’usuari que inserti 2 números
i el programa li dirà quin és el més gran i quin el més petit. Si son iguals sortirà que son iguals.
"""

def mayor():
    print('Introduce por consola dos numeros (A y B) y te diré cual es mayor.\n')
    valor1= int(input('Aporta el valor de A: '))
    valor2= int(input('Ahora introduce el valor de B: '))

    if (valor1 > valor2):
        print(f'El valor A={valor1} es mayor al valor B= {valor2}.\n')

    if (valor2 > valor1):
        print(f'El valor B= {valor2}, es mayor al valor A= {valor1}.\n')

    if(valor1==valor2):
        print('Los numeros introducidos son iguales.\n')


