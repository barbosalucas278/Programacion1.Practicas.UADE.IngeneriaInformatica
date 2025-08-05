#  Desarrollar una función que reciba tres números enteros positivos correspondientes 
# al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
# tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
# Devolver True o False según la fecha sea correcta o no. Realizar también un 
# programa para verificar el comportamiento de la función.
import sys
sys.path.append(r'c:\Users\Lucas\Desktop\UADE\Programacion I')
from Libs.terminalHelper import pedir_numero

def main():
    es_fecha_valida = True
    dia = pedir_numero("Ingrese el día:")
    mes = pedir_numero("Ingrese el mes:")
    anio = pedir_numero("Ingrese el año:")
    es_fecha_valida = validar_fecha(dia, mes, anio)
    if es_fecha_valida:
        print(f'La fecha {dia}/{mes}/{anio} es válida.')
    else:
        print(f'La fecha {dia}/{mes}/{anio} no es válida.')

def validar_fecha(dia, mes, anio):
    es_fecha_valida = True
    if anio < 1:
        es_fecha_valida = False
    if mes < 1 or mes > 12:
        es_fecha_valida = False
    if dia < 1 or dia > 31:
        es_fecha_valida = False
    if mes in [4, 6, 9, 11] and dia > 30:
        es_fecha_valida = False
    if es_bisiesto(anio):
        if mes == 2 and dia > 29:
            es_fecha_valida = False
    else:
        if mes == 2 and dia > 28:
            es_fecha_valida = False
    return es_fecha_valida
        
def es_bisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            return True
        else:
            return False
    return False        
# def validar_dia(dia):
    
# def validar_mes(mes):
    
# def validar_anio(anio):
    








main()