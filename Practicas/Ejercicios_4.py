#                   GENERADOR DE SECUENCIAS
def generar_secuencia(inicio, fin, paso=1):
    """Genera una lista de números desde inicio hasta fin
    Paso controla de cuánto en cuánto va """
    secuencia = []
    if paso > 0:
        while inicio <= fin:
            secuencia.append(inicio)
            inicio = inicio + paso
    elif paso < 0:
        while inicio >= fin:
            secuencia.append(inicio)
            inicio = inicio + paso
    else:
        return "Error, no se puede poner 0"
        
    return secuencia

# Pruebas:
print(generar_secuencia(1, 5))      # [1, 2, 3, 4, 5]
print(generar_secuencia(0, 10, 2))  # [0, 2, 4, 6, 8, 10]
print(generar_secuencia(5, 1, -1))  # [5, 4, 3, 2, 1]


#                   BUSCADOR EN LISTA
def buscar_elemento(lista, elemento):
    for indice in range(len(lista)):
        if lista[indice] == elemento:
            return True, indice
    return False, -1

# Pruebas:
print(buscar_elemento(["manzana", "banana", "naranja"], "banana"))  # (True, 1)
print(buscar_elemento([1, 2, 3, 4], 5))  # (False, -1)
print(buscar_elemento([10, 20, 30, 20, 40], 20))  # (True, 1) - primera aparición


#               CONVERTIDOR DE UNIDADES SIMPLES
#Conversiones básicas:
#    - metros a centímetros y viceversa (1m = 100cm)
#    - horas a minutos y viceversa (1h = 60min)
#    - kilogramos a gramos y viceversa (1kg = 1000g)
def convertir_unidades(valor, unidad_origen,unidad_final):
    valor = float(valor)
    unidad_origen = str(unidad_origen)
    unidad_final = str(unidad_final)
    if unidad_origen == "centímetros" and unidad_final == "metros":
        valor = valor / 100
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "metros" and  unidad_final == "centimetros":
        valor = valor * 100
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "minutos" and  unidad_final == "horas":
        valor = valor / 60
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "horas" and  unidad_final == "minutos":
        valor = valor * 60
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "kilogramos" and  unidad_final == "gramos":
        valor = valor * 1000
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "gramos" and  unidad_final == "kilogramos":
        valor = valor / 1000
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "celsius" and  unidad_final == "Fahrenheit":
        valor = (valor * 9/5) + 32
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "Fahrenheit" and  unidad_final == "celsius":
        valor = (valor - 32) * 5/9
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "litros" and  unidad_final == "mililitros":
        valor = valor * 1000
        return f"Son: {valor} {unidad_final}"
    elif unidad_origen == "mililitros" and  unidad_final == "litros":
        valor = valor / 1000
        return f"Son: {valor} {unidad_final}"
    else:
        return "Pon un valor que sea compatible"


# Pruebas:
print(convertir_unidades(2, "metros", "centimetros"))  # 200
print(convertir_unidades(90, "minutos", "horas"))      # 1.5
print(convertir_unidades(1.5, "kilogramos", "gramos")) # 1500
print(convertir_unidades(5, "metros", "horas"))        # "Error: Conversión no soportada"


#           VERSION MAS AVANZADA Y OPTIMIZADA
def convertir_unidades_avanzada(valor, unidad_origen, unidad_destino):
    conversiones = {
        "longitud": {"metros": 1, "centimetros": 100},
        "tiempo": {"horas": 1, "minutos": 60},
        "peso": {"kilogramos": 1, "gramos": 1000},
        "volumen": {"litros": 1, "mililitros": 1000}
    }
    
    # Buscar en qué categoría están las unidades
    for categoria, unidades in conversiones.items():
        if unidad_origen in unidades and unidad_destino in unidades:
            factor = unidades[unidad_destino] / unidades[unidad_origen]
            return valor * factor
    
    return "Error: Conversión no soportada"


# Pruebas:
print(convertir_unidades_avanzada(2, "metros", "centimetros"))  # 200
print(convertir_unidades_avanzada(90, "minutos", "horas"))      # 1.5
print(convertir_unidades_avanzada(1.5, "kilogramos", "gramos")) # 1500
print(convertir_unidades_avanzada(5, "metros", "horas"))        # "Error: Conversión no soportada"
