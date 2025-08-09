#  Desarrollar una función que reciba tres números enteros positivos correspondientes 
# al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe 
# tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos. 
# Devolver True o False según la fecha sea correcta o no. Realizar también un 
# programa para verificar el comportamiento de la función.
import sys
sys.path.append(r'c:\Users\Lucas\Desktop\UADE\Programacion I')
from Libs.dateHelper import validar_fecha
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
      
main()