coche = input("que tipo de coche desea alquilar: ")
print(f"veamos si tenemos un {coche} para usted")

mesa = input("cuantos invitados vienen con usted?:")
mesa = int(mesa)
if mesa > 8:
    print("tendra que esperar una mesa")
else:
    print("su mesa esta lista")

numero = input("dame un numero: ")
numero = int(numero)
if numero % 10 == 0:
    print(f"{numero} es multiplo de 10")
else: 
    print(f"{numero} no es multiplo de 10")
    
