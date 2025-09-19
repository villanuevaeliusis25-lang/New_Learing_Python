# Adivina la palabra
def adivina_palabra():
    import random

    # Lista de palabras para el juego. ¡Puedes añadir más!
    palabras = ["python", "programacion", "desarrollo", "computadora", "teclado", "gemini"]
    palabra_secreta = random.choice(palabras).lower()
    
    intentos = 5
    letras_adivinadas = []
    
    print("¡Bienvenido al juego de Adivina la Palabra!")
    print("El objetivo es adivinar la palabra oculta.")
    print(f"Tienes {intentos} intentos para adivinar letras incorrectas.")
    print(f"La palabra tiene {len(palabra_secreta)} letras.")

    # El bucle principal del juego
    while intentos > 0:
        # Muestra el estado actual de la palabra (con guiones bajos)
        palabra_mostrada = ""
        letras_faltantes = 0
        for letra in palabra_secreta:
            if letra in letras_adivinadas:
                palabra_mostrada += letra + " "
            else:
                palabra_mostrada += "_ "
                letras_faltantes += 1
        
        print(f"\nPalabra: {palabra_mostrada}")
        
        # Si no quedan letras por adivinar, el jugador gana
        if letras_faltantes == 0:
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            print(f"La palabra era: {palabra_secreta.title()}")
            break

        print(f"Te quedan {intentos} intentos.")
        print(f"Letras ya usadas: {', '.join(sorted(letras_adivinadas))}")

        # Pide al usuario que introduzca una letra
        letra_usuario = input("Introduce una letra: ").lower()

        # Validaciones de la entrada
        if len(letra_usuario) != 1 or not letra_usuario.isalpha():
            print("Entrada no válida. Por favor, introduce una única letra.")
            continue
        if letra_usuario in letras_adivinadas:
            print("Ya has intentado con esa letra. ¡Prueba con otra!")
            continue

        letras_adivinadas.append(letra_usuario)

        # Comprueba si la letra está en la palabra y actualiza los intentos si no lo está
        if letra_usuario in palabra_secreta:
            print(f"¡Bien! La letra '{letra_usuario}' está en la palabra.")
        else:
            print(f"Lo siento, la letra '{letra_usuario}' no está. Pierdes un intento.")
            intentos -= 1

    # Si se acaban los intentos, el jugador pierde
    if intentos == 0 and letras_faltantes > 0:
        print("\n¡Te has quedado sin intentos!")
        print(f"La palabra secreta era: '{palabra_secreta.title()}'.")

# Inicia el juego
while True:
    adivina_palabra()
    
    jugar_de_nuevo = input("\n¿Quieres jugar de nuevo? (si/no): ").lower()
    if jugar_de_nuevo != "si":
        print("¡Gracias por jugar! ¡Hasta pronto!")
        break