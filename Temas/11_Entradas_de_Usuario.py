#                   ENTRADAS DE USUARIO
# Para PEDIR INFORMACION a un usuario, nesecitamos la funcion "INPUT()"
# La función input() PAUSA el programa y espera a que el usuario introduzca texto
message = input("tell me someting, and I will repeat it back to you: ")
#le decimos al usuario que tipo de informacion debe introducir
print("message")
#el programa espera la respuesta hasta que el usuario presiona INTRO

#Siempre debemos ser claros en la informacion que necesitamos
name = input("Please enter your name: ")
print(f"\nHello, {name}!")
#a veces es necesario usar mas de una linea
prompt = "If you share your name, we can personalize the messages you see"
prompt += "\nWhats your first name?" # el "+=" añade una nueva cadena al final de "prompt"
#podemos asignar indicaciones a una variable y pasarla a una funcion "input()"
name = input(prompt)
print(f"\nHello, {name}!")

# Usamos "INT()" para entradas numericas
#hasta el momento el progrma señala todo como una cadena, pero si queremos hacer operaciones: 
height = input("How tall are you, in inches? ")
height = int(height)
# "int()" lo convierte en una representacipn numerica
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you are a little older.")
#el programa puede comprar porque int lo convierte en una representacion numerica

# EL OPERADOR MODULO
# (%) este operador divide un numero entre otro y devuelve el resto 
operacion = 5 % 3
print(operacion) #sale 2
