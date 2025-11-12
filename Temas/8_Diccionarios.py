#                           DICCIONARIOS
# Los Diccionarios permiten conectar informaciones relacionadas
# y almacenar listas, duplas, incluso otros diccionarios, ejm:

alien_0 = {"color": "green", "points": 5} #es una colección de pares clave-valor (color-green)
#donde "color" es la clave y "green" es el valor
print(alien_0["color"]) # Usamos la clave para acceder el valor 
print(alien_0["points"])

# AÑADIR nuevos pares clave-valor
# primero definimos el diccionario donde trabajaremos (alien:0)
# luego añadimos un nuevo par clave-valor: "x_position" como clave y "0" como valor
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)
# A veces suele ser conveniente empezar con uno VACIO

# MODIFICAR valores
#primero definimos el diccionario y el valor asocioado que queremos cambiar
alien_0["color"] = "yellow"
print(f"The alien is now {alien_0['color']}.")

# para acerlo interesante podemos jugar con la velocidad y posicion del alien
alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"} # empezamos definiendo su posicion y velocidad
print(f"Original position: {alien_0['x_position']}") #imprimimos su posicion 

# Mueve el alien a la derecha
# Determina cuanto se muevele el alien segun su velocidad
if alien_0["speed"] == "slow":
    x_increment = 1 #si es "lenta" aumenta en 1
elif alien_0["speed"] == "medium":
    x_increment = 2 #si es "media" aumenta en 2
else: # si es rapida aumenta en 3
    x_increment = 3
# El resultado se guarda en la siguiente variable
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(f"New position: {alien_0['x_position']}")

#ELIMINAR valores
del alien_0["color"]
print(alien_0)
# "del" le indica que borre la clave 'points' del diccionario y elimine también el valor asociado a esa

# MANEJANDO los diccionarios
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
# esta es una buena forma de oraganizar los elementos dentro del diccionario
language = favorite_languages["sarah"].title()
#lo guardamos en una variable para hacerlo mas limpio
print(f"Sarah's favorite language is {language}.")

# "get()" lo usamos en caso de que no exista la variable
# o en caso de que el diccionario sea grange y tenamos que buscar una 
carlos_languaje = favorite_languages.get("carlos", "carlos don't have a favorite language")
print(carlos_languaje)

#BUCLE FOR en diccionarios
user_0 = {
    "username": "efermi",
    "first": "enrico",
    "last": "fermi",
}
# para usar un bucle "for" en un diccionario
for key, value in user_0.items(): # "items()" para seleccionar los valores
    print(f"\nKey: {key}") # pasa por todas las claves
    print(f"Value: {value}") #imprime los valores

#es perfecto para pasar por todos los valores de un diccionario
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite languajes is {language.title()}.")
# esto es perfecto si tenemos miles o millones de datos 

# el metodo KEYS() es perfecto cuando no hace falta trabajar con todos los valores del diccionario
favorite_languages = {
    "jen": "python",
    "sarah": "c",
    "edward": "ruby",
    "phil": "python",
}
# pedimos que saque todas las claves del diccionario
for name in favorite_languages.keys():
    print(name.title())

#tambien podemos jugar con el IF
friends = ["phil", "sarah"]
#amigos especiales
for name in favorite_languages.keys():
    print(f"Hi {name.title()}")
    #si el nombre esta en amigos especiales
    if name in friends:
        language = favorite_languages[name].title()
        #se guarda el valor en la variable "language"
        print(f"\t{name.title()}, I see you love {language}!")

#si queremos ORDENAR las claves usamos "SORTED()"
for name in sorted(favorite_languages.keys()):
    # sorted  le dice que ordene en una lista antes de ser iniciar el bucle
    print(f"{name.title()}, thank you for taking the poll.")

#Ahora si queremos usar los valores usamos VALUES()
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    
#puede que se haga infinita y repetitiva, en es caso usamos "SET()"
for language in set(favorite_languages.values()):
    #set identifica los elementos UNICOS y crea un conjunto de ellos
    print(language.title())
