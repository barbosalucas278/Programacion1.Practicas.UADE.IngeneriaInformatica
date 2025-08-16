from Utils.terminalHelper import pedir_numero


def crear_matriz(filas, columnas):
    matriz = []
    for f in range(filas):
        matriz.append([])
        for c in range(columnas):
            matriz[f].append(pedir_numero("Ingrese un número: "))
    return matriz

#  b. Ordenar en forma ascendente cada una de las filas de la matriz.
def ordenar_numeros_de_fila(matriz):
    for f in range(len(matriz)):
        matriz[f].sort()
        
#  c. Intercambiar dos filas, cuyos números se reciben como parámetro.
def swap_fila(matriz, posicion_fila_inicio, posicion_fila_destino):
    fila_buffer = matriz[posicion_fila_destino]
    matriz[posicion_fila_destino] = matriz[posicion_fila_inicio]
    matriz[posicion_fila_inicio] = fila_buffer

#  d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
def swap_columna(matriz, posicion_columna_inicio, posicion_columna_destino):
    columna_buffer = []
    for f in range(len(matriz)):
        columna_buffer.append(matriz[f][posicion_columna_destino])
        
    for f in range(len(matriz)):
        matriz[f][posicion_columna_destino] = matriz[f][posicion_columna_inicio]
        matriz[f][posicion_columna_inicio] = columna_buffer[f]

#  e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
def trasponer_matriz(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_traspuesta = [[0] * filas for c in range(columnas)] #init
    for f in range(filas):
        for c in range(columnas):
            matriz_traspuesta[c][f] = matriz[f][c]
    return matriz_traspuesta

#  f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como 
#   parámetro.
def calcular_promedio(lista_de_numeros):
    cantidad_de_numeros = len(lista_de_numeros)
    total = 0
    for n in lista_de_numeros:
        total = total + n
        
    return total / cantidad_de_numeros

#  g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo nú
# mero se recibe como parámetro.
def calcular_porcentaje_impar_por_columna(matriz, indice_columna):
    columna_buffer = []
    for f in range(len(matriz)):
        columna_buffer.append(matriz[f][indice_columna])
    numeros_impares = 0;    
    cantidad_de_numeros_por_columna = len(columna_buffer);    
    for n in columna_buffer:
        if n % 2 != 0:
            numeros_impares = numeros_impares + 1
    return (numeros_impares * 100) / cantidad_de_numeros_por_columna

#  h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
def es_matriz_simetrica(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    es_simetria = True
    for f in range(filas): #1
        if(f != 0):
            for c in range(columnas):
                if matriz[f][c] != matriz[c][f]:
                    es_simetria = False
            
    return es_simetria

#  i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
def es_matriz_simetrica_secundaria(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    es_simetria = True
    for c in range(columnas): #1
        if(c != columnas - 1):
            for f in range(filas):
                if matriz[f][(columnas-1) - c] != matriz[c][(columnas-1) - f]:
                    es_simetria = False
            
    return es_simetria

#  j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo 
#   una lista con los números de las mismas.
def get_columna_palindromo(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    palindromo = []
    for c in range(columnas): #1
        current_col = []
        for f in range(filas):
            current_col.append(matriz[f][c])
        if calcular_palindromo(current_col):
            palindromo.append(current_col)
            
    return palindromo

def calcular_palindromo(numeros):
    for n in range(len(numeros)):
        if numeros[n] == numeros[(len(numeros) -1) - n]:
            return numeros
        else:
            return False