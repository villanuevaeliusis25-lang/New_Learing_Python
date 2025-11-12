#                       SENTENCIAS IF 🔍

# Examina condiciones y ejecuta código cuando una condición se evalúa como VERDADERA (True)

print("🎮 EJEMPLO 1: Diferenciando marcas de autos")
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':  # Si la variable car es igual a 'bmw'
        print(car.upper())  # 🚗 BMW en mayúsculas
    else:  # Si NO se cumple la condición del if
        print(car.title())  # 🚙 Otras marcas en formato título
# else no es obligatorio, pero if sí lo es

#                       CONDICIONALES SIMPLES ⚡
print("\n" + "="*40)
print("CONDICIONALES SIMPLES")
print("="*40)

# Verifica si una condición es True y ejecuta código si lo es
# O si es False, no hace nada (o ejecuta el else si existe)

car = 'bmw'
print(f"¿car == 'bmw'? {car == 'bmw'}")  # ✅ True
print(f"¿car != 'audi'? {car != 'audi'}")  # ✅ True (!= significa "no es igual a")

# ⚠️ IMPORTANTE: Python es CASE-SENSITIVE (distingue mayúsculas/minúsculas)
print(f"¿car == 'BMW'? {car == 'BMW'}")  # ❌ False
print(f"¿car.lower() == 'bmw'? {car.lower() == 'bmw'}")  # ✅ True (convertimos a minúsculas)

#                       COMPARACIONES MATEMÁTICAS 🔢
print("\n" + "="*40)
print("COMPARACIONES MATEMÁTICAS")
print("="*40)

age = 18
print(f"age = {age}")
print(f"age < 21: {age < 21}")   # menor que ✅
print(f"age <= 18: {age <= 18}") # menor o igual que ✅
print(f"age > 21: {age > 21}")   # mayor que ❌
print(f"age >= 16: {age >= 16}") # mayor o igual que ✅

#                       OPERADORES LÓGICOS: AND y OR 🔗
print("\n" + "="*40)
print("OPERADORES LÓGICOS")
print("="*40)

age_0 = 22
age_1 = 18
print(f"Edades: {age_0} y {age_1}")

# AND: ambas condiciones deben ser True
print(f"¿Ambos >= 21? {age_0 >= 21 and age_1 >= 21}")  # ❌ False (18 < 21)

# OR: al menos una condición debe ser True  
print(f"¿Al menos uno >= 21? {age_0 >= 21 or age_1 >= 21}")  # ✅ True (22 >= 21)

#                       COMPROBAR ELEMENTOS EN LISTAS 📋
print("\n" + "="*40)
print("COMPROBANDO ELEMENTOS EN LISTAS")
print("="*40)

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
print(f"Toppings disponibles: {requested_toppings}")

print(f"¿'mushrooms' está en la lista? {'mushrooms' in requested_toppings}")  # ✅ True
print(f"¿'pepperoni' está en la lista? {'pepperoni' in requested_toppings}")  # ❌ False

# También existe "not in" (no está en)
print(f"¿'pepperoni' NO está en la lista? {'pepperoni' not in requested_toppings}")  # ✅ True
print(f"¿'mushrooms' NO está en la lista? {'mushrooms' not in requested_toppings}")  # ❌ False

#                       CADENAS IF-ELIF-ELSE 🎯
print("\n" + "="*40)
print("IF-ELIF-ELSE")
print("="*40)

age = 12
print(f"Edad del cliente: {age}")

if age < 4:
    price = 0  # 🆓 Entrada gratis para menores de 4
    print("¡Entrada GRATIS!")
elif age < 18:  # ELIF = "else if"
    price = 5   # 💰 Precio reducido para menores
    print("Precio reducido: $5")
elif age < 65:
    price = 10  # 💵 Precio normal
    print("Precio normal: $10")
else:
    price = 7   # 👵 Precio para adultos mayores
    print("Precio para adultos mayores: $7")

print(f"Total a pagar: ${price}")

#                       MÚLTIPLES CONDICIONES INDEPENDIENTES 🍕
print("\n" + "="*40)
print("MÚLTIPLES CONDICIONES INDEPENDIENTES")
print("="*40)

requested_toppings = ["mushrooms", "extra cheese"]
print(f"Toppings solicitados: {requested_toppings}")

# Usamos if separados cuando son condiciones independientes
if "mushrooms" in requested_toppings:
    print("🍄 Adding mushrooms...")
if "pepperoni" in requested_toppings:
    print("🍕 Adding pepperoni...")
if "extra cheese" in requested_toppings:
    print("🧀 Adding extra cheese...")

print("\n¡Tu pizza está lista! 🎉")

#                       IF CON LISTAS 🔄
print("\n" + "="*40)
print("IF CON LISTAS")
print("="*40)

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]
print(f"Preparando pizza con: {requested_toppings}")

for topping in requested_toppings:
    if topping == "green peppers":  # ⚠️ Nos quedamos sin pimientos
        print("❌ Sorry, we are out of green peppers right now.")
    else:
        print(f"✅ Adding {topping}.")

print("\n¡Pizza terminada! 🍕")

#                       VERIFICAR LISTAS VACÍAS 📭
print("\n" + "="*40)
print("VERIFICANDO LISTAS VACÍAS")
print("="*40)

requested_toppings = []  # Lista vacía

if requested_toppings:  # ✅ Si la lista NO está vacía (evalúa como True)
    for topping in requested_toppings:
        print(f"Adding {topping}.")
    print("\n¡Pizza terminada!")
else:  # ❌ Si la lista está vacía (evalúa como False)
    print("🤔 Are you sure you want a plain pizza?")
    print("(No toppings selected)")

#                       MÚLTIPLES LISTAS 📋📋
print("\n" + "="*40)
print("TRABAJANDO CON MÚLTIPLES LISTAS")
print("="*40)

available_toppings = ["mushrooms", "olives", "green peppers", 
                     "pepperoni", "pineapple", "extra cheese"]
requested_toppings = ["mushrooms", "french fries", "extra cheese"]

print(f"🏪 Toppings disponibles: {available_toppings}")
print(f"👤 Toppings solicitados: {requested_toppings}")

print("\n🔄 Procesando tu orden...")
for topping in requested_toppings:
    if topping in available_toppings:
        print(f"✅ Adding {topping}")
    else:
        print(f"❌ Sorry, we don't have {topping}")

print("\n🎉 ¡Finished making your pizza!")

#                       EXTRAS: TERNARY OPERATOR ✨
print("\n" + "="*40)
print("OPERADOR TERNARIO (IF en una línea)")
print("="*40)

age = 20
status = "adult" if age >= 18 else "minor"
print(f"Age: {age} -> Status: {status}")

# Múltiples condiciones en una línea
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "F"
print(f"Score: {score} -> Grade: {grade}")

print("\n" + "🎊" * 20)
print("¡Dominaste las sentencias IF! 🚀")
print("🎊" * 20)