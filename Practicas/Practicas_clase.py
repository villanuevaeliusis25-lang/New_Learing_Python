#Obtener iniciales y poner en mayusc
def Iniciales(nombre):
    partes = nombre.split()
    iniciales = ""
    for parte in partes:
        iniciales += parte[0].upper()
    return iniciales

print(Iniciales("Eliu villanueva"))


# Revisar si es un palindromo o no lo es 
def palindromos(frase):
    palindromo = ""
    for n in frase[::-1]:
        palindromo += n
    if palindromo == frase:
        print(f"'{frase}' Es un palindromo")
    else:
        print("No es un palindromo")

palindromos("reconocer")

#otra forma 

def es_palindromo(frase):
    invertido = frase[::-1]
    if invertido.lower() == frase.lower():
        print("Es un palindromo")
    else:
        print("No es un palindromo")

es_palindromo("RecOnocer OSO")    

#Funcion que cree un programa que cuente cuantas palabras tienen mas de 5 letras

def contador_5(frase):
    dividido = frase.split()
    contador = 0
    for n in dividido:
        if len(n) > 5:
            contador += 1
    return contador
print(contador_5("Gemini genero este mensaje"))


#Funcion que reemplace los espacios por "_" y todo minus

def cambios(frase):
    cambio = frase.strip().replace(" ", "_")
    return cambio.lower()
print(cambios(" GemIni HiZo este TraBAjo "))

#otra forma
def normalizar_frase(frase):
    palabras = frase.strip().lower().split()
    return "-".join(palabras)
print(normalizar_frase(" PyThOn es MuY facIl "))

#Crear una funcion que reciba una frase con comas 
#devuelve una frase normal con espacios

def adios_comas(frase):
    comas_bye = frase.strip().replace(",", " ")
    return comas_bye
print(adios_comas("Python,Java,c++"))

def limpiar_comas(frase):
    palabras  = frase.split(",")
    return " ".join(palabras)
print(limpiar_comas("Python,Java,c++"))


