# ============================================
# 📘 NIVEL 1 - TEORÍA COMPLETA
# Variables y Tipos de Datos en Python
# ============================================

# 🔹 1. Qué es una variable
# Una variable es como una "cajita" donde podemos guardar un valor.
# En Python no es necesario declarar su tipo, se detecta automáticamente.

# Ejemplo:
nombre = "Ana"   # variable tipo cadena (str)
edad = 20        # variable tipo entero (int)
pi = 3.1416      # variable tipo decimal (float)

print(nombre)  # Ana
print(edad)    # 20
print(pi)      # 3.1416


# 🔹 2. Tipos de datos básicos

# 2.1 Enteros (int) → números sin decimales
numero = 10
print(numero)  # 10

# 2.2 Flotantes (float) → números con decimales
decimal = 3.5
print(decimal)  # 3.5

# 2.3 Cadenas de texto (str) → texto entre comillas
texto = "Hola Python"
print(texto)  # Hola Python

# 2.4 Booleanos (bool) → True o False
es_mayor = True
es_menor = False
print(es_mayor)  # True
print(es_menor)  # False


# 🔹 3. Operaciones básicas con variables

# Suma de enteros
a = 5
b = 3
print("Suma:", a + b)  # 8

# Resta de enteros
print("Resta:", a - b)  # 2

# Multiplicación
print("Multiplicación:", a * b)  # 15

# División
print("División:", a / b)  # 1.666...

# División entera
print("División entera:", a // b)  # 1

# Módulo (resto de la división)
print("Módulo:", a % b)  # 2

# Potencia
print("Potencia:", a ** b)  # 5^3 = 125


# 🔹 4. Operaciones con cadenas

# Concatenación → unir textos
nombre = "Ana"
saludo = "Hola " + nombre
print(saludo)  # Hola Ana

# Repetir cadenas
print("Python " * 3)  # Python Python Python

# Longitud de una cadena
texto = "Python"
print("Longitud:", len(texto))  # 6

# Acceder a caracteres de la cadena
print("Primer letra:", texto[0])  # P
print("Última letra:", texto[-1])  # n
print("Subcadena:", texto[1:4])  # yth


# 🔹 5. La función type()
# Sirve para saber el tipo de dato de una variable
x = 10
y = 3.5
z = "Hola"
b = True

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
print(type(b))  # <class 'bool'>


# 🔹 6. Conversión de tipos

# Convertir int → float
num1 = 5
print(float(num1))  # 5.0

# Convertir float → int
num2 = 3.8
print(int(num2))  # 3

# Convertir número a cadena
num3 = 100
print(str(num3) + " es un número")  # 100 es un número

# Convertir cadena a número
num4 = "50"
print(int(num4) + 10)  # 60


# 🔹 7. Entrada de datos con input()
# input() permite pedir datos al usuario
# siempre devuelve una cadena (str)

nombre_usuario = input("¿Cómo te llamas? ")
print("Hola", nombre_usuario)

# Si quieres un número, debes convertirlo
edad_usuario = int(input("¿Cuántos años tienes? "))
print("El próximo año tendrás:", edad_usuario + 1)


# 🔹 8. Buenas prácticas en variables

# - Usa nombres descriptivos: edad, nombre, total
# - Evita nombres reservados de Python: print, input, int
# - No uses espacios ni caracteres raros
# - Se sensible a mayúsculas y minúsculas
# Ejemplo:
total_compra = 150
TotalCompra = 200
print(total_compra, TotalCompra)  # Diferentes variables
