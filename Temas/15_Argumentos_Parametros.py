#                   ARGUMENTOS Y PARAMETROS
# PARAMETRO: Variables definidas en la función que actúan como "placeholders" para recibir valores.
def saludar(nombre, mensaje):  # 'nombre' y 'mensaje' son parámetros
    print(f"{mensaje}, {nombre}!")

# ARGUMENTO: Los valores reales que se envían a la función cuando se invoca.
saludar("Ana", "Hola")  # "Ana" y "Hola" son argumentos

#Como vimos, se puede usar desde uno a varios parametros y llamar la funcion varias veces
def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')
#Como puede ver el orden es importante, no queremos ver un harry llamado hamster

#               PALABRAS CLAVE
# Es un par nombre-valor que pasamos a una funcion 
# Esto nos evita preocuparnos por el orden 

def describe_pet(animal_type, pet_name):
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')
# la funcion "describe_pet" no ha cambiado,
# pero ahora le decimos explicitamente que parametro debe asociarse 

#           VALORES PREDETERMINADOS
# Si ya tenemos un valor que usamos regularmente, lo mejor tenerlo prederteminado
# En este caso casi siempre usaremos "dog" como tipo de animal

def describe_pet(pet_name, animal_type='dog'):
#observe que cambiamos de lugar porque el unico valor solicitado sera el nombre 
    """Muestra información sobre una mascota."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

#       ERRORES
# Si dejamos vacio lor parametros, python lo reconoce y nos dice donde esta el error 
# Al igual si tenemos mas valores de los que pedimos
