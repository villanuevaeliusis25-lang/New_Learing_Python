#                               BUCLES 🔁
# Estructuras de control que permiten repetir un bloque de código varias veces

newjeans = ["minji", "haerin", "hanni", "danielle", "hyein"]  # 🎤 miembros de NewJeans

# "for" toma cada elemento de la lista y lo asigna a una variable temporal "newjean"
for newjean in newjeans:
    # Los ":" le indican a Python que la siguiente línea indentada es parte del bucle
    print(f"{newjean.title()} te extrañamos mucho <3 💖")
# Se repite el bloque de código para cada elemento de la lista
# Es recomendable usar nombres diferentes para la variable temporal y la lista

# Podemos crear espacios entre ciclos con "\n"
print("\n" + "="*50)  # Línea separadora
print("Gracias por todo lo que hacen por nosotros <3 🫶")
print("="*50)

for newjean in newjeans:
    print(f"\n{newjean.title()} te extrañamos mucho <3 💕")
    print(f"¡Sé fuerte {newjean.title()}! 💪")

print("\n" + "✨" * 20)
print("NewJeans never die <3 🌟")
print("✨" * 20)

# ⚠️ IMPORTANTE: Las sangrías (indentación) son cruciales en Python
# El bloque de código dentro del bucle for debe estar indentado
# El bloque de código fuera del bucle for NO debe estar indentado

#                       RANGE() 🔢
print("\n" + "="*30)
print("USANDO RANGE()")
print("="*30)

for value in range(1, 6):  # El segundo valor es exclusivo (no se incluye)
    print(f"Número: {value}")

# Aunque range(1,6) va del 1 al 5, nunca incluye el valor final

# Si queremos guardar los números en una lista usamos list()
numbers = list(range(1, 6))
print(f"\nLista creada con range(): {numbers} 📋")

# También podemos especificar un incremento (step)
even_numbers = list(range(2, 11, 2))  # Empieza en 2, termina en 10, incrementa de 2 en 2
print(f"Números pares del 2 al 10: {even_numbers} 🔢")

# Podemos elevar estos números al cuadrado
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)  # append() agrega un elemento al final de la lista
    print(f"{value}² = {square}")

print(f"\nLista de cuadrados: {squares} 🧮")

# Podemos usar min(), max() y sum() con listas de números
print(f"\n--- Estadísticas de la lista de cuadrados ---")
print(f"Valor mínimo: {min(squares)} 📉")
print(f"Valor máximo: {max(squares)} 📈")
print(f"Suma total: {sum(squares)} ➕")

#                       PARTIR LISTAS O SLICES 🍰
print("\n" + "="*30)
print("SLICES (REBANADAS DE LISTA)")
print("="*30)

blackpink = ["jennie", "jisoo", "rose", "lisa"]
print(f"Miembros de BLACKPINK: {blackpink} 🖤💖")

print(f"Miembros coreanas: {blackpink[0:2]}")  # Índice 0 hasta 2 (exclusivo)
print(f"Miembros extranjeras: {blackpink[2:]}")  # Desde índice 2 hasta el final
print(f"Mi bias: {blackpink[-1:]}")  # Último elemento de la lista

# Slice con pasos (step)
print(f"Cada segundo miembro: {blackpink[::2]}")  # Cada 2 elementos
print(f"Lista al revés: {blackpink[::-1]}")  # Lista invertida

#                           COPIAR LISTAS 📋
print("\n" + "="*30)
print("COPIANDO LISTAS")
print("="*30)

# Para copiar una lista correctamente usamos el slice completo [:]
bias_groups = blackpink[:]  # ✅ Crear una copia independiente
# bias_groups = blackpink  # ❌ ESTO NO COPIA, crea una referencia

# Para añadir elementos a la nueva lista usamos append()
bias_groups.append("danielle")  # 🎤 de NewJeans
bias_groups.append("haerin")    # 🎤 de NewJeans

print(f"BLACKPINK original: {blackpink} 🖤💖")
print(f"Mis bias: {bias_groups} 💕")

#                                TUPLAS 📦
print("\n" + "="*30)
print("TUPLAS (INMUTABLES)")
print("="*30)

# Son inmutables - *no se pueden modificar* una vez creadas
# Se definen con paréntesis () y los elementos se separan por comas
tupla_original = (1, 2, 3, 4, 5)
print(f"Tupla original: {tupla_original}")

# También podemos usar bucle "for" para recorrer los elementos de una tupla
print("Recorriendo la tupla:")
for elemento in tupla_original:
    print(f"Elemento: {elemento}")

# Aunque no podamos modificar una tupla, sí podemos reasignar una nueva tupla
print(f"\nTupla original: {tupla_original}")
tupla_original = (6, 7, 8, 9, 10)  # Reasignación
print(f"Nueva tupla: {tupla_original} 🔄")

# EXTRA: Desempaquetado de tuplas
coordenadas = (4, 5)
x, y = coordenadas
print(f"\nCoordenadas: {coordenadas}")
print(f"X = {x}, Y = {y} 📍")

# EXTRA: Tuplas con un solo elemento necesitan coma
tupla_un_elemento = (1,)  # ✅ Correcto
# tupla_un_elemento = (1)  # ❌ Incorrecto (sería un entero)
print(f"Tupla con un elemento: {tupla_un_elemento}")

# EXTRA: Convertir entre lista y tupla
lista_a_tupla = tuple([1, 2, 3])
tupla_a_lista = list((1, 2, 3))
print(f"Lista a tupla: {lista_a_tupla}")
print(f"Tupla a lista: {tupla_a_lista} 🔄")

print("\n" + "🎉" * 20)
print("¡Dominaste los bucles for! 🚀")
print("🎉" * 20)