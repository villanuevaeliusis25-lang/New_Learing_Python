#           PASAR UN NUMERO ARBITIARIO DE ARGUMENTOS
# A veces no sabemos cuantos parametros necesitaremos
def make_pizza(*toppings):
#El asterisco "*" que cree una tupla vacia que contenga los valores que reciba
    """Imprime una lista de los ingradientes solicitados"""
    print("\nMaking a Pizza whit the following toppings")
    for topping in toppings:
        print(f"- {topping}")
#Ahora ponemos los parametros que queramos
make_pizza("pepperoni") #Como ve crea una tupla aunque solo sea un valor
make_pizza("mushrooms", "green peppers", "extra cheese")


#         MEZCLAR ARGUMENTOS POSICIONALES Y ARBITRARIOS
#Para hacer esto se debe poner de ultimo, el que acepta mas de un parametro
def make_pizza(size, *toppings):
    """Ahora con rebanadas, tamaño o size en ingles"""
    print(f"\nMaking a {size}-inch Pizza whit the following toppings")
    for topping in toppings:
        print(f"- {topping}")
#ponemos primero el "tamaño o rebanadas" y lo demas seran los extras
make_pizza(16, "pepperoni") 
make_pizza(18, "mushrooms", "green peppers", "extra cheese")

#       USAR ARGUMENTOS DE PALABRA CLAVE ARBITRARIOS
# Muchas veces necesitaremos varios pares de "valor-clave"
# y como nosabemos cuantos son podemos hacer lo siguiente:
def build_profile(first, last, **user_info):
#el doble asterisco "**" indica que se creara un diccionario vacio
    
    """Crea un perfil de usuario"""
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein",
                            location = "princeton",
                            field = "physics")
print(user_profile)
