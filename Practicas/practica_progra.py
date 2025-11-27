def imc(peso, altura):
    imc  = peso / (altura**2)
    if imc >= 40:
        estado = "Obesidad III"
    elif imc >=35:
        estado = "Obesidad II"
    elif imc >= 30:
        estado = "Obesidad I"
    elif imc >= 25:
        estado = "Sobre peso"
    elif imc >= 18.5:
        estado = "Normal"
    else:
        estado = "Bajo peso"
    return print(f"Tu estado es: {estado}")
peso = float(input("Introduzca su peso: "))
altura = float(input("Introduzca su altura: "))
imc(peso, altura)