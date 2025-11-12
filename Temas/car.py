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
        if mileage >= self.odometer_reading: #el propietario no puede bajar el valor del kilometraje
            self.odometer_reading = mileage #se establece al valor dado
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Añade la cantidad dada al kilomettraje"""
        self.odometer_reading += miles #aqui va a ir sumando al valor que ya tenia
class battery:
    """Intento de Bateria de Coche"""
    def __init__(self, battery_size = 40): 
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