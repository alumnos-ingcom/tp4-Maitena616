################
# Rue Maitena - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################
from TP4Ejercicio1 import ingreso_entero
from TP4Ejercicio6 import maximo, minimo

class IngresoIncorrecto(Exception):
    pass

def ordenar_mayor_a_menor(uno, dos, tres):
    lista = [uno, dos, tres]
    suma = uno + dos + tres
    maxim = maximo(lista)   
    mini = minimo(lista)
    n_medio = suma - mini - maxim
    tupla = (maxim, n_medio, mini)
        
    return tupla

def ordenar_menor_a_mayor(uno, dos, tres):
    lista = [uno, dos, tres]
    suma = uno + dos + tres              
    maxim = maximo(lista)               
    mini = minimo(lista)                 
    n_medio = suma - mini - maxim        
    tupla = (mini, n_medio, maxim)
        
    return tupla
    
            
def prueba():
    print('Ingrese 3 numeros para ordenarlos')
    uno = ingreso_entero('Numero 1')
    dos = ingreso_entero('Numero 2')
    tres = ingreso_entero('Numero 3')
    
    print('Ordenados de mayor a menor')
    tupla = ordenar_mayor_a_menor(uno, dos, tres)
    print(tupla)
    
    print('Ordenados de menor a mayor')
    tupla2 = ordenar_menor_a_mayor(uno, dos, tres)
    print(tupla2)
    
if __name__ == "__main__":        
    prueba()
