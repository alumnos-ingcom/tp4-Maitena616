################
# Rue Maitena - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4Ejercicio1 import ingreso_entero,IngresoIncorrecto

def factores_primos(numero):
    if numero <= 0:
        raise IngresoIncorrecto("Enteros positivos!")
    lista = []
    i = 2
    
    while numero >= i:
        if numero % i == 0:       
            numero /= i     
            lista.append(i) 
        else:
            i +=1  
        
    tupla = (lista)
    return tupla
    
def prueba():
    numero = ingreso_entero('Digite un numero entero positivo para devolverlo en factores primos')
    tupla_de_primos = factores_primos(numero)
    print(tupla_de_primos)
 
if __name__ == "__main__":
    prueba()
