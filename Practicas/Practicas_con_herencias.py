#9-6. Carrito de helados: Un carrito de helados es, en cierto modo, parecido a un restaurante.
# Escriba una clase llamada "CarritoDeHelados" que herede de la clase Restaurante del ejercicio 9-1 o del 9-4. Servirá cualquiera de las dos versiones, así que coja la que más le guste. 
# Añada un atributo llamado sabores que almacene una lista de sabores de helado. 
# Escriba un método que muestre los sabores. Cree una instancia de CarritoDeHelados y llame a ese método.

class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.servicio = 0
    
    def describir(self):
        print(f"Hay un nuevo restaurante llamado {self.nombre} de tipo {self.tipo}")
    
    def abrir(self):
        print(f"El restaurante {self.nombre} esta abierto!")
    
    def atendidos(self, clientes):
        self.servicio += clientes
        print(f"El dia de hoy atendio {self.servicio} personas")
    
    def nuevos_clientes(self, nuevos):
        self.servicio += nuevos
    
    def cerrar_caja(self):
        print(f"se cierra la caja con {self.servicio} clientes atendidos")

class carrito_de_helados(Restaurante):
    def __init__(self, nombre, tipo):
        super().__init__(nombre, tipo)
        self.sabores = ["chocolate","vainilla","uva"]
    
    def mostrar_sabores(self):
        print("Los sabores son los siguientes:")
        for i in self.sabores:
            print(i)

carrito = carrito_de_helados("cokie", "Heladeria")
carrito.describir()
carrito.mostrar_sabores()


# 9-7. Admin: Un administrador es un tipo especial de usuario. Escriba una clase llamada Admin que herede de la clase Usuario del ejercicio 9-3 o del 95.
# Añada un atributo privilegios que acoja una lista de cadenas como "puede añadir comentario" , "puede borrar comentario" , "puede vetar usuarios" , etc. 
# Escriba un método llamado show_privileges() que enumere el conjunto de privilegios del administrador. Cree una instancia de Admin y llame al método

class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
        self.intentos_inicio = 0
        
    def descripcion(self):
        print(f"El nombre del usuario es: {self.nombre} {self.apellido}")
    
    def saludo(self):
        print(f"Bienvenido {self.nombre}, te tomo {self.intentos_inicio} intentos")
    
    def intentos(self ):
        self.intentos_inicio += 1
    
    def restablecer(self):
        self.intentos_inicio = 0

class admin(Usuario):
    
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.privilegios = ["puede añadir comentario", "puede borrar comentario", "puede vetar usuarios"]
    
    def mostrar_privilegios(self):
        print("Tiene los siguientes privilegios:")
        for i in self.privilegios:
            print(i)

usr = admin("eliu", "Villanueva")
usr.mostrar_privilegios()

#9-8. Privilegios: Escriba una clase Privilegios aparte. 
# Esta clase debería tener un atributo, privilegios , que almacene una lista de cadenas como la descrita en el ejercicio anterior. 
# Mueva el método show_privileges() a esta clase.
# Haga una instancia de Privilegios como atributo de la clase Admin . 
# Cree una nueva instancia de Admin y use su método para mostrar los privilegios.
class privilegios:
    
    def __init__(self):
        self.privilegios = ["puede añadir comentario", "puede borrar comentario", "puede vetar usuarios"]
        
    
    def mostrar_privilegios(self):
        print("Tiene los siguientes privilegios:")
        for i in self.privilegios:
            print(i)

class admin(Usuario):
    
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.privilegios = privilegios()

usr.mostrar_privilegios()