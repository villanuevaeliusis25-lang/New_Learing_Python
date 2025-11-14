# Ejercicio "CONTRASEÑA SEGURA"

def contraseña (contra):
    if len(contra) < 8:
        return False
    tiene_may = False
    tiene_num = False
    for c in contra:
        if c.isupper():
            tiene_may = True
        if c.isdigit():
            tiene_num = True
    return tiene_may and tiene_num
contra = input("Ingrese una contraseña")
if contraseña(contra):
    print("La contraseña es segura")
else:
    print("La contraseña no es segura")

# Con MATCH
match contraseña(contra):
    case True:
        print("La contraseña es segura")
    case False:
        print("La contraseña no es segura")
        
# Ejercicio "CONTAR PALABRAS"
def contar_palabras(frase):
    palabras = frase.split()
    return len(palabras)

frase = input("Ingrese un texto: ")
print(f"Palabras ene el texto: {contar_palabras(frase)}")

# Ejericio "MULTIPLOS DE "
def multiplos(num1, num2):
    if num1 or num2 == 0:
        return False
    return num1 % num2
a = int(input("Ingrese el primer numero"))
b = int(input("Ingrese el segundo numero"))
if multiplos(a, b) or multiplos(b, a):
    print(f"{a} y {b} son multiplos")
else:
    print(f"{a} y {b}  no  son multiplos")
    
# Ejercicio "CALCULADORA"
def suma(num1, num2):
    return num1 + num2
def resta(num1, num2):
    return num1 - num2
def multiplicacion(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "No se puede dividir"
    return num1 / num2

def calculadora():
    print("---------CALCULADORA---------")
    print("1.Suma")
    print("2.Resta")
    print("3.Multiplicacion")
    print("4.Division")
    opcion = int(input("Elige una opcion"))
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    match opcion:
        case 1:
            resultado = suma(a,b)
        case 2:
            resultado = resta(a,b)
        case 3:
            resultado = multiplicacion(a,b)
        case 4:
            resultado = division(a,b)
        case _:
            print("Opcion Invalida")
    print(f"El resultado es: {resultado}")