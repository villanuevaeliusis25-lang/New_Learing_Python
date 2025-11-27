#Crear una función pares() que imprima todos los números pares entre 1 y 50 usando un 
def pares():
    for n in range(0,51):
        if n % 2 == 0:
            print(n)
pares()

#Crear una función login() que pida una contraseña.
#La contraseña correcta es "python123".

def contraseña():
    correcta = "python123"
    intentos = 3
    while intentos != 0:
        usuario = input("Escriba la contraseña: ")
        if usuario != correcta:
            print("contraseña incorrecta")
            intentos -= 1
        else:
            print("Contraseñla correcta")
    if intentos == 0:
        print("No tienes mas intentos")

contraseña()

#Crear una función que reciba una lista y retorne únicamente la suma de los números pares.

def list_pares(lista):
    resultado = 0
    for pares in lista:
        if pares % 2 == 0:
            resultado += pares
    return print(f"El resultado final es: {resultado}")

usuario = 1
list = []
while usuario != 0:
    list.append(usuario)
    usuario = int(input("Dame un numero: \n presiona 0 para finalizar"))

list_pares(list)

#4. Verificar edad para registro (if + función)

def registro(edad):
    if edad >= 18:
        print("Registro permitido")
    else:
        print("Registro denegado")

usuario = int(input("Dime tu edad: "))
registro(usuario)

#Números del 1 al n, pero saltando múltiplos de 3

def conteo(num):
    for n in range(0,num+1):
        if n % 3 != 0:
            print(n)

usuario = int(input("Dime un numero: "))
conteo(usuario)

#Contador de números positivos, negativos y ceros

def contador(numeros):
    positivos = 0
    negativos = 0
    ceros = 0
    for n in numeros:
        if n > 0:
            positivos += 1
        elif n < 0:
            negativos += 1
        elif n == 0:
            ceros += 1
    print(f"los positivos son: {positivos}")
    print(f"Los negativos son: {negativos}")
    print(f"lso ceros son: {ceros}")
    
lista = []
usuario = "Inicio"
while usuario != "fin":
    usuario = input("Ingrese un numero ('fin' para terminar):   ")
    if usuario != "fin":
        usuario = int(usuario)
        lista.append(usuario)
contador(lista)