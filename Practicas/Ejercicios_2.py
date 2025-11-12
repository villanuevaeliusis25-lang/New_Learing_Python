#                   CALCULADORA BASICA
# operacion puede ser: "suma", "resta", "multiplicacion", "division"
# Devuelve el resultado o "Error" si la división es por cero
def calculadora(a, b, operacion):
    """lA CONCHA DE LA LORA"""
    operacion = operacion.lower()
    resultado = 0
    if operacion == "suma":
        resultado = a + b
        return resultado
    elif operacion == "resta":
        resultado = a - b
        return resultado
    elif operacion == "multiplicacion":
        resultado= a * b
        return resultado
    elif operacion == "division":
        if b == 0:
            return "No se puede dividir entre 0"
        else:
            resultado = a / b
            return resultado
    else:
        print("Dale gordo estoy aprendiendo")
    pass

# Pruebas:
print(calculadora(10, 5, "suma"))           # Debería devolver 15
print(calculadora(10, 5, "resta"))          # Debería devolver 5
print(calculadora(10, 5, "multiplicacion")) # Debería devolver 50
print(calculadora(10, 5, "division"))       # Debería devolver 2.0
print(calculadora(10, 0, "division"))       # Debería devolver "Error"


#               GESTOR DE NOTAS
# estudiantes es un diccionario: {"nombre": [nota1, nota2, ...]}
# Devuelve un diccionario con:
# - Promedio de cada estudiante
# - Mejor promedio del grupo
# - Estudiantes con promedio mayor a 3.0 (aprobados)

def gestionar_notas(estudiantes):
    promedios_individuales = {}
    
    # Paso 1: Calcular promedios
    for nombre, notas in estudiantes.items():
        promedio = sum(notas) / len(notas)
        promedios_individuales[nombre] = round(promedio, 2)
    
    # Paso 2: Encontrar mejor promedio
    mejor_promedio = max(promedios_individuales.values())
    
    # Paso 3: Encontrar aprobados
    aprobados = []
    for nombre, promedio in promedios_individuales.items():
        if promedio > 3.0:
            aprobados.append(nombre)
    
    # Paso 4: Mostrar resultados con print()
    print("=== RESULTADOS ===")
    print("Promedios individuales:")
    for nombre, promedio in promedios_individuales.items():
        print(f"  {nombre}: {promedio}")
    
    print(f"\nMejor promedio del grupo: {mejor_promedio}")
    print(f"Estudiantes aprobados: {', '.join(aprobados)}")

# Probamos
estudiantes_ejemplo = {
    "Ana": [4.5, 3.0, 2.5],
    "Luis": [2.0, 3.5, 4.0],
    "Maria": [5.0, 4.5, 4.0]
}

gestionar_notas(estudiantes_ejemplo)