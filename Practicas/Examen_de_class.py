# 9-13. Dados: Haga una clase Dados con un atributo llamado caras , que tenga un valor predeterminado de 6. 
# Escriba un método llamado tirar_dado() que imprima un número aleatorio entre 1 y el número de caras que tenga el dado. 
# Haga un dado de 6 caras y tírelo 10 veces. Haga un dado de 10 caras y otro de 20. Lance cada dado 10 veces
import random

class Dado:
    def __init__(self, caras, tiradas):
        
        self.caras = caras
        self.tiradas = tiradas
    
    def tirar_dado(self):
            for i in range(1, self.tiradas +1):
                resultado  = random.randint(1, self.caras)
                print(f"Dado {i}: {resultado}")

tirada = Dado(6,7)
tirada.tirar_dado()

# 9-14. Lotería: Cree una lista o tupla que contenga series de 10 números y 5 letras.
# Seleccione aleatoriamente cuatro números o letras de la lista e imprima un mensaje diciendo que cualquier boleto con estos cuatro números o letras está premiado

Boleto = [1,5,8,3,4,5,6,7,8,9,0,"t","k","g","a","o"]
eleccion = random.sample(Boleto, 4)
print(f"El boleto premiado tiene : {eleccion}")

#9-15. Análisis de la lotería: 
# Puede usar un bucle para ver lo difícil que sería ganar el tipo de lotería que acaba de modelar. 
# Haga una lista o tupla llamada mi_boleto .
# Escriba un bucle que saque números hasta que gane su boleto.
# Imprima un mensaje que indique cuántas veces ha tenido que ejecutarse el bucle hasta que ha salido el número ganador
intentos = 0
mi_boleto = []

while True:
    # Generar un boleto aleatorio
    mi_boleto = random.sample(Boleto, 4)
    intentos += 1
    
    # Verificar si ganamos (comparar sin importar el orden)
    if set(mi_boleto) == set(eleccion):
        break

print(f"¡Felicidades! Tu boleto {mi_boleto} es ganador.")
print(f"Te tomó {intentos} intentos ganar la lotería.")