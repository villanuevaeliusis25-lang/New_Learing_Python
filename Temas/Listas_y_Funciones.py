#                       PASAR UNA LISTA
# Las funciones tienen acceso al contenido de las listas, eso las vuelve mas eficiente

def greet_users (names): #espera una lista con los nombres
    """Imprime un sencillo saludo a para cada usuario"""
    for name in names:
        msg =f"Hello, {name.title()}!"
        print(msg)
usernames = ["hanna", "ty", "margot"] #guardamos los nombres
greet_users(usernames) #imprime la funcion con los nombre en "usernames"


#                   MODIFICAR UNA LISTA EN UNA FUNCION
# Tal vez queremos cambiar de una lista a otra, modificar sus elementos.
# Los cambios que se hacen son permanentes
# por ejemplo, este ejercicio sobre a medida que imprime se guarda en completados: 

#la primera funcion se ocupara de la impresion de los diseños
def print_models(unpringted_designs, completed_models):
    """Simula imprimir cada diseño, hasta que no tenga ninguno.
    Mueve cada diseño a completed_models despues de la impresion"""
    while unpringted_designs:
        current_design = unpringted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
        
# Esta segunda funcion, resumira las impresiones que se han hecho
def show_completed_models(completed_models):
    """Muestra los modelos que se han imprimido"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unpringted_desingns = ["phone case", "robot pendant", "dodecahedron"]
completed_models = []
print_models(unpringted_desingns,completed_models)
show_completed_models(completed_models)


#           EVITAR QUE UNA FUNCION MODIFIQUE UNA LISTA
# en este caso tal vez queramos mantener la primera lista, para revisarla despues.
# Para eso podemos copiar la lista:

#  nombre_funcion(nombre_lista[:])
print_models(unpringted_desingns[:],completed_models)
#en esta ocacion, sigue recibiendo los nombres a imprimir pero es solo una copia de la original