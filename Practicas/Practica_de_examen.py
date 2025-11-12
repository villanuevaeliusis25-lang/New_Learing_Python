#   EJERCICIO 1: CONTADOR CON WHILE
def contador_while(limite):
    i = 1
    contador = []
    suma = 0
    while i <= limite:
        contador.append(i)
        i = i + 1
    for dato in contador:
        suma = suma + dato
    resultado = '+'.join(map(str, contador))
    return f"({resultado}) \nLa suma total es: {suma}"

# Pruebas:
print(contador_while(5))   # 15 (1+2+3+4+5)
print(contador_while(10))  # 55

#   EJERCICIO 2: ADIVINA EL NUMERO
import random

def adivina_numero():
    numero_secreto = random.randint(1, 10)  # Más simple que usar lista
    contador = 0
    adivinado = False
    
    print("¡Adivina el número entre 1 y 10!")
    
    while not adivinado:  # Mientras NO se haya adivinado
        adivinanza = int(input("Tu intento: "))
        contador += 1  # Contamos CADA intento
        
        if adivinanza == numero_secreto:
            adivinado = True  # Cambiamos la condición para salir del bucle
            return f"¡Felicidades! Lo lograste en {contador} intentos"
        else:
            if adivinanza < numero_secreto:
                print("El número es MAYOR")
            else:
                print("El número es MENOR")
    
    # Esta línea no se ejecutará por el return, pero es buena práctica
    return f"¡Felicidades! Lo lograste en {contador} intentos"

# Prueba
print(adivina_numero())
# Prueba:
# adivina_numero()  # Juega hasta adivinar