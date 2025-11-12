#                   NUMERO PAR O IMPAR
# Escribe una función que determine si un número es par
# Devuelve True si es par, False si es impar
def es_par(numero):
    return numero % 2 == 0

# Pruebas:
print(es_par(4))   # Debería devolver True
print(es_par(7))   # Debería devolver False
print(es_par(0))   # Debería devolver True

#               CLASIFICAR NUMEROS
# Escribe una función que:
    # - Devuelva "positivo par" si el número es positivo y par
    # - Devuelva "positivo impar" si es positivo e impar
    # - Devuelva "negativo par" si es negativo y par
    # - Devuelva "negativo impar" si es negativo e impar
    # - Devuelva "cero" si es 0
def clasificar_numero(numero):
    if numero > 0 and numero % 2 == 0 and numero != 0:
        print("Es positivo y par")
    elif numero > 0 and numero != 0:
        print("Es positivo e impar")
    elif numero % 2 == 0 and numero != 0:
        print("Es negativo y par")
    elif numero != 0: 
        print("Es negativo e impar")
    else:
        print("Cero")
    pass

# Pruebas:
clasificar_numero(5)    # "positivo impar"
clasificar_numero(-4)   # "negativo par"
clasificar_numero(0)   # "cero"

#                   CONTAR PARES E IMPARES
# Cuenta cuántos números pares e impares hay en un rango
# Ejemplo: del 1 al 5 → pares: 2, impares: 3
# Devuelve un diccionario: {'pares': X, 'impares': Y}

def contar_pares_impares(inicio, fin):
    contador_de_pares = 0
    contador_de_impares = 0
    
    for contar in range(inicio, fin + 1):
        if contar % 2 == 0:
            contador_de_pares = contador_de_pares + 1
        else:
            contador_de_impares = contador_de_impares + 1
    
    return {"pares": contador_de_pares, "impares": contador_de_impares}

# Pruebas:
print(contar_pares_impares(1, 10))
print(contar_pares_impares(5, 15))