#                            SENTENCIAS SIMPLES IF
song = "Cool with you"
if song == "Cool with you":
    print("Esa es mi cancion favorita")

girlgroup = "Blackpink"
if girlgroup == "NewJeanz":
    print("Me encanta Blackpink")
else:
    print(f"{girlgroup.lower()} es mi otro grupo favorito")

edad = 27
edad_menor = 18
if edad >= 30 and edad_menor >= 18:
    print("TRUE")
else:
    print("FALSE")

edad = 35
if edad >= 30 and edad_menor >= 18:
    print("TRUE")
else:
    print("FALSE")

edad_menor = 17
if edad >= 30 or edad_menor >= 1:
    print("TRUE")
else:
    print("FALSE")

NewJeanz = ["Hanni", "Danielle", "Haerin", "Minji", "hyen"]
if "Hanni" in NewJeanz:
    print("Hanni es mi favorita")
if "Lisa" in NewJeanz:
    print("Lisa no esta en NewJeanz")
if "Lisa" not in NewJeanz:
    print("Lisa no esta en NewJeanz")

#                            CADENAS IF-ELIF-ELSE
aliens = ['green', 'yellow', 'red']
if 'green' in aliens:
    print("Has ganado 5 puntos")
if "brown" in aliens:
    print("De donde salio uno marron?")

aliens.append('white')

if 'white' in aliens:
    print("Has ganado 10 puntos") #aqui ya termina la cadena if
elif 'yellow' in aliens: #si pondria if en vez de elif, se evaluaria la condicion aunque la anterior se haya cumplido
    print("Has ganado 5 puntos")
else:
    print("Has ganado 15 puntos")

edad = 27
if edad < 4:
    print("eres un bebe")
elif edad < 18:
    print("eres un niño")
elif edad < 65:
    print("eres un adulto")

frutas = ["manzana", "banana", "pera"]
if "manzana" in frutas:
    print("Me encantan las manzanas")
if "banana" in frutas:
    print("Me encantan las bananas")
if "pera" in frutas:
    print("Me encantan las peras")
if "kiwi" not in frutas:
    print("deberiamos añadir kiwi a frutas")
    
#               IF CON LISTAS
usuarios = ["admin", "jorgito_pro", "miguelito052", "novia_de_miguel"]
for usr in usuarios:
    if usr == "admin":
        print("Bienvenido, quieres ver un informe de estado?")
    else:
        print(f"{usr} a iniciado secion")
usuarios.clear()
if usuarios: 
    for usr in usuarios:
        print(f"Bienvenido {usr}")
    else:
        print("Necesitamos nuevos usuarios")

usr_disponibles = ["alejandro01", "rocozo", "GrayColori", "CriminalSimpson", "HannaArtWork"]
usr_nuevos = ["alejandro01", "kkjjer", "CriminalSimpson", "oocBrazil", "GrayColori"]
for usr_nuevo in usr_nuevos:
    if usr_nuevo in usr_disponibles:
        print(f"Creaste una cuenta nueva, Bienvenido {usr_nuevo}")
    else:
        print("Ese nombre de usuario no esta disponible")
        
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]
grados = []
for numero in numeros:
    if numero == 1:
        grados.append(f"{numero}st")
    elif numero == 2:
        grados.append(f"{numero}nd")
    elif numero == 3:
        grados.append(f"{numero}rd")
    else:
        grados.append(f"{numero}th")
print(*grados)