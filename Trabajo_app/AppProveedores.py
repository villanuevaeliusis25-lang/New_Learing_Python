#   BASES DE DATOS
proveedores = {}            # {id: {"nombre":..., "categoria":..., "productos":[...], "reseñas":[...]}}
pagos_registrados = []      # lista de pagos realizados por usuarios
#   FUNCIONES
def registrar_proveedor():
    id_prov = len(proveedores) + 1
    nombre = input("Nombre del proveedor: ")
    categoria = input("Categoría (alimentos/ropa/servicios/etc): ")
    proveedores[id_prov] = {
        "nombre": nombre,
        "categoria": categoria,
        "productos": [],
        "reseñas": []
    }
    print(f"Proveedor '{nombre}' registrado con ID {id_prov}.\n")

def agregar_producto():
    if len(proveedores) == 0:
        print("No hay proveedores registrados.\n")
        return
    
    id_prov = input("ID del proveedor: ")

    if not id_prov.isdigit():
        print("El ID debe ser un número.\n")
        return

    id_prov = int(id_prov)

    if id_prov not in proveedores:
        print("Proveedor no encontrado.\n")
        return

    nombre_prod = input("Nombre del producto: ")
    precio = input("Precio del producto: ")

    if precio.replace(".", "", 1).isdigit():
        precio = float(precio)
    else:
        print("El precio debe ser numérico.\n")
        return

    producto = {"nombre": nombre_prod, "precio": precio}
    proveedores[id_prov]["productos"].append(producto)

    print(f"Producto '{nombre_prod}' agregado con éxito.\n")

def ver_proveedores():
    if len(proveedores) == 0:
        print("No hay proveedores.\n")
        return
    print("\n=== LISTA DE PROVEEDORES ===")
    for pid, data in proveedores.items():
        print(f"{pid}. {data['nombre']} | Categoría: {data['categoria']} | Productos: {len(data['productos'])}")
    print()

def ver_productos():
    id_prov = input("ID del proveedor: ")

    if not id_prov.isdigit():
        print("Debe ingresar un número.\n")
        return
    id_prov = int(id_prov)
    if id_prov not in proveedores:
        print("Proveedor no existe.\n")
        return
    prov = proveedores[id_prov]
    print(f"\nProductos de {prov['nombre']}:")

    if len(prov["productos"]) == 0:
        print("No tiene productos registrados.\n")
        return
    for i, p in enumerate(prov["productos"], 1):
        print(f"{i}. {p['nombre']} - ${p['precio']}")
    print()
def registrar_pago():
    id_prov = input("ID del proveedor: ")

    if not id_prov.isdigit():
        print("Ingrese solo números.\n")
        return
    id_prov = int(id_prov)

    if id_prov not in proveedores:
        print("Proveedor no encontrado.\n")
        return

    monto = input("Monto del pago: ")

    if not monto.replace(".", "", 1).isdigit():
        print("El monto debe ser número.\n")
        return

    monto = float(monto)
    usuario = input("Nombre del usuario: ")

    pago = {"usuario": usuario, "proveedor_id": id_prov, "monto": monto}
    pagos_registrados.append(pago)

    print("Pago registrado correctamente.\n")

def dejar_reseña():
    id_prov = input("ID del proveedor: ")

    if not id_prov.isdigit():
        print("Debe ingresar un número.\n")
        return

    id_prov = int(id_prov)

    if id_prov not in proveedores:
        print("Proveedor no existe.\n")
        return

    usuario = input("Tu nombre: ")
    comentario = input("Comentario: ")
    calificacion = input("Calificación (1-5): ")

    if not calificacion.isdigit():
        print("La calificación debe ser un número.\n")
        return

    calificacion = int(calificacion)

    if calificacion < 1 or calificacion > 5:
        print("La calificación debe ser entre 1 y 5.\n")
        return

    reseña = {"usuario": usuario, "comentario": comentario, "calificacion": calificacion}
    proveedores[id_prov]["reseñas"].append(reseña)

    print("Reseña registrada.\n")


def ver_reseñas():
    id_prov = input("ID del proveedor: ")

    if not id_prov.isdigit():
        print("Debe ingresar un número.\n")
        return

    id_prov = int(id_prov)

    if id_prov not in proveedores:
        print("Proveedor no existe.\n")
        return

    prov = proveedores[id_prov]
    print(f"\nReseñas de {prov['nombre']}:")

    if len(prov["reseñas"]) == 0:
        print("No tiene reseñas.\n")
        return

    for r in prov["reseñas"]:
        print(f"- {r['usuario']}: {r['comentario']} (⭐ {r['calificacion']})")
    print()


def resumen():
    print("\n=== RESUMEN GENERAL ===")
    print("Proveedores registrados:", len(proveedores))
    total_prod = 0
    for p in proveedores.values():
        total_prod += len(p["productos"])
    print("Productos totales:", total_prod)
    print("Pagos registrados:", len(pagos_registrados))
    print()

#   MENÚ PRINCIPAL (match-case)
def menu():
    while True:
        print("===== PLATAFORMA DIGITAL DE PROVEEDORES =====")
        print("1. Registrar proveedor")
        print("2. Agregar producto")
        print("3. Ver proveedores")
        print("4. Ver productos de proveedor")
        print("5. Registrar pago")
        print("6. Agregar reseña")
        print("7. Ver reseñas")
        print("8. Resumen general")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1": registrar_proveedor()
            case "2": agregar_producto()
            case "3": ver_proveedores()
            case "4": ver_productos()
            case "5": registrar_pago()
            case "6": dejar_reseña()
            case "7": ver_reseñas()
            case "8": resumen()
            case "9":
                print("Saliendo del sistema...")
                break
            case _:
                print("Opción inválida\n")


menu()
