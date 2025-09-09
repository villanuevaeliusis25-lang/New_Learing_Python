persona = {
    "nombre" : "Danielle",
    "apellido" : "Marsh",
    "edad" : 20,
    "ciudad" : "Newcastle",
}
persona_2 = {
    "nombre" : "Haerin",
    "apellido" : "kang",
    "edad" : 19,
    "ciudad" : "seul",
}
persona_3 ={
    "nombre" : "hanni",
    "apellido" : "pham",
    "edad" : 20,
    "ciudad" : "melbourne",
}
personas = [persona, persona_2, persona_3]

for p in personas:
    print(f"{p['nombre'].title()} {p['apellido'].title()} tiene {p['edad']} años y nacio en {p['ciudad'].title()}")

canciones_a_anadir = ["cool with you", "newjeanz", "OMG"]

for i, p in enumerate(personas):
    p["cancion"] = canciones_a_anadir[i]
