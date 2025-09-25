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
    
    pass

# Pruebas:
print(clasificar_numero(5))    # "positivo impar"
print(clasificar_numero(-4))   # "negativo par"
print(clasificar_numero(0))    # "cero"