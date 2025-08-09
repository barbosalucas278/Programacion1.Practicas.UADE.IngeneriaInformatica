# Una persona desea llevar el control de los gastos realizados al viajar en el subte
# rráneo dentro de un mes. Sabiendo que dicho medio de transporte utiliza un es
# quema de tarifas decrecientes (detalladas en la tabla de abajo) se solicita desarro
# llar una función que reciba como parámetro la cantidad de viajes realizados en un 
# determinado mes y devuelva el total gastado en viajes. Realizar también un pro
# grama para verificar el comportamiento de la función.
import sys
sys.path.append(r'c:\Users\Lucas\Desktop\UADE\Programacion I')

from Libs.numberOperationsHelper import disminuir_porcentaje
from Libs.terminalHelper import pedir_numero

TARIFA_MAXIMA = 1000
PRIMERA_FRANJA = 0.2
SEGUNDA_FRANJA = 0.3
TERCERA_FRANJA = 0.4

cantidad_de_viajes = pedir_numero("Ingrese la cantidad de viajes realizados: ")
def calcular_costo_de_viaje(cantidad_de_viajes):
    match cantidad_de_viajes:
        case cantidad_de_viajes if cantidad_de_viajes >= 1 and cantidad_de_viajes <= 20:
            return "Averiguar en Internet el valor actualizado"
        case cantidad_de_viajes if cantidad_de_viajes > 20 and cantidad_de_viajes <= 30:
            return disminuir_porcentaje(TARIFA_MAXIMA,PRIMERA_FRANJA)
        case cantidad_de_viajes if cantidad_de_viajes > 30 and cantidad_de_viajes <= 40:
            return disminuir_porcentaje(TARIFA_MAXIMA,SEGUNDA_FRANJA)
        case cantidad_de_viajes if cantidad_de_viajes > 40:
            return disminuir_porcentaje(TARIFA_MAXIMA,TERCERA_FRANJA)
        
costo = calcular_costo_de_viaje(cantidad_de_viajes)
print(f'Costo: {costo}')