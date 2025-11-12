#                           LISTAS 📚

# Una lista es una colección de elementos en un orden determinado.
# Se definen con corchetes [].
libros = ["mateo", "marcos", "lucas", "juan"]
print(libros)

# Podemos acceder a un elemento de la lista por su índice.
print(libros[0])  # ➡️ primer elemento
print(libros[1])  # ➡️ segundo elemento, luego sigue 2, 3...
print(libros[-1])  # ➡️ último elemento

# Podemos combinar texto con elementos de la lista.
print(f"El primer libro del Nuevo Testamento es {libros[0].title()} 📖")

#              MODIFICAR, AGREGAR Y ELIMINAR ELEMENTOS DE UNA LISTA ✏️

# Las listas son dinámicas: podemos agregar, quitar o modificar elementos.

newjeans_songs = ["Hype Boy", "Super Shy", "ETA", "Cool With You"]

newjeans_songs[0] = "Attention"  # ✏️ modificamos el primer elemento
newjeans_songs.append("Ditto")  # ➕ agregamos un elemento al final de la lista

# A menudo creamos listas vacías y luego agregamos elementos.
nueva_lista = []
nueva_lista.append("Hola")  # ➕ agregamos un elemento

newjeans_songs.insert(0, "OMG")  # ➕ agregamos un elemento en la posición 0

# Para eliminar un elemento usamos `del`.
del newjeans_songs[2]  # 🗑️ eliminamos el tercer elemento "ETA"

# Existe el método `pop()` que elimina el último elemento y lo devuelve.
listen_songs = newjeans_songs.pop()  # 🎵 eliminamos el último elemento y lo guardamos
print(f"La última canción escuchada es {listen_songs}")

# Si solo conocemos el valor del elemento, usamos `remove()`.
love_songs = "ETA"
newjeans_songs.remove(love_songs)  # 🗑️ eliminamos "ETA" de la lista

# También podemos usar `.clear()` para eliminar todos los elementos de la lista.
# newjeans_songs.clear()  # 🧹 ¡lista vacía!

#                       ORDENAR UNA LISTA 🔠

# Podemos ordenar una lista de forma permanente o temporal.

# TEMPORAL
Lol_caracters = ["Shaco", "Ivern", "Akali", "Caitlyn"]
print(f"Lista original: {Lol_caracters}")
print(f"Lista ordenada temporalmente: {sorted(Lol_caracters)}")  # 🔄 orden temporal
print(f"Lista ordenada al revés temporalmente: {sorted(Lol_caracters, reverse=True)}")  # 🔄 reverso

print(f"Lista original después de sorted(): {Lol_caracters}")  # ✅ la original no cambia

# PERMANENTE
Lol_caracters.sort()  # 🔁 ordenamos permanentemente
print(f"Lista ordenada permanentemente: {Lol_caracters}")

Lol_caracters.sort(reverse=True)  # 🔁 orden reverso permanente
print(f"Lista ordenada al revés permanentemente: {Lol_caracters}")

# Para ver la longitud de una lista usamos `len()`.
print(f"La lista tiene {len(Lol_caracters)} personajes 📊")

# EXTRA: Iterar sobre una lista
print("Personajes de LoL:")
for personaje in Lol_caracters:
    print(f"- {personaje}")

# EXTRA: Crear una lista de números con range()
numeros = list(range(1, 6))
print(f"Lista de números: {numeros}")

# EXTRA: Obtener el índice y valor con enumerate()
for indice, personaje in enumerate(Lol_caracters):
    print(f"Índice {indice}: {personaje}")

# EXTRA: Comprensión de listas (list comprehension)
cuadrados = [x**2 for x in range(1, 6)]
print(f"Cuadrados: {cuadrados}")

# EXTRA: Copiar una lista (evitar modificar la original)
copia_lista = Lol_caracters.copy()
# o también: copia_lista = Lol_caracters[:]