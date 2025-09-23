#                           BANDERAS TRUE AND FALSE}
# Es una tecnica fundamental para controlar el flujo de ejecucion 
# actua como un interruptor

# Inicialización
bandera = True  # o False, dependiendo de la lógica

while bandera:
    # Código que se ejecuta mientras la bandera sea True
    
    # En algún punto, cambiamos la bandera basado en una condición
    if condicion_para_terminar:
        bandera = False  # Esto hará que el bucle se detenga
        

# Podemos usar varias para controlar diferentes aspectos, dependiendo la logica necesaria
#inicio de secion 
usuario_activo = True
tiene_intentos = True
intentos = 3 

while usuario_activo and tiene_intentos:
    respuesta = input("Ingresa la contraseña: ")
    
    if respuesta == "secreta":
        print("¡Acceso concedido!")
        usuario_activo = False  # Salimos del bucle
    else:
        intentos -= 1
        print(f"Contraseña incorrecta. Te quedan {intentos} intentos.")
        
        if intentos == 0:
            tiene_intentos = False  # Ya no tiene intentos
            print("Demasiados intentos fallidos.")

print("Fin del programa")

# Tambien podemos cronometrar el tiempo 
import time  # Importamos el módulo time para trabajar con funciones de tiempo

ejecutando = True  # Inicialización de la bandera
tiempo_inicio = time.time()  # Registramos el momento de inicio
tiempo_limite = 10  # segundos - Establecemos el límite de tiempo

while ejecutando:  # Bucle controlado por la bandera
    print("Ejecutando tarea...")
    time.sleep(1)  # Espera 1 segundo
    
    # Verificamos si ha pasado el tiempo límite
    if time.time() - tiempo_inicio > tiempo_limite:
        ejecutando = False  # Cambiamos la bandera para salir del bucle
        print("Tiempo límite alcanzado")


# Bandera para una validacion compleja
datos_validos = False
#Creamos una variable booleana llamada datos_validos y la inicializamos en False
#Esta bandera controlará el bucle: mientras sea False, el bucle continuará ejecutándose
while not datos_validos:
#El bucle se ejecutará mientras mientras los datos no sean válidos
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    
    # Múltiples condiciones para validar
    nombre_valido = len(nombre) > 0 and nombre.isalpha() 
    #Verifica que el nombre no esté vacío Y Verifica que el nombre contenga solo letras (sin números ni símbolos)
    edad_valida = edad.isdigit() and 0 < int(edad) < 120
    #Verifica que la edad sea un valor numérico Y Verifica que la edad esté en un rango razonable (entre 1 y 119)
    
    if nombre_valido and edad_valida:
        datos_validos = True  # Cambiamos la bandera
        print("¡Datos válidos!")
    else:
        print("Datos inválidos. Intenta nuevamente.")