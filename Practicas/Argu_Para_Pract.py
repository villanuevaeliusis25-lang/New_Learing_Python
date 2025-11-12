#               VENTA DE CAMISETAS
def camisetas(talla, mensaje):
    """Pide la talla y el mesnaje impreso"""
    print(f"Usted escogio la talla: {talla} ")
    print(f"Con el mensaje impreso: {mensaje.title()} ")

camisetas("M", mensaje="hola.mundo")

#           VALORES PREDERTEMINADOS Y CAMBIOS 
def camisetas(talla = "XXXL", mensaje = "Me encanta Python"):
    """Pide la talla y el mesnaje impreso"""
    print(f"Usted escogio la talla: {talla} ")
    print(f"Con el mensaje impreso: {mensaje.title()} ")

camisetas()
camisetas(talla = "M")
camisetas(talla="S", mensaje="toy chiquito")

#               CIUDADES
def mapas(pais, ciudad):
    """Paises del Mundo con sus ciudades"""
    print(f"{ciudad.title()} esta en {pais.title()}")

mapas("bolivia", "cochabamba")
mapas(pais="argentina", ciudad="buenos aires")
mapas("peru", "montevideo")