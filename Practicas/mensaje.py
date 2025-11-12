mensaje = "Hola Eliu, Que aprenderemos hoy?"
nombre = "Eliu"
print(nombre.title())
print(nombre.upper())

cita = "¨And if not, he is still good¨"
biblia = "Daniel 3:18"
print(f'Mi cita favorita es {cita} del libro de {biblia}')

nombre = " Eliu "
print(f"Nombre:\n{nombre.rstrip()} Villanueva") #"\n" es para salto de linea
print(f"Nombre:\t{nombre.lstrip()} Villanueva") #"\t" es para tabulador
print(nombre.strip() + "Villanueva")