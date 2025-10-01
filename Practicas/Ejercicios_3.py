#                   VERIFICADOR DE PALINDROMOS
# Determina si una palabra se lee igual al derecho y al reves
# Ignora mayusculas/minusculas y espacios
def es_palindromo(palabra):
    palabra_limpia = palabra.lower().replace(" ","")
    palabra_invertida = ""
    for letra in palabra_limpia:
        palabra_invertida = letra + palabra_invertida
    return palabra_limpia == palabra_invertida


# Pruebas
print(es_palindromo("reconocer"))    # True
print(es_palindromo("Ana"))          # True  
print(es_palindromo("Python"))       # False

# Mas corto
def es_palindromo(palabra):
    palabra_limpia = palabra.lower().replace(" ", "")
    return palabra_limpia == palabra_limpia[::-1] 
# puedes obtener una parte de una cadena (o lista) usando la sintaxis [inicio:fin:paso].
# [::-1] significa:
# inicio: vacío (empieza desde el principio)
# fin: vacío (hasta el final)
# paso: -1 (va hacia atrás)


#                       ANALIZADOR DE TEXTO 
# Analiza: el numero de palabras
#          -la palabra mas larga
#          -frecuencia de palabras
#          -logitud promedio 
def analizar_texto(texto):
    palabras = texto.split() #"split()" divide por espacios
    num_palabras = len(palabras)
    
    palabra_mas_larga = ""
    for palabra in palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    
    frecuencia = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    
    total_letras = sum(len(palabras) for palabra in palabras)
    logitud_promedio = total_letras / num_palabras
    
    return  {
        "numero de palabras": num_palabras,
        "palabra mas larga": palabra_mas_larga,
        "frecuencia" : frecuencia,
        "Longitud promedio" : logitud_promedio
    }
    pass
# Pruebas:
texto_ejemplo = "El rápido zorro marrón salta sobre el perro perezoso"
resultado = analizar_texto(texto_ejemplo)
print(resultado)

#               CALCULADORA DE EDAD
# Calcula la edad actual y cuantos años tendra en 2050
def calcular_edad(año_nacimiento, año_actual):
    edad_actual = año_actual - año_nacimiento
    edad_2050 = 2050 - año_nacimiento
    print(f"Tu edad actual es: {edad_actual}")
    print(f"tu edad en 2050 sera: {edad_2050}")
    
# Pruebas:
calcular_edad(1990, 2025)  # (34, 60)
calcular_edad(2010, 2025)  # (14, 40)


#               CONTADOR DE CARACTERES
# Cuenta:
#    - Total de caracteres
#    - Número de letras (solo a-z, A-Z)
#    - Número de dígitos
#    - Número de espacios
def contador_caracteres(texto):
    total_caracteres = len(texto)
    letras = 0
    digitos = 0
    espacios = 0
    
    print("Analizando texto:", repr(texto))
    for caracter in texto:
        
        if caracter.isalpha():
            letras += 1
            
        elif caracter.isdigit():
            digitos += 1
            
        elif caracter.isspace():
            espacios += 1
    
    return {
        'total': total_caracteres,
        'letras': letras,
        'digitos': digitos,
        'espacios': espacios
    }
# Pruebas:
print(contador_caracteres("Hola 123!"))  # {'total': 9, 'letras': 4, 'digitos': 3, 'espacios': 1}