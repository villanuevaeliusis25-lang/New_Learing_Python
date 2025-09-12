#           MOVER ENTRAE LISTAS
pedidos_bocadillos = ["pollo", "coca-cola", "hamburguesa", "papas fritas"]
bocadillos_terminados = []
while pedidos_bocadillos:
    pedido = pedidos_bocadillos.pop()
    print(f"su {pedido} esta listo")
    bocadillos_terminados.append(pedido)
print("-------SU CONSUMO TOTAL ES-------")
for bocadillo in bocadillos_terminados:
    print(bocadillo.title())
    
#               ELIMINAR ELEMENTOS

pedidos_bocadillos = ["pollo","pastrami", "coca-cola","pastrami", "hamburguesa","pastrami", "papas fritas"]
print(pedidos_bocadillos)
print("ya no queda pastrami")
while "pastrami" in pedidos_bocadillos:
    pedidos_bocadillos.remove("pastrami")
print(pedidos_bocadillos)

#              INTRODUCIR ELEMENTOS
datos = {}
bandera = True

while bandera:
    nombre = input("Cual es tu nombre? ")
    lugar = input("Donde te gustaria vacacionar? ")
    datos[nombre] = lugar
    respuesta = input("Te gustaria que otra persona responda? (si/no)")
    if respuesta == "no":
        bandera = False
for nombre, lugar in datos.items():
    print(f"A {nombre.title()} le gustaria vacacionar en {lugar.title()}")