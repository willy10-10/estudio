# ============================================================
# 📘 TEMA 2: EXPRESIONES, OPERACIONES Y OPERADORES LÓGICOS
# ============================================================

# 🔹 1. ¿Qué es una expresión?
# Una expresión en Python es cualquier combinación de valores,
# variables, operadores y llamadas a funciones que se puede evaluar
# y produce un resultado.
# Ejemplo:
x = 5
y = 3
resultado = x + y   # Esto es una expresión: 5 + 3 = 8
print("Resultado de la expresión:", resultado)


# 🔹 2. Operadores aritméticos
# Se usan para realizar operaciones matemáticas básicas.

#   +   suma
#   -   resta
#   *   multiplicación
#   /   división (resultado flotante)
#   //  división entera (sin decimales)
#   %   módulo (residuo de la división)
#   **  potencia

a = 10
b = 3
print("Suma:", a + b)        # 13
print("Resta:", a - b)       # 7
print("Multiplicación:", a * b)  # 30
print("División:", a / b)    # 3.333...
print("División entera:", a // b)  # 3
print("Módulo:", a % b)      # 1
print("Potencia:", a ** b)   # 1000


# 🔹 3. Operadores de comparación
# Comparan dos valores y devuelven un resultado booleano (True o False).
#   ==  igual a
#   !=  diferente de
#   >   mayor que
#   <   menor que
#   >=  mayor o igual que
#   <=  menor o igual que

print("¿a == b?", a == b)   # False
print("¿a != b?", a != b)   # True
print("¿a > b?", a > b)     # True
print("¿a < b?", a < b)     # False
print("¿a >= b?", a >= b)   # True
print("¿a <= b?", a <= b)   # False


# 🔹 4. Operadores lógicos
# Se usan para combinar condiciones lógicas (booleanas).
#   and  → devuelve True si ambas condiciones son verdaderas.
#   or   → devuelve True si al menos una condición es verdadera.
#   not  → invierte el valor lógico (True → False, False → True).

edad = 20
es_estudiante = True

print("¿Edad mayor a 18 y estudiante?", edad > 18 and es_estudiante)   # True
print("¿Edad menor a 18 o estudiante?", edad < 18 or es_estudiante)    # True
print("¿No es estudiante?", not es_estudiante)                         # False


# 🔹 5. Precedencia de operadores
# Es el orden en que Python evalúa las operaciones.
# De mayor a menor prioridad:
#   1. **   (potencia)
#   2. *, /, //, %   (multiplicación y divisiones)
#   3. +, -          (suma y resta)
#   4. Comparaciones (==, !=, >, <, >=, <=)
#   5. not
#   6. and
#   7. or

expr = 3 + 2 * 5   # Multiplicación primero: 2*5=10 → 3+10=13
print("Resultado de precedencia:", expr)

expr2 = (3 + 2) * 5  # Paréntesis cambia el orden: (3+2)=5 → 5*5=25
print("Con paréntesis:", expr2)


# 🔹 6. Conversión de tipos en expresiones
# A veces necesitamos transformar tipos para operar correctamente.
# int() → convierte a entero
# float() → convierte a decimal
# str() → convierte a texto
# bool() → convierte a True o False

numero = "15"      # tipo string
print("Número como string:", numero)
print("Número como entero:", int(numero) + 5)   # 20

decimal = 7.8
print("Número decimal:", decimal)
print("Convertido a entero:", int(decimal))  # 7 (trunca, no redondea)

texto = str(100)
print("Número convertido a texto:", texto, "→ tipo:", type(texto))


# 🔹 7. Mini ejemplos prácticos

# Ejemplo 1: calcular área de un rectángulo
base = float(input("Ingresa la base del rectángulo: "))
altura = float(input("Ingresa la altura del rectángulo: "))
area = base * altura
print("Área del rectángulo:", area)

# Ejemplo 2: verificar si un número es par
num = int(input("Ingresa un número: "))
print("¿Es par?", num % 2 == 0)

# Ejemplo 3: combinar condiciones lógicas
edad = int(input("Ingresa tu edad: "))
tiene_dni = input("¿Tienes DNI? (s/n): ") == "s"
print("¿Puedes votar?", edad >= 18 and tiene_dni)
