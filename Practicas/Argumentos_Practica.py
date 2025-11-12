#                       SANDWICHES
def sandwich(*ingredientes):
    """Crea un sandwich"""
    print("\nPreparando un Sandwich con:")
    for ingrediente in ingredientes:
        print(f"- {ingrediente.title()}")
sandwich("mayonesa","mortadela")
sandwich("mortadela","tomate", "cebolla")
sandwich("pollo","mayonesa", "mostaza", "ensalada")


#                   MI PERFIL
def crear_mi_perfil(nombre, apellido,**info):
    """Crear mi propio perfil"""
    info["nombre"] = nombre
    info["apellido"] = apellido
    return info

perfil_de_usuario = crear_mi_perfil("eliu", "villanueva",
                                    ciudad = "cochabamba",
                                    edad = 26)
print(perfil_de_usuario)


#           PERFIL DE AUTO
def crear_un_auto(fabrica, modelo,**caracteristicas):
    """Crear mi propio perfil"""
    caracteristicas["fabrica"] = fabrica
    caracteristicas["modelo"] = modelo
    return caracteristicas

perfil_del_auto = crear_un_auto("subaru", "outblack",
                                    color = "azul",
                                    seguro = True)
print(perfil_del_auto)