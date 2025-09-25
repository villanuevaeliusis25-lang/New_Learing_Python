                        #        LISTAS 

#una lista es una coleccion de elementos en un orden determinado
#se definen con corchetes []
libros = ["mateo", "marcos", "lucas", "juan"]
print(libros)

#podemos acceder a un elemento de la lista por su indice
print(libros[0]) #primer elemento
print(libros[1]) #segundo elemento, luego sigue 2,3...
print(libros[-1]) #ultimo elemento
#podemos combinar texto con elementos de la lista
print(f"El primer libro del nuevo testamento es {libros[0].title()}")


#              MODIFICAR, AGREGAR Y ELIMINAR ELEMENTOS DE UNA LISTA
#las listas son dinamicas, podemos agregar elementos, quitarlos o modificarlos

newjeans_songs = ["Hype", "Super Shy", "ETA", "Cool With You"]

newjeans_songs[0] = "Attention" #modificamos el primer elemento
newjeans_songs.append("Ditto") #agregamos un elemento al final de la lista
#a menudo creamos listas vacias y luego agregamos elementos
newjeans_songs.insert(0, "OMG") #agregamos un elemento en la posicion 0
#para eliminar un elemento usamos *del*
del newjeans_songs[2] #eliminamos el tercer elemento "ETA"
#existe el metodo "pop()" que elimina el ultimo elemento y lo devuelve a una variable
listen_songs = newjeans_songs.pop() #eliminamos el ultimo elemento y lo guardamos en 
print(f"la ultima cancion escuchada es {listen_songs}")
#si solo conocemos el valor del elemento, usamos remove()
love_songs = "ETA"
newjeans_songs.remove(love_songs) #eliminamos "Hybe" de la lista
#pero sigue tenemos a "hybe" en la variable love_songs
#tambien podemos usar ".clear()" para eliminar todos los elementos de la lista

#                       ORDENAR UNA LISTA
#Podemos ordenar una lista de forma permanente o temporal

#TEMPORAL
Lol_caracters = ["Shaco", "Ivern", "Akaly", "Catlyn"]
print(f"Lista original: {Lol_caracters}")
print(f"Lista ordenada temporalmente: {sorted(Lol_caracters)}") #ordenamos temporalmente
#tambien acepta ".reverse()" para un orden reverso

print(f"Lista original: {Lol_caracters}")

#PERMANENTE
Lol_caracters.sort() #ordenamos permanentemente
print(f"Lista ordenada permanentemente: {Lol_caracters}")

#Para ver la longitud de una lista usamos "len()" 
len(Lol_caracters)
print(f"la lista tiene {len(Lol_caracters)} personajes")