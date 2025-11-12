#               GUARDAR FUNCIONES EN MODULOS
# Una de las ventajasd de las funciones es que puedes separarlas y usarlas en otros programas
# Podemos ir mas halla almacenando las funciones en  un "MODULO" 
# importando despues ese modulo al programa principál usando "IMPORT" 
# Esto nos permite concentrarnos en la logica del programa 


#               IMPORTAR UN MODULO COMPLETO 
# Un modulo es un archivo con extension ".py" ejemplo:

# todo esto lo guardamos en un archivo aparte "/pizza.py" 
# y llamamos a la funcion con "import"
import Pizza
#reiteramos cual funcion estamos llamando "Pizza."
Pizza.make_pizza(16, "pepperoni") 
Pizza.make_pizza(18, "mushrooms", "green peppers", "extra cheese")

# no vemos la copia de archivos porque el programa ya lo hace

#               IMPORTAR FUNCIONES ESPECIFICAS
#Para hacerlo usamos la siguiente sintaxis:  from nombre_módulo import nombre_función
# Podemos hacerlo tantas veces como queramos
from Pizza import make_pizza
make_pizza(16, "pepperoni") 
make_pizza(18, "mushrooms", "green peppers", "extra cheese")

#               PONER APODOS O ALIAS A LAS FUNCIONES 
# Aveces las funciones tienen nombres largos y complicados, asi que mejor ponemos un apodo
# Es sencillo solo tenemos que aumentar el "as"
from Pizza import make_pizza as mp #ponemos el apodo de "mp"
mp(16, "pepperoni")
mp(18, "mushrooms", "green peppers", "extra cheese")

#               PONER APODODOS O ALIAS A MODULOS
# De la misma forma podemos hacerlo con los modulos
import Pizza as p #Ponemos el apodo "p" a Pizza
p.mp(16, "pepperoni")
p.mp((18, "mushrooms", "green peppers", "extra cheese"))

#           IMPORTAR TODAS LAS FUNCIONES DE UN MODULO
#Paraa hacerlo soloponemos el asterisco "*"
from Pizza import *
make_pizza(16, "pepperoni")
make_pizza(18, "mushrooms", "green peppers", "extra cheese")

