#                               CLASES
#L a programacion orientada a objetos (POO) escribimos "clases" que representan 
# Cosas y situaciones en la vida real y creamos "objetos" basados en esas clases

class dog: 
    """Un intento sencillo de modelar un perro"""
    def __init__(self, name, age):
        """Inicia los atributos de nonbe y edad"""
        self.name = name
        self.age = age
    def sit(self):
        """Simula un perro sentandose en respuesta a una orden"""
        print(f"{self.name} is now sitting")
    def roll_over(self):
        """Simula hacer la croqueta en respuesta de una orden"""
        print(f"{self.name} rolled over!")

# Empezamos definiendo la funcion,por el momento no necesita "()" porque la hacemos desde 0
# despues describimos lo que hace esta clase

# EL METODO "__init__"
# Toda funcion dentro de una clase es un "metodo"
# "__init__" es un metodo especial que que se ejecutara automaticamente 
# Lo definimos con 3 parametros "self, name, age"
# cuando llamamos a la clase esta pasa automaticamente a "self"

my_dog = dog("willy", 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
# Aqui se muestra como busca el valor de los atributos 
# en "my_dog.NAME" buscara a NAME y en "my_dog.AGE" buscara AGE

# LLAMAR METODOS
# Para llamar a un método, damos el nombre de la instancia
#  y el método al que queremos llamar separados por un punto.
my_dog.sit()
my_dog.roll_over()

# LLAMAR MULTIPLES INSTANCIAS
#  Podemos crear todas las instancias que necesitemos a partir de una clase
your_dog = dog("Lucy", 3)
print(f"My dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()

