#                   RESTAURANTES
class Restaurante:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    def describir(self):
        print(f"Hay un nuevo restaurante llamado {self.nombre} de tipo {self.tipo}")
    
    def abrir(self):
        print(f"El restaurante {self.nombre} esta abierto!")
    
mi_restaurante = Restaurante("Dominos", "pizzeria")
mi_restaurante.describir()
mi_restaurante.abrir()

tu_restaurante = Restaurante("Sabrositos", "polleria")
tu_restaurante.describir()
tu_restaurante.abrir()

el_restaurante = Restaurante("Tu amigo", "hamburgueseria")
el_restaurante.describir()
el_restaurante.abrir()

#           USUARIO
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre.title()
        self.apellido = apellido.title()
    def descripcion(self):
        print(f"El nombre del usuario es: {self.nombre} {self.apellido}")
    def saludo(self):
        print(f"Bienvenido {self.nombre}")
        
usuario_1 = Usuario("ricky", "ricon")
usuario_2 = Usuario("bart", "simpson")
usuario_3 = Usuario("timmy", "turner")
usuario_1.descripcion()
usuario_1.saludo()
usuario_2.descripcion()
usuario_2.saludo()
usuario_3.descripcion()
usuario_3.saludo()