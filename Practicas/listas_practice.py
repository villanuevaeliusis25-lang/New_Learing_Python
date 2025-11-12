#                               BUCLE FOR
caracters = ["mario", "luigi", "peach", "bowser"]
for caracter in caracters:
    print(f"{caracter.title()}")
    print("Es un personaje jugable\n")
print("Escoge a tu favorito!")

#                               RANGE()
numbers =[ value for value in range(1,21)]
print(numbers)
#masximos, minimos y suma
min(numbers)
max(numbers)
sum(numbers)
print(f"El valor minimo es {min(numbers)}")
print(f"El valor maximo es {max(numbers)}")
print(f"La suma de todos los valores es {sum(numbers)}")
#impares
impars = [ impar for impar in range(1,21,2)]
print(f"los numeros impaser son: {impars}")
#multiplo de 3
multiple_of_3 = [multi*3 for multi in range(1,11)]
print(f"los multiplos del 3 son: {multiple_of_3}")

#                           COPIAR Y PARTIR LISTAS
songs = ["ditto", "cool with yoy", "gabriela", "narly", "lovesick girls", "pink venom"]
print("         MIS CANCIONES FAVORITAS")
print("Los 3 primeros son:")
for song in songs[:3]:
    print(song.title())
print("Los 3 del medio son:")
for song in songs[2:5]:
    print(song.title())
print("Los 3 ultimos son:")
for song in songs[-3:]:
    print(song.title())
#copia de listas
blackpink_songs = songs[-2:]
newjeanz_songs = songs[:2]
blackpink_songs.append("shut down")
newjeanz_songs.append("super shy")
print("Canciones de blackink:")
print(blackpink_songs)
print("Canciones de newjeanz:")
print(newjeanz_songs)

#                               TUPLAS
fods  = ("sushi", "ramen", "tacos", "pizza", "hamburguesa")
for fod in fods:
    print(f"{fod.title()} es delicioso")
print("el restaurante se reinventa y cambia el menu")
fods = ("spagetti", "ensalada", "paella", "charke", "milanesa")
for fod in fods:
    print(f"{fod.title()} new!")
