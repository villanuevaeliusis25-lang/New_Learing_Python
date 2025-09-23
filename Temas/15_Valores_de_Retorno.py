#               VALORES DE RETORNO
# Una función no siempre tiene por qué mostrar su salida
# directamente. En vez de eso, puede procesar datos y devolver un
# valor o un conjunto de valores.

#Imagina que el robot es una máquina de chicles 🍬:
def maquina_chicles(moneda1, moneda2):
    #Tú le das una moneda (los números 5 y 3).
    chicle = moneda1 + moneda2
    # La máquina hace crunch-crunch (suma 5+3).
    return chicle  # 🍬 ¡Aquí sale el chicle!
#¡Y luego escupe un chicle con el número 8! ESO ES EL "RETURN".

# ¡Usamos la máquina!
mi_chicle = maquina_chicles(5, 3) #aqui ponemos los valores
print(mi_chicle)  #  ¡Imprime 8!


#           ARGUMENTOS OPCIONALES
#Imagina que tienes una máquina de helados mágica 🍦🤖 que puede poner toppings extras... ¡pero solo si se los pides!
def hacer_helado(sabor, topping_extra=''):
    """Crea un helado delicioso, con topping extra si quieres."""
    if topping_extra:  # ¡Si escribiste un topping extra!
        helado = f"🍦 Helado de {sabor} con {topping_extra} ¡Yummy!"
    else:  # Si no pediste topping extra
        helado = f"🍦 Helado de {sabor} ¡Simple pero delicioso!"
    return helado
#Si solo quieres el helado básico (sin toppings extras):
helado1 = hacer_helado('vainilla')
print(helado1)  # 🍦 Helado de vainilla ¡Simple pero delicioso!
#Si quieres un helado con topping extra
helado2 = hacer_helado('chocolate', 'chispas de arcoíris')
print(helado2)  # 🍦 Helado de chocolate con chispas de arcoíris ¡Yummy!

#               DEVOLVER A UN DICCIONARIO 
#Una función puede devolver cualquier tipo de valor que necesitemos
# incluidas estructuras de datos más complejas, como listas y diccionarios

def crear_carta_magica(nombre, poder, elemento, nivel=1):
    # 🧙 Creamos un diccionario (como una carta mágica)
    carta = {
        "nombre": nombre,
        "poder": poder,
        "elemento": elemento,
        "nivel": nivel,
        "descripcion": f"⚡ {nombre} usa el poder {poder} del elemento {elemento}"
    }
    return carta  # 🤖✨ ¡La máquina te ENTREGA la carta completa!

# 🎯 Usamos la función
mi_carta = crear_carta_magica("Dragón de Fuego", "Llamarada", "Fuego 🔥", 5)
tu_carta = crear_carta_magica("Sirena Marina", "Canto", "Agua 💧")

print(mi_carta)
print(tu_carta)
#🧐 ¿Qué hace el return aquí?
# 1.- Recoge toda la información del personaje en un diccionario (como una ficha de juego)
# 2.- Te ENTREGA esa ficha completa para que puedas usarla después
# 3.- Sin el return, la función crearía la carta pero no te la daría 
# (¡sería como tener un juguete atrapado dentro de una máquina!)

# 🎪 ¡PODEMOS JUGAR CON LAS CARTAS!
# 🎲 Acceder a partes específicas de la carta
print(f"¡{mi_carta['nombre']} ataca con {mi_carta['poder']}!")  # ¡Dragón de Fuego ataca con Llamarada!

# 🎮 Comparar cartas
if mi_carta["nivel"] > tu_carta["nivel"]:
    print("¡Mi carta es más poderosa! 🏆")


#  FUNCION EN UN BUCLE WHILE
#Imagina que tenemos un juego de adivinanzas donde un mago 🧙‍♂️ tiene un número secreto y tú debes adivinarlo.
# El bucle while sigue repitiendo hasta que aciertes, y el return es cuando el mago grita "¡Correcto!" y te da tu premio.
def juego_adivinanza():
    numero_secreto = 4
    intentos = 0
    
    print("🎩 ¡Bienvenido al Juego del Mago Adivinador!")
    print("🔮 Estoy pensando en un número entre 1 y 10...")
    
    # 🔁 El bucle se repite HASTA que adivines el número
    while True:
        try:
            # 👦 Pedimos al usuario que adivine
            adivinanza = int(input("\n¿Cuál crees que es mi número mágico? "))
            intentos += 1
            
            # ✅ Verificamos si adivinó
            if adivinanza == numero_secreto:
                # 🎉 ¡RETURN MÁGICO! Rompe el bucle y devuelve el mensaje
                return f"✨ ¡CORRECTO! El número mágico era {numero_secreto}. ¡Te tomó {intentos} intentos!"
            
            # ❌ Si no adivinó, damos pista
            elif adivinanza < numero_secreto:
                print("⬆️ ¡Más alto! Sigue intentando...")
            else:
                print("⬇️ ¡Más bajo! Sigue intentando...")
                
        except ValueError:
            print("❌ ¡Oops! Debes ingresar un número, no letras.")

# 🎯 Iniciamos el juego
resultado = juego_adivinanza()
print(f"\n{resultado}")
print("🏆 ¡Eres un verdadero mago!")

#🧩 ¿CÓMO FUNCIONA EL BUCLE WHILE?
#El bucle while True: es como un hechizo repetitivo que:
# 1.- Se ejecuta una y otra vez (como un eco interminable)

# 2.- Solo se detiene cuando encuentra un return o un break
# 3.- En nuestro caso, el return actúa como rompehechizos 🪄

#🎯 ¿QUÉ HACE EL RETURN?
#El return tiene un doble poder mágico:
# 1.- ¡DETIENE EL BUCLE inmediatamente (como decir "¡Alto!")
# 2.- DEVUELVE EL RESULTADO (el mensaje de felicitación)