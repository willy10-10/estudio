# ============================================================
# 📝 TEMA 1: ENTRADA Y SALIDA DE USUARIO EN PYTHON
# ============================================================
# Este tema es la base de todo programa en Python.
# Un programa suele necesitar:
#   1. Mostrar información al usuario (SALIDA).
#   2. Recibir información del usuario (ENTRADA).
# Con esto ya podemos empezar a interactuar.
# ------------------------------------------------------------

# ============================================================
# 📌 1. FUNCIÓN print() → SALIDA DE DATOS
# ============================================================
# La función print() sirve para mostrar información en pantalla.
# Puede mostrar texto, números, resultados de operaciones, etc.

print("Hola, mundo")  # Muestra un mensaje de texto
print(2025)           # Muestra un número
print(5 + 3)          # Muestra el resultado de una operación
print("El resultado es:", 5 * 2)  # Mostrar texto + valor

# Podemos separar elementos con comas o unirlos con '+'
print("Python", "es", "genial")  # Separados por espacio
print("Python" + " es " + "genial")  # Concatenados

# También podemos usar el parámetro sep y end
print("A", "B", "C", sep="-")    # Cambia separador → A-B-C
print("Hola", end=" ")           # end evita salto de línea
print("mundo")                   # se junta con la anterior

# ------------------------------------------------------------

# ============================================================
# 📌 2. FUNCIÓN input() → ENTRADA DE DATOS
# ============================================================
# La función input() permite pedir datos al usuario.
# Siempre devuelve el valor como una CADENA (str).

nombre = input("¿Cómo te llamas? ")
print("Encantado de conocerte,", nombre)

# Ejemplo: pedir un número y mostrarlo
numero = input("Escribe un número: ")
print("El número ingresado es:", numero)

# OJO: input() devuelve texto, aunque escribas un número.
# Si quieres trabajar como número, debes convertirlo.

# ------------------------------------------------------------

# ============================================================
# 📌 3. CONVERSIÓN DE TIPOS DE DATOS
# ============================================================
# Usamos funciones de conversión:
#   int()   → convierte a entero
#   float() → convierte a decimal
#   str()   → convierte a texto

# Ejemplo: pedir dos números y sumarlos
num1 = int(input("Escribe un número entero: "))
num2 = int(input("Escribe otro número entero: "))
suma = num1 + num2
print("La suma es:", suma)

# Ejemplo con decimales
decimal = float(input("Escribe un número con decimales: "))
print("Has escrito:", decimal)

# Conversión inversa → número a cadena
edad = 20
print("Tengo " + str(edad) + " años")

# ------------------------------------------------------------

# ============================================================
# 📌 4. FORMATOS DE SALIDA
# ============================================================
# Existen varias formas de mostrar resultados:

# 1) Concatenación con +
nombre = "Ana"
edad = 25
print("Me llamo " + nombre + " y tengo " + str(edad) + " años.")

# 2) Separar con comas
print("Me llamo", nombre, "y tengo", edad, "años.")

# 3) Usar f-strings (recomendado desde Python 3.6)
print(f"Me llamo {nombre} y tengo {edad} años.")

# 4) Método format()
print("Me llamo {} y tengo {} años.".format(nombre, edad))

# ------------------------------------------------------------

# ============================================================
# 📌 5. ERRORES COMUNES EN ESTE TEMA
# ============================================================
# 1. Olvidar convertir con int() o float() al pedir números
#    Ejemplo incorrecto:
#    num = input("Número: ")
#    print(num + 5)   # ❌ Error, porque input() es texto
#
#    Solución:
#    num = int(input("Número: "))
#    print(num + 5)   # ✅ Ahora sí funciona
#
# 2. Concatenar números sin convertirlos a texto
#    edad = 18
#    print("Tengo " + edad + " años")   # ❌ Error
#
#    Solución:
#    print("Tengo " + str(edad) + " años")  # ✅

# ------------------------------------------------------------

# ============================================================
# 📌 6. RESUMEN DEL TEMA
# ============================================================
# - print() → muestra información
# - input() → pide datos al usuario (siempre como texto)
# - Conversión de tipos → int(), float(), str()
# - Formatos de salida → + , comas, f-strings, format()
# - Errores comunes → olvidar conversiones
# ============================================================

