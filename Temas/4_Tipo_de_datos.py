# 📚 APUNTES: TIPOS DE DATOS EN PYTHON
# ------------------------------------

# 1. 🟢 TIPOS BÁSICOS (INMUTABLES)
# --------------------------------

# Enteros (int)
numero_entero = 42
otro_entero = -10

# Flotantes (float)
pi = 3.1416
temperatura = -20.5

# Texto (str) 📝
saludo = "Hola Mundo"
nombre = 'Ana'
multilinea = """Esto es un texto multilínea"""

# Booleanos (bool) ✅❌
es_verdadero = True
es_falso = False

# NoneType (None) ⚫
valor_nulo = None

# 2. 🧮 COLECCIONES (MUTABLES)
# ----------------------------

# Listas (list) 📋
lista_frutas = ["manzana", "banana", "naranja"]
lista_mixta = [1, "hola", 3.14, True]

# Tuplas (tuple) 📦
coordenadas = (10, 20)
colores_rgb = (255, 128, 0)

# Diccionarios (dict) 📖
estudiante = {
    "nombre": "Carlos",
    "edad": 25,
    "cursos": ["Python", "Matemáticas"]
}

# Conjuntos (set) 🔄
numeros_primos = {2, 3, 5, 7, 11}
vocales = {'a', 'e', 'i', 'o', 'u'}

# 3. 🔧 FUNCIONES ÚTILES PARA TIPOS
# ----------------------------------

# type() - Verificar tipo
type(10)           # <class 'int'>
type("Hola")       # <class 'str'>

# Conversión entre tipos
int("100")         # Convierte a entero
str(3.14)          # Convierte a texto
list((1, 2, 3))    # Convierte tupla a lista

# 4. 💡 DATOS CURIOSOS
# --------------------

# Los strings son inmutables:
texto = "Python"
# texto[0] = "J"  # ❌ Esto daría error

# Las listas son mutables:
lista = [1, 2, 3]
lista[0] = 99     # ✅ Esto funciona

# Los diccionarios usan llaves únicas:
diccionario = {"a": 1, "b": 2}
diccionario["a"] = 100  # Actualiza valor

# 5. 🧪 EJEMPLOS PRÁCTICOS
# -------------------------

# Verificar tipo
def verificar_tipo(dato):
    print(f"🔍 El dato {dato} es de tipo: {type(dato).__name__}")

# Ejemplo de uso
verificar_tipo(10)
verificar_tipo("Hola Pythonistas!")

# ✨💻 ¡Recuerda practicar con cada tipo de dato!
# Guarda este archivo como 'tipos_datos.py' y ejecútalo para ver los resultados.