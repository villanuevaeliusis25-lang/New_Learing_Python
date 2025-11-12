
#Tenemos una Instancia con valores prederteminados para eso podemos usar "__init__"


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
    
new_car = car("audi", "a4", 2024)
print(new_car.get_descriptive_name())
new_car.read_odometer()

#Podemos MODIFICAR el atributo directaamete llamando al parametro
new_car.odometer_reading = 23
new_car.read_odometer()

# A veces es necesario hacer esto, pero muchas veces queremos que el valor se vaya 
# ACTUALIZANDO y para ello agragamos la funcion "update_odometer"

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

new_car = car("audi", "a4", 2024)
new_car.update_odometer(23)
new_car.read_odometer()


# A veces en lugar de reemplazar el numero solo queremos que aumente
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

used_car = car("subaru", "outblack", 2019)
print(used_car.get_descriptive_name())

used_car.update_odometer(23) #damos el kilometraje del auto usado
used_car.read_odometer()

used_car.increment_odometer(10) #y añadimos el valor que nosotros manejamos
used_car.read_odometer()

