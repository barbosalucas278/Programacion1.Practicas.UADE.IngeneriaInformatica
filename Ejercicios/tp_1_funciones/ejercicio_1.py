# 1.  Desarrollar una función que reciba tres números enteros positivos y devuelva el 
# mayor de los tres, sólo si éste es único (es decir el mayor estricto). Devolver -1 en 
# caso de no haber ninguno. No utilizar operadores lógicos (and, or, not). Desarrollar 
# también un programa para ingresar los tres valores, invocar a la función y mostrar 
# el máximo hallado, o un mensaje informativo si éste no existe
import sys
sys.path.append(r'c:\Users\Lucas\Desktop\UADE\Programacion I')
from Libs.terminalHelper import pedir_numero

cantidad_de_numeros = 3
numeros_ingresados = []

def obtener_mayor_estricto(numeros):
    ultimo_mayor = -1
    for n in numeros:
        if n > ultimo_mayor:
            if numeros.count(n) == 1:
                ultimo_mayor = n
    return ultimo_mayor
    
for c in range(cantidad_de_numeros):
    numeros_ingresados.append(pedir_numero())
    
numero_mayor_unico = obtener_mayor_estricto(numeros_ingresados)
print(f'El número mayor sin repetir es: {numero_mayor_unico}' )

