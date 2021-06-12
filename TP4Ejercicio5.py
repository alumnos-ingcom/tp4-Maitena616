################
# Rue Maitena- @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4Ejercicio1 import ingreso_entero

def signo(numero):
    if numero > 0:
        return '+'
    elif numero < 0:
        return '-'
    else:
        return '='

def prueba():
    print('Numeros positivos y negativos')
    numero = ingreso_entero('Ingrese un numero')
    
    if signo(numero) == '+':
        print('Es positivo')
    elif signo(numero) == '-':
        print('Es negativo')
    else:
        print('Es igual a cero')

if __name__ == "__main__":
    prueba()
    
    
