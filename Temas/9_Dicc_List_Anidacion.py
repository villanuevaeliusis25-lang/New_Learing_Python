#                   DICCIONARIOS Y ANIDACION 
# Que hacemos con mucha informacion? pues facil, anidamos
# Aqui añadimos diccionarios a listas
alien_0 = {"color": "green", "points": 5}
alien_1 = {"color": "yellow", "points": 10}
alien_2 = {"color": "red", "points": 15}
#creamos 3 aliens diferentes
aliens = [alien_0, alien_1, alien_2]
#y todos ellos los almacenamos en una lista
for alien in aliens:
    print(alien)

# En un ejemplo mas realista, necesitamos generar nuevos aliens
# usamos "range()" para crear una flota de aliens
aliens =[]

for alien_number in range(30):
#indica cuantos aliens queremos que genere
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    aliens.append(new_alien)
#muestra los 5 primeros aliens 
for alien in aliens[:5]:
    print(alien)
print("...")

#Muestra cuantos aliens hemos creado
print(f"Total number of aliens: {len(aliens)}")

#todos estos alienigenas tienen los mismon datos pero se los considera un elemento separado
#asi que podemos MODIFICARLOS con el bucle "for" y "if"

for alien in aliens[:3]:# seleccionamos los 3 primeros aliens
    if alien["color"] == "green": #si el alien es verde
        alien["color"] = "yellow" #cambia a amarillo
        alien["speed"] = "medium" #su velocidad es media
        alien["points"] = 10 #y tiene 10 puntos
for alien in aliens[:5]:
    print(alien)
print("...")

# a veeces resultas mas conveniente anidar las LISTAS A DICCIONARIOS
pizza = {
    "crust" : "thick", #crust = clave, thick = valor
    "toppings" : ["mushrooms", "extra cheese"], #topping = clave, mushrooms y extra cheese como valor
    }
#pedido
print(f"You ordered a {pizza['crust']}-crust pizza"
    "with the following toppings:")
#usamos el bucle for para acceder a la lista de ingredientes
for topping in pizza["toppings"]:
    print(f"\t" + topping)

# al pasar un bucle por el diccionario, el valor asociado seria una lista en ves de uno solo
favorite_languages = {
    "jen": ["python", "rust"],
    "sarah" : "c",
} #el valor awsociado a lops nombre es ahora una lista
for name, languages in favorite_languages.items():
    #al pasar el bucle, usamos "languages" para alojar cada valor porque sabemos que sera una lista
    print(f"\n{name.title()}s favorite languages are:")
    for language in languages:
        #usamos este bucle para pasar lista los leng.fav. de cada persona
        print(f"\t{language.title()}")

#podemos anidar un diccionario dentro de otro diccionario, aunque no es recomendable
user = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",},
    "mcurie" :{
        "first": "marie",
        "last": "curie",
        "location": "paris",}
    }
for username, user_info in user.items():
    #pasamos el bucle por "user"
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    #guardamos los nombres en full name
    location = user_info["location"]
    #y guardamos su locacion 
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")