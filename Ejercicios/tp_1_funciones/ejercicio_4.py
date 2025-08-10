# Un comercio de electrodomésticos necesita para su línea de cajas un programa que 
# le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan 
# dos números enteros, correspondientes al total de la compra y al dinero recibido. 
# Informar cuántos billetes de cada denominación deben ser entregados como vuelto, 
# de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes 
# de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el 
# dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta 
# de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se 
# abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1 
# billete de $200, 1 billete de $100 y 3 billetes de $10.

import sys
sys.path.append(r'c:\Users\Lucas\Desktop\UADE\Programacion I')
from Utils.terminalHelper import pedir_numero

BILLETES_EXISTENTES = [5000,1000,500,200,100,50,10]
total_compra = pedir_numero("Ingrese el total de la compra: ")
dinero_recibido = pedir_numero("Ingrese el dinero recibido: ")

def calcular_vuelto(total, recibido):
    vuelto = recibido - total
    vuelto_detallado = []
    for i in range(len(BILLETES_EXISTENTES)):
        while vuelto >= BILLETES_EXISTENTES[i]:
            vuelto = vuelto - BILLETES_EXISTENTES[i]
            vuelto_detallado.append(BILLETES_EXISTENTES[i]) 
    return vuelto_detallado

def contar_billetes(billetes):
    totalidad_de_billetes = []
    billetes_unicos = list(set(billetes))
    for i in range(len(BILLETES_EXISTENTES)):
        if billetes_unicos.count(BILLETES_EXISTENTES[i]):
            cantidad_de_billetes = billetes.count(BILLETES_EXISTENTES[i])
            totalidad_de_billetes.append(f'{cantidad_de_billetes} {f'billetes' if cantidad_de_billetes > 1 else f'billete'} de {BILLETES_EXISTENTES[i]} pesos')
    return totalidad_de_billetes

vuelto_resultado = calcular_vuelto(total_compra,dinero_recibido)

print(contar_billetes(vuelto_resultado))