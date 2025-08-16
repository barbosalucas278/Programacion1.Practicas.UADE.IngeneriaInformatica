# Desarrollar cada una de las siguientes funciones y escribir un programa que permi
# ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun
# ción:
#  NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
# sea el valor ingresado
import sys
sys.path.append(r'c:\Users\Lucas\Desktop\UADE\Programacion I')
from Utils.matricesHelper import calcular_porcentaje_impar_por_columna, calcular_promedio, crear_matriz, es_matriz_simetrica, es_matriz_simetrica_secundaria, get_columna_palindromo, swap_columna, swap_fila, trasponer_matriz
from Utils.terminalHelper import pedir_numero

#  a. Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado. 

filas_input = pedir_numero("Ingrese el numero de filas de la  matriz: ")
columnas_input = pedir_numero("Ingrese el numero de columnas de la  matriz: ")

matriz = crear_matriz(filas_input,columnas_input)

swap_fila(matriz, 1, 0)

swap_columna(matriz, 1, 0)

matriz_traspuesta = trasponer_matriz(matriz)    
print(matriz_traspuesta)

for f in range(len(matriz)):
    print(f'El promedio de la fila {f + 1} es {calcular_promedio(matriz[f])}')

for f in range(len(matriz)):
    print(f'El porcentaje de impares de la columna {f + 1} es {calcular_porcentaje_impar_por_columna(matriz,f)}')

matriz_simetrica = [
    [1,9,8,2],
    [9,1,2,8],
    [8,2,1,9],
    [2,8,9,1],
]  
print(es_matriz_simetrica(matriz_simetrica))    

matriz_simetrica = [
    [1,9,8,2],
    [9,1,2,8],
    [8,2,1,9],
    [2,8,9,1],
]  
print(es_matriz_simetrica_secundaria(matriz_simetrica))  

matriz_simetrica = [
    [1,9,8,2],
    [9,1,2,8],
    [9,2,1,8],
    [1,8,9,2],
]  
print(get_columna_palindromo(matriz_simetrica))  
print(matriz)