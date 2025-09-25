#                   FUNCIONES
# Son bloques de código con nombre diseñados para hacer una tarea específica
# si tienes que hacer algo mas de 3 veces, automatizalo

# funcion = "def", para informar que estamos haciendo una funcion
# luego definimos el nombre de la funcion y el tipo de trabajo que realizara
def greet_user():                       #empieza el cuerpo de la funcion 
    """Muestra un simple saludo"""      #ponemos el comentario o "cadena de documentacion"
    print("Hello!")                     # y tenemos el codigo de la funcion

greet_user()                            #Cuando queramos usar una funcion hay que llamarla 

#               AÑADIR INFORMACION 
#Solo tenemos que añadir la informaciondentro del "()"
def greet_user(username):
    """Muestra un saludo personalizado"""
    print(f"Hello, {username.title()}!")

greet_user("jesse")
#se nota que añadimos el valor al llamar la funcion? y se almacena en "username"?

