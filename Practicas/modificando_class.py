# Empiece con el programa del ejercicio 9-1. Añada un atributo llamado número_servido con un valor predeterminado de 0
#Cree una instancia llamada restaurante a partir de esta clase. Imprima el número de clientes a los que ha servido el restaurante, cambie ese valor y vuelva a imprimirlo.
#Añada un método llamado "establecer_número_servido()" que le permita congurar el número de clientes a los que se ha servido. Llámelo con un número nuevo y vuelva a imprimir el valor.
#Añada un método llamado "incrementar_número_servido()" que le permita incrementar el número de clientes atendidos. Llámelo con cualquier número que pueda representar a cuántos clientes se ha servido en un día laborable normal

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
        

rest = Restaurante("Pollos Tunel", "broasteria")
rest.describir()
rest.abrir()
rest.atendidos(10)
rest.cerrar_caja()
rest.nuevos_clientes(20)
rest.cerrar_caja()

# 9-5. Intentos de inicio de sesión: Añada un atributo intentos_inicio a la clase Usuariodel ejercicio 9-3. 
# Escriba un método llamado incrementar_intentos_inicio() que aumente el valor de  intentos_inicio en 1. 
# Escriba otro método llamado restablecer_intentos_inicio() que restablezca el valor de intentos_inicio a 0.
# Haga una instancia de la clase Usuarioy llame varias veces a incrementar_intentos_inicio(). Imprima el valor de intentos_inicio para asegurarse de que se ha incrementado correctamente y luego llame a restablecer_intentos_inicio(). Vuelva a imprimir intentos_inicio para asegurarse de que se ha restablecido a 0

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

user = Usuario("Eliu", "Villanueva")
user.intentos()
user.intentos()
user.intentos()
user.intentos()
user.saludo()
user.restablecer()
user.saludo()