#                   INTRODUZCA SUS INGREDIENTES
prompt = "\nPor favor, introduzca los ingreditentes de su pizza:"
prompt += "\nIntroduzca 'quit' cuando halla terminado. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(f"{message.title()} se agrego a su pizza.")


#                   VALOR DE SU BOLETO
prompt = "\nQue edad tienes?: "
prompt += "\nPresione 'quit' si es el ultimo. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        message = int(message)
        if message <= 3:
            print("entrada gratis")
        elif message <= 12:
            print("entrada a 8$")
        elif message >= 12:
            print("entrada a 12$")