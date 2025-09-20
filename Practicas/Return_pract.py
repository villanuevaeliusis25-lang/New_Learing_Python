#           CIUDAD PAIS
def mapa(ciudad, pais):
    localidades = f"{ciudad}, {pais}"
    return localidades.title()
print(mapa("Bolivia", "La Paz"))
print(mapa("Argentina", "Buenos Aires"))
print(mapa("Peru", "Lima"))

#               ARTISTAS
def hacer_album(artista, album, canciones=None):
    discografia = {
        "artista" : artista,
        "album" : album,
        "canciones" : canciones
    }
    return discografia
artista_1 = (hacer_album("My chemical romance","the black parade"))
artista_2 = (hacer_album("fall out boy", "folie a deux", 3))
print(artista_1)
print(artista_2)

#                TIENDA DE MUSICA
def compras(artista, album, canciones=None):
    """Funcion que hace de tienda de albumes"""
    discografia = {
        "artista" : artista,
        "album" : album,
        "canciones" : canciones
        }
    return discografia

while True:
    print("Dime el artista y el album que estas buscado:")
    print("Escribe q para terminar")
    
    arts = input("Cual es el nombre del artista: ")
    if arts == "q":
        break
    alb = input("Cual es el nombre del album: ")
    if alb == "q":
        break
    songs = int(input("Sabes cuantas canciones tiene?: "))
    if songs == "No":
        break
    compra_completa = compras(arts, alb, songs )
    print(f"\nTu compra completa es, {compra_completa}")