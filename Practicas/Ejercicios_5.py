#                   ANALIZADOR DE NOTAS
# A naliza una lista de notas y devuelve un reporte completo
# Promedio, Aprobados, Reprobados, Mejor Nota, Peor Nota
def analizar_notas(notas):
    aprobado = 0
    reprobado = 0
    mejor_nota = notas[0]
    peor_nota = notas[0]
    promedio = 0
    #Sumamos todas notas
    for nota in notas:
        promedio = promedio + nota
    # Dividimos los aprobados y los reprobados
        if nota >= 6:
            aprobado += 1
        else:
            reprobado += 1
    #Buscamos la mejor y peor nota
        if nota > mejor_nota:
            mejor_nota = nota
        elif nota < peor_nota:
            peor_nota = nota
    #sacamos el promedio de las notas
    promedio = promedio / len(notas)
    
    return {
        "promedio": promedio,
        "aprobados": aprobado,
        "reprobados": reprobado,
        "Mejor nota": mejor_nota,
        "Peor nota": peor_nota
    }

print(analizar_notas([7, 5, 8, 6, 9, 4]))
print(analizar_notas([10, 8, 9, 7]))
print(analizar_notas([4, 3, 5]))

# CONTADOR CON WHILE 
# Cuenta desde 1 hasta el limite 
# Devuelve la suma total de los numeros
def contador_while(limite):
    i = 1
    contador = []
    suma = 0
    while i <= limite:
        contador.append(i)
        i = i + 1
    for dato in contador: 
        suma = suma + dato
    resultado = '+'.join(map(str, contador))
    return f"({resultado}) \nLa suma total es {suma}"
# Pruebas:
print(contador_while(5))   # 15 (1+2+3+4+5)
print(contador_while(10))  # 55
