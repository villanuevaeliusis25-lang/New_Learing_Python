#                       BUCLE "WHILE"
#El "bucle for" coge una colección de elementos y ejecuta un bloque de código una vez por cada elemento de la colección.
# en cambio "WHIILE" se ejecuta mientras se cumpla una CONDICION
current_number = 1
while current_number <= 5:
    #se seguira ejecutando mientras el numero sea menor a 5
    print(current_number)
    #imprime el valor 
    current_number += 1
    #añade un numero, es abreviacion de (current_number = current_number + 1)
#llegado a 5 finaliza el programa

# tambien podemos hacer que el programa continua hasta que el usuario lo permita
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != "quit":
    message = input(prompt)
    if message != "quit":
        print(message)

#               BANDERAS
# ¿qué pasa con programas más complejos en los que distintos eventos pueden hacer que el programa deje de ejecutarse?
# podemos definir una variable que determine si todo el programa está activo o no.
# Podemos escribir mientras sea "TRUE" y detenerse cuando sea "FALSE"

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

active = True
# podemos como true paraque el programa inicie activo
while active: 
    #esto simplifica while porque no hace la comparacion, mientras sea true el programa continua
    message = input(prompt)
    if message == 'quit':
        #si el usuario escribe "quit" active cambia a false 
        active = False
        #el programa termina
    else:
        print(message)

#                   BREAK
#para SALIR de un bucle while podemos usar breack
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    #un bucle que empieza con "TRUE" se ejecutara eternamente
    city = input(prompt)
    if city == 'quit':
        break
# a menos que "BREAK" lo interrumpa
    else:
        print(f"I'd love to go to {city.title()}!")

#               CONTINUE
#En lugar de interrumpir, podemos usar "continue" para volver al inicio en funcion del resultado

current_number = 0
#empezamos con una variable < a 10
while current_number < 10:
    current_number += 1
    #aumentamos el numero de 1 en uno
    if current_number % 2 == 0:
        #si el residuo del numero es igual a 0
        continue
    #continuara, omitiendo los pares
    else: #en caso de que no 
        print(current_number) 
    #imprimira los numeros impares
    
#           CONTROL-C PARA PARAR LOS BUCLES INFINITOS