#                               BUCLES 
# Estructuras de control que permiten repetir un bloque de código varias veces
newjeanz = ["minji", "haerin", "hanni", "danielle", "hanni"]
#"for" toma un elemento de la lista y lo asigna a una variable temporal "member"
for newjean in newjeanz: 
    #los ":" le indican a Python que interprete la siguiente línea como el inicio de un bucle
    print(f"{newjean.title()} te extrañamos mucho <3")
# se repite el bloque de código para cada elemento de la lista
# es recomendable usar nombres diferentes para la variable temporal y la lista

#podemos crear una lista vacia tras cada ciclo con"\n"
print("Gracias por todo lo que hacen por nosotros <3")
for newjean in newjeanz:
    print(f"{newjean.title()} te extrañamos mucho <3")
    print(F"se fuerte {newjean.title()}!\n")
print("NewJeanz never die <3")

#NO OLVIDES que las sangrias son importantes en python
# el bloque de código dentro del bucle for debe estar indentado
# el bloque de código fuera del bucle for no debe estar indentado

#                       RANGE()
for value in range(1,6): # el segundo valor es exclusivo
    print(value)
#aunque deberia imprimir el 6, nunca contiene el valor final

#si queremos incluir los numeros a una lista usamos list()
numbers = list(range(1,6))
print(numbers)
# tambien podemos especificar un incremento
even_numbers = list(range(2,11,2)) # empieza en 2, termina en 10, incrementa de 2 en 2
print(even_numbers)
#podemos elevar estos numeros al cuadrado
squares = []
for value in range(1,11):
    squares.append(value**2) # append() agrega un elemento al final de la lista
print(squares)
#podemos usar min(), max() y sum() con listas de numeros par identificar
# el valor minimo, maximo y la suma de todos los elementos

#                       PARTIR LISTAS O SLICES
# podemos obtener una parte de la lista especificando un rango de indices
blackpink = ["jennie", "jisoo", "rose", "lisa"]
print(f"Miembros coreanas: {blackpink[0:2]}") # imprime desde el indice 0 hasta el 2 (exclusivo)
#si queremos que empiece desde otro indice
print(f"Miembros extranjeras: {blackpink[2:]}") # imprime desde el indice 2 hasta el final
#si queremos que imprima el final, aunque aumente la lista siempre sera el ultimo
print(f"favorita: {blackpink[-1:]}") # imprime el ultimo elemento de la lista

#                           COPIAR LISTAS
# para copiar una lista usamos el slice completo [:]
Byas_groups = blackpink[-1:] # crea una copia de la lista blackpink
# para añadir elementos a la nueva lista usamos append()
Byas_groups.append("danielle")
print(f"mis bias son: {Byas_groups}") 

#                                TUPLAS
# Son inmutables,*no se pueden modificar* una vez creadas.
# Se definen con paréntesis () y los elementos se separan por comas.
tuplas = (1, 2, 3, 4, 5)
print(tuplas)
#tambien podemos usar la función "for" para recorrer los elementos de una tupla
for elemento in tuplas:
    print(elemento)
#aunque no podamos modificar una tupla, si podemos reasignar una nueva tupla a la misma variable
print("duplas originales: ")
print(f"{tuplas}\n")
print("Reasignando una nueva tupla a la variable 'tuplas'")
tuplas = (6, 7, 8, 9, 10)
print(f"{tuplas}")