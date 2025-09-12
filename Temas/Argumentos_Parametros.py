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