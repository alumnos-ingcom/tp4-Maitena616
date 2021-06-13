################
# Rue Maitena - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4Ejercicio1 import ingreso_entero,IngresoIncorrecto

def maximo(lista):
    maxx = -999
      
    for item in lista:
        if item > maxx:
            maxx = item
    return maxx


def minimo(lista):
    minimo = 999
    
    for item in lista:
        if item < minimo:
            minimo = item
    return minimo
   
def prueba():
    print('Digite una lista de numeros enteros')
    cantidad_numeros = ingreso_entero('¿Cuantos numeros tendra su lista?')
    
    if cantidad_numeros <= 0:
        raise IngresoIncorrecto("No puede ser menor o igual a 0") 
    
    lista = []
    for i in range(cantidad_numeros):
        n = ingreso_entero(f'Ingrese el numero {i+1}/{cantidad_numeros}')
        lista.append(n)
    
    min_lista = minimo(lista)
    print(f'El minimo de la la lista es: {min_lista}')
    max_lista = maximo(lista)
    print(f'El maximo de la la lista es: {max_lista}')
   
if __name__ == "__main__":
    prueba()
    
    
