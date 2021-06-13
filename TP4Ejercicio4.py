################
# Rue Maitena - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4Ejercicio1 import ingreso_entero
 
def compara(numero, otro_numero):
    if numero < otro_numero:
        return -1
    elif numero == otro_numero:
        return 0
    else:
        return 1

def prueba():
    print(f'Comparacion de numeros\n')
    numero = ingreso_entero('Ingrese el primer numero')
    otro_numero = ingreso_entero('Ingrese otro numero')
    resultado = compara(numero, otro_numero)
    print(f'Respuesta: {resultado}')
    
if __name__ == "__main__":
    prueba()
