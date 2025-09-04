#                       SENTENCIAS IF 

#Examina una serie de condiciones y ejecuta un bloque de código tan pronto como una de las condiciones se evalúa como verdadera.

cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':# Si la variable car es igual a 'bmw', se ejecuta el bloque de código indentado.
        print(car.upper())
    else: # Si la condición del if no se cumple, se ejecuta el bloque de código del else.
        print(car.title())
    #else no es obligatorio, pero if sí.

# CONDICIONALES SIMPLES
# Verifica si una condición es verdadera (TRUE) y ejecuta un bloque de código si lo es.
# O  si lo califica como falso (FALSE) y no hace nada.

car == 'bmw' # Condición
car != 'Bmw' # Negación de la condición (!= significa "no es igual a")
#hay que tomar en cuenta que las mayúsculas y minúsculas importan en las comparaciones de cadenas.

#también podemos incluir comparaciones matemáticas
age = 18
age < 21 # menor que
age <= 21 # menor o igual que
age > 21 # mayor que
age >= 21 # mayor o igual que

# AND y OR
# Podemos combinar múltiples condiciones en una sola expresión condicional usando las palabras clave and y or.
age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 # Ambas condiciones deben ser verdaderas para que la expresión completa sea verdadera.
age_0 >= 21 or age_1 >= 21 # Solo una de las condiciones debe ser verdadera para que la expresión completa sea verdadera.

#                       COMPROBAR SI UN ELEMENTO ESTA EN UNA LISTA
#usamos la palabra clave "in"
requests_topings = ["mushrooms", "green peppers", "extra cheese"]
print("mushrooms" in requests_topings) #devuelve True
print("pepperoni" in requests_topings) #devuelve False|

#tambien existe "not in"
print("pepperoni" not in requests_topings) #devuelve True
print("mushrooms" not in requests_topings) #devuelve False

#                       CADENAS IF ELSE ELIF
# if-elif-else es una estructura condicional que comprueba cada una hasta que se cumple una condición.
age = 12
if age < 4:
    price = 0 # Almacenamos el precio en una variable
elif age < 18: # ELIF significa "else if"
    price = 5
#Podemos tener tantos bloques elif como queramos
else:
    price = 10
    #segun la edad, se asigna un valor diferente a la variable price
print(f"Tú entrada tiene un costo de {price}$.")

#if-elif-else es buena cuando necesitamos una unica prueba
#a veces necesitamos probar multiples condiciones independientes
requests_topings = ["mushrooms", "extra cheese"]
if "mushrooms" in requests_topings:
    print("Adding mushrooms.")
if "pepperoni" in requests_topings:
    print("Adding pepperoni.")
if "extra cheese" in requests_topings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")

#                       IF CON LISTAS 
# Usamos if para verificar si un elemento esta en una lista o no
# O podemos dar una oprden especial para ese elemento
requests_topings = ["mushrooms", "green peppers", "extra cheese"]
for requests_toping in requests_topings: #Empezamos a recorrer la lista
    if requests_toping == "green peppers": # Si el elemento es "green peppers"  
        print("Sorry, we are out of green peppers right now.") # Lew decimos que se acabo
    else: # Si no es "green peppers
        print(f"Adding {requests_toping}.") #recorremos la lista normalmente
print("\nFinished making your pizza!")  

# Tambien podemos verificar si una LISTA ESTA VACIA
requests_topings = []
if requests_topings: # Si la lista no esta vacia
    for requests_toping in requests_topings: # Empezamos a recorrer la lista
        print(f"Adding {requests_toping}.") 
    print("\nFinished making your pizza!")
else: # Si la lista esta vacia
    print("Are you sure you want a plain pizza?") # Le preguntamos si quiere una pizza sin nada

#Con MULTIPLES LISTAS 
# que pasa si queremos compbinar listas, entre los ingredientes disponibles y lo que quiere el cliente
avaible_topings = ["mushroom", "oliver", "green peppers", "pepperoni", "pineapple", "extra cheese"]
#son los ingredientes disponibles
requests_topings = ["mushroom", "french fries", "extra chesse"]
for requests_toping in requests_topings: #pasamos un bucle por la lista de solicitud para ver si esta disponible
    if requests_toping in avaible_topings:
        print(f"adding {requests_toping}") #si lo encuentra lo añade a la pizza
    else:
        print(f"sorry, we dont have {requests_toping}") #informa que no esta disponible
print("\nFinished making your pizza!")
