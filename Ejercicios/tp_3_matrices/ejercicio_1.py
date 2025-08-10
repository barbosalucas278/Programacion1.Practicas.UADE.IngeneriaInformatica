# Desarrollar cada una de las siguientes funciones y escribir un programa que permi
# ta verificar su funcionamiento, imprimiendo la matriz luego de invocar a cada fun
# ción:
#  g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú
# mero se recibe como parámetro.
#  h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
#  i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
#  j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
#   una lista con los números de las mismas.
#  NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera 
# sea el valor ingresado
import sys
sys.path.append(r'c:\Users\Lucas\Desktop\UADE\Programacion I')
from Utils.terminalHelper import pedir_numero

#  a. Cargar números enteros en una matriz de N x N, ingresando los datos desde teclado. 

filas_input = pedir_numero("Ingrese el numero de filas de la  matriz: ")
columnas_input = pedir_numero("Ingrese el numero de columnas de la  matriz: ")

def crear_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(pedir_numero("Ingrese un número: "))
    return matriz

matriz = crear_matriz()
#  b. Ordenar en forma ascendente cada una de las filas de la matriz.
def ordenar_numeros_de_fila(matriz):
    for f in range(len(matriz)):
        matriz[f].sort()
    
#  c. Intercambiar dos filas, cuyos números se reciben como parámetro.
def swap_fila(matriz, posicion_fila_inicio, posicion_fila_destino):
    fila_buffer = matriz[posicion_fila_destino]
    matriz[posicion_fila_destino] = matriz[posicion_fila_inicio]
    matriz[posicion_fila_inicio] = fila_buffer

# swap_fila(matriz, 1, 0)

#  d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
def swap_columna(matriz, posicion_columna_inicio, posicion_columna_destino):
    columna_buffer = []
    for f in range(len(matriz)):
        columna_buffer.append(matriz[f][posicion_columna_destino])
        
    for f in range(len(matriz)):
        matriz[f][posicion_columna_destino] = matriz[f][posicion_columna_inicio]
        matriz[f][posicion_columna_inicio] = columna_buffer[f]

# swap_columna(matriz, 1, 0)

#  e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
def trasponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_traspuesta = [[0] * filas for c in range(columnas)] #init
    for f in range(filas):
        for c in range(columnas):
            matriz_traspuesta[c][f] = matriz[f][c]
    return matriz_traspuesta

matriz_traspuesta = trasponer_matriz(matriz)    
# print(matriz_traspuesta)


#  f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
#   parámetro.
def calcular_promedio(lista_de_numeros):
    cantidad_de_numeros = len(lista_de_numeros)
    total = 0
    for n in lista_de_numeros:
        total = total + n
        
    return total / cantidad_de_numeros

for f in range(len(matriz)):
    print(f'El promedio de la fila {f + 1} es {calcular_promedio(matriz[f])}')

print(matriz)