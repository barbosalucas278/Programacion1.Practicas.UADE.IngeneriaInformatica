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
    return False  