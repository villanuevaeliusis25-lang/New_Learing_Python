#                               PASAR DE UNA LISTA A OTRA
# Empieza con usuarios que hay que verificar,
# y una lista vacía para alojar a los usuarios confirmados.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# El bucle continuara hasta que la primera lista este vacia
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    # ".pop()" eliminara desde el ultimo a las personas dentro la primera lista
    print(f"Verifying user: {current_user.title()}")
    #imprimes segun el usuario que se va eliminando
    confirmed_users.append(current_user)
    #añade todos los eliminados a la lista vacia
    
# Muestra todos los usuarios confirmados
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
        #recorre los nuevos nombres en la lista anteriormente vacia
    print(confirmed_user.title())

#                               ELIMINAR VALORES ESPECIFICOS
# Usamos la funcion "remove()" para sacar a un elemento 
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets: #mientras tenga "cat" en la lista
    pets.remove('cat') #removera el valor "cat"
print(pets)

#                     RELLENAR UN DICCIONARIO CON ENTRADA DE USUARIO
# Podemos hacer que el usuario rellene los datos que necesitemos 
responses = {}
# Configura una bandera para indicar que la encuesta está activa.
polling_active = True
while polling_active:
# Pide el nombre y la respuesta de la persona.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")
# Guarda la respuesta en el diccionario.
    responses[name] = response
# Averigua si alguien más va a hacer la encuesta.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# La encuesta está completa. Muestra los resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")