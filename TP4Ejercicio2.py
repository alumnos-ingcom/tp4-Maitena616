################
# Maitena Rue - @Maitena616
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from TP4Ejercicio1 import ingreso_entero,IngresoIncorrecto

def suma_lenta(numero, otro_numero):
    limite = otro_numero     
    if otro_numero < 0:           
        limite *= -1
        
          for i in range(limite):
        if otro_numero < 0:
            resultado = numero - i-1
            print(f'{numero-i} + (-1) = {resultado}')
        else:
            resultado = numero + i+1
            print(f'{numero+i} + 1 = {resultado}')
    return resultado
            
def prueba():
   print('Ingrese 2 numeros para sumarlos ')
   numero = ingreso_entero('Ingrese un numero')
   otro_numero = ingreso_entero('Ingrese otro numero')
   suma_lenta(numero, otro_numero)
      
   
    for i in range(limite):
        if otro_numero < 0:
            resultado = numero - i-1
            print(f'{numero-i} + (-1) = {resultado}')
        else:
            resultado = numero + i+1
            print(f'{numero+i} + 1 = {resultado}')
    return resultado
            
def prueba():
   print('Ingrese 2 numeros para sumarlos ')
   numero = ingreso_entero('Ingrese un numero')
   otro_numero = ingreso_entero('Ingrese otro numero')
   suma_lenta(numero, otro_numero)
      
if __name__ == "__main__":        
    prueba()
    
