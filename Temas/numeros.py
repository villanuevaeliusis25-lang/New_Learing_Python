#En python los numeros no llevan comillas
entero = 4 #"int" es para enteros
flotante = 5.5 #"float" es para numeros con decimales
#Podemos sumar, restar, multiplicar, dividir y elevar con "**#"
suma = entero + flotante 
print(suma)
#Los numeros se sumaran como numeros, no como cadenas de texto
#al dividir siempre dara un numero flotante
division = entero / 2
print(division)
#si queremos una division entera usamos "//"

#Podemos escribir numeros largos usando guiones bajos para mayor legibilidad
numero_grande = 1_000_000
print(numero_grande) #No se leera con los guiones bajos

#Tambien podemos asignar valores a multiples variables en una sola linea
x, y, z = 1, 2, 3
print(x)
print(z)

#Una constante es como una variable cuyo valor permanece invariable a lo largo del programa
MAX_CONECCTION = 5000 #Por convención, las constantes se escriben en mayúsculas