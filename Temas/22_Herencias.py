# No hace falta empezar de 0, siempre puedes heredar a una nueva con las mismas funciones
# e incluso incluir nuevas funciones

# Aqui tenemos la "CLASE BASE"
class car:
    def __init__(self, make, model, year):
        """Iniciamos watributos para definir al Auto"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0 # ponemos este parametro PREDEFINIDO en 0
    
    def get_descriptive_name(self):
        """Devuelve un ombre descriptivo"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Imprime el kilometraje del coche"""
        print(f"This car has {self.odometer_reading} miles on it ")
    
    def update_odometer(self, mileage):
        """Configura el kilometraje con el valor dado"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage 
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Añade la cantidad dada al kilomettraje"""
        self.odometer_reading += miles

# Y aqui la CLASE DERIVADA
class electric_car(car): #llamamos a la clase base
    """Representa a la clase de autos electricos"""
    def __init__(self, make, model, year): # "__init__" coge la informacion necesaria 
        """Inicializa los atributos de la clase base"""
        super().__init__(make, model, year) # "super()" nos permite a un metodo de la clase base


my_leaf = electric_car("nissan","leaf", 2024)
print(my_leaf.get_descriptive_name())

#Como ves podemos usar todas las funciones dentro de CAR en ELECTRIC CAR
# Ahora podemos añadir lo que queramos, por ejemplo "bateria"

class electric_car(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 40 # añadimos la bateria, pero solo funcionara en la nueva clase
    
    def descriptive_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

my_leaf = electric_car("nissan","leaf", 2024)
print(my_leaf.get_descriptive_name())
my_leaf.descriptive_battery()

#Asi como podeños añadir podemos anular
#supongamos que la clase car tiene un metodo llamado "tanque de gas"

class electric_car(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    
    def full_gas_tank(self):
        print("This car dosen't have a gas tank")

# Asi, si tratan de ver el tanke de gas, no podran porque es un coche electrico hohohoho

# COMPOSICION
# si notamos que hay varios atributos de uno mismo podemos mandar a una nueva clase

class battery:
    """Intento de Bateria de Coche"""
    def __init__(self, battery_size = 40): #si no damos un valor, se pondra el valor prederteminado
        self.battery_size = battery_size
    
    def descriptive_batery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

class electric_car(car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = battery()

my_leaf = electric_car('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()

# Parece mucho trabajo pero ahora podemos describir a la bateria sin saturar "electric_car"




