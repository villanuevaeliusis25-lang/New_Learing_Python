#                   MENSAJES 
def mostrar_mensajes(mensajes):
    for mensaje in mensajes:
        print(mensaje)
cartas = ["hola mundo", "me gusta python", "funciones y for <3"]
mostrar_mensajes(cartas)

#               CORREOS ENVIADOS 
def enviar_mensajes(mensajes, enviados):
    while mensajes:
        cargando = mensajes.pop()
        print(f"enviando: {cargando}")
        enviados.append(cargando)

def Mostrar_enviados(enviados):
    print("\nFueron enviados:")
    for enviado in enviados:
        print(enviado)

mensajes = ["Hello word", "Im coding", "I wanna sleap"]
enviados = []

enviar_mensajes(mensajes[:], enviados)
Mostrar_enviados(enviados)
print(mensajes)
print(enviados)