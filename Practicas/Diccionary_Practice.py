#           DICCIONARIO
persona = {
    "nombre" : "Danielle",
    "apellido" : "Marsh",
    "edad" : 20,
    "ciudad" : "Newcastle"
}
numeros = {
    "hanni": 21,
    "haerin" : 19,
    "danielle" : 20,
    "minji" : 22,
    "hyein" : 17
}
for person in persona:
    print(f"{person.title()}: {persona[person]}")

canciones ={
    "newjeanz": "cool with you",
    "blackpink": "pinkvenom",
    "aespa": "armagedom",
}
for grupo, cancion in canciones.items():
    if cancion == "Cool with you":
        print(f"{cancion.title} es mi cancion favorita de {grupo.title}")
    elif cancion == "pinkvenom":
        print(f"{cancion.title} es mi cancion favorita de {grupo.title}")
    else:
        print(f"{cancion.title} es mi cancion favorita de {grupo.title}")

for grupo in canciones.keys():
    print(grupo.title())
for cancion in canciones.values():
    print(cancion.title())
