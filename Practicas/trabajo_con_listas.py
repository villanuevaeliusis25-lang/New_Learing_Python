                          #TRABAJO CON LISTAS

nombres = ["Ana", "Luis", "Carlos", "Marta"]
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[-1])

print(f"Hola {nombres[0]}, ¿cómo estás?")
print(f"Hola {nombres[1]}, ¿como vas?")
print(f"Hola {nombres[2]}, ¿qué tal?")
print(f"Hola {nombres[-3]}, ¿qué haces?")

                        #MIS VEHICULOS FAVORITOS

vehiculos = ["auto", "moto", "avion", "barco"]
print(f"me gustaria tener un {vehiculos[0]}")
print(f"la {vehiculos[1]} es muy rapida")
print(f"me gustaria viajar en un {vehiculos[2]}")
print(f"quiero navegar en un {vehiculos[-1]} por el ocenano")

                        #LISTA DE INVITADOS
                        
list_de_invitados = ["danielle", "minji", "haerin"]
print(f"Hola {list_de_invitados[0].title()}, te invito a cenar")
print(f"Hola {list_de_invitados[1].title()}, te invito a cenar")
print(f"Hola {list_de_invitados[2].title()}, te invito a cenar")

cant_go = "minji"
list_de_invitados.remove(cant_go)
print(f"lamentablemente {cant_go.title()} no puede asistir a la cena")

list_de_invitados.append("hanni")
print(f"gracias por confirmas tu asistencia {list_de_invitados[0].title()}")
print(f"gracias por confirmas tu asistencia {list_de_invitados[1].title()}")
print(f"gracias por confirmas tu asistencia {list_de_invitados[2].title()}")

print("encontre una mesa mas grande")

couples = ["lisa", "jisoo", "jennie"]
print(f"{list_de_invitados[0]} invito a {couples[0].title()}")
print(f"{list_de_invitados[1]} invito a {couples[1].title()}")
print(f"{list_de_invitados[2]} invito a {couples[2].title()}")

print("la mesa no llegara a tiempo, solo hay lugar para dos personas")

removed_guest = list_de_invitados.pop()
print(f"lo siento {removed_guest.title()}, no hay lugar en la mesa")
print(f"lo siento {list_de_invitados.pop().title()}, no hay lugar en la mesa")
removed_couple = couples.pop()
print(f"Lo siento {removed_couple.title()}, no hay lugar en la mesa")
print(f"Lo siento {couples.pop().title()}, no hay lugar en la mesa")

#                          ORDENAR LAS CANCIONES
songs = ["ditto", "like jennie", "gabriela", "cool with you", "narly"]
print(f"Favoritos <3: {songs}")
print(f"Calificar por nombre ^: {sorted(songs)}")
print(f"Calificar por fecha: {songs}") 
songs.sort()
print(f"Confirmar guardar por nombre ^: {songs}")
songs.reverse()
print(f"Guardando: {songs}")
print(f"{len(songs)} canciones guardadas en esta lista")
songs.reverse()
print(f"Favoritos <3: {songs}")