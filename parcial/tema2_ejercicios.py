# ============================================================
# ✅ SOLUCIONES — TEMA 2: EXPRESIONES, OPERACIONES Y OPERADORES LÓGICOS
# ============================================================
# Nota:
# Cada ejercicio incluye su enunciado como comentario de varias líneas
# para que sea más fácil leer y entender antes de ejecutar.
# ============================================================


# -------------------------
# 📌 EJERCICIOS BÁSICOS (1–10)
# -------------------------

print("Ejercicio 1")
# ------------------------------------------------------------
# Pide dos números y muestra su suma.
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("Suma:", a + b)


print("Ejercicio 2")
# ------------------------------------------------------------
# Pide dos números y muestra su resta.
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("Resta:", a - b)


print("Ejercicio 3")
# ------------------------------------------------------------
# Pide dos números y muestra su multiplicación.
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("Multiplicación:", a * b)


print("Ejercicio 4")
# ------------------------------------------------------------
# Pide dos números y muestra su división.
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("División:", a / b)


print("Ejercicio 5")
# ------------------------------------------------------------
# Pide dos números y muestra:
# - la división entera (//)
# - el residuo o módulo (%)
# ------------------------------------------------------------
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))
print("División entera:", a // b)
print("Residuo:", a % b)


print("Ejercicio 6")
# ------------------------------------------------------------
# Pide un número y muestra su cuadrado.
# ------------------------------------------------------------
n = int(input("Ingresa un número: "))
print("Cuadrado:", n ** 2)


print("Ejercicio 7")
# ------------------------------------------------------------
# Pide un número y muestra su cubo.
# ------------------------------------------------------------
n = int(input("Ingresa un número: "))
print("Cubo:", n ** 3)


print("Ejercicio 8")
# ------------------------------------------------------------
# Pide tres números y muestra su suma total.
# ------------------------------------------------------------
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
print("Suma total:", n1 + n2 + n3)


print("Ejercicio 9")
# ------------------------------------------------------------
# Pide un número decimal y muéstralo redondeado a 2 decimales.
# ------------------------------------------------------------
n = float(input("Ingresa un número decimal: "))
print("Redondeado a 2 decimales:", round(n, 2))


print("Ejercicio 10")
# ------------------------------------------------------------
# Pide dos números y muestra el mayor usando max().
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("El mayor es:", max(a, b))


# -------------------------
# 📌 EJERCICIOS INTERMEDIOS (11–20)
# -------------------------

print("Ejercicio 11")
# ------------------------------------------------------------
# Pide dos números y muestra si son iguales (==).
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("¿Son iguales?", a == b)


print("Ejercicio 12")
# ------------------------------------------------------------
# Pide dos números y muestra si son diferentes (!=).
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("¿Son diferentes?", a != b)


print("Ejercicio 13")
# ------------------------------------------------------------
# Pide dos números y muestra si el primero es mayor que el segundo (>).
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("¿El primero es mayor?", a > b)


print("Ejercicio 14")
# ------------------------------------------------------------
# Pide dos números y muestra si el primero es menor o igual al segundo (<=).
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("¿El primero es menor o igual?", a <= b)


print("Ejercicio 15")
# ------------------------------------------------------------
# Pide tres números y calcula su promedio.
# ------------------------------------------------------------
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
prom = (n1 + n2 + n3) / 3
print("Promedio:", prom)


print("Ejercicio 16")
# ------------------------------------------------------------
# Pide tu edad y muestra si eres mayor o igual a 18.
# ------------------------------------------------------------
edad = int(input("Ingresa tu edad: "))
print("¿Mayor o igual a 18?", edad >= 18)


print("Ejercicio 17")
# ------------------------------------------------------------
# Pide un número y muestra si es positivo (n > 0).
# ------------------------------------------------------------
n = float(input("Ingresa un número: "))
print("¿Es positivo?", n > 0)


print("Ejercicio 18")
# ------------------------------------------------------------
# Pide un número y muestra si es múltiplo de 5 (n % 5 == 0).
# ------------------------------------------------------------
n = int(input("Ingresa un número entero: "))
print("¿Es múltiplo de 5?", n % 5 == 0)


print("Ejercicio 19")
# ------------------------------------------------------------
# Pide dos números y muestra True si ambos son pares.
# (usar operador lógico AND)
# ------------------------------------------------------------
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
print("¿Ambos son pares?", a % 2 == 0 and b % 2 == 0)


print("Ejercicio 20")
# ------------------------------------------------------------
# Pide dos números y muestra True si al menos uno es impar.
# (usar operador lógico OR)
# ------------------------------------------------------------
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
print("¿Al menos uno es impar?", a % 2 != 0 or b % 2 != 0)


# -------------------------
# 📌 EJERCICIOS AVANZADOS (21–30)
# -------------------------

print("Ejercicio 21")
# ------------------------------------------------------------
# Pide tres números y muestra el mayor usando max().
# ------------------------------------------------------------
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
print("El mayor es:", max(n1, n2, n3))


print("Ejercicio 22")
# ------------------------------------------------------------
# Pide tres números y muestra el menor usando min().
# ------------------------------------------------------------
n1 = float(input("Ingresa el primer número: "))
n2 = float(input("Ingresa el segundo número: "))
n3 = float(input("Ingresa el tercer número: "))
print("El menor es:", min(n1, n2, n3))


print("Ejercicio 23")
# ------------------------------------------------------------
# Pide un número y muestra True si está entre 1 y 10.
# (condición compuesta: 1 <= n <= 10)
# ------------------------------------------------------------
n = int(input("Ingresa un número: "))
print("¿Está entre 1 y 10?", 1 <= n <= 10)


print("Ejercicio 24")
# ------------------------------------------------------------
# Pide tu edad y muestra True si está en el rango 18–30 inclusive.
# ------------------------------------------------------------
edad = int(input("Ingresa tu edad: "))
print("¿Edad entre 18 y 30?", 18 <= edad <= 30)


print("Ejercicio 25")
# ------------------------------------------------------------
# Pide un número y muestra True si es par y mayor que 10.
# ------------------------------------------------------------
n = int(input("Ingresa un número: "))
print("¿Es par y mayor que 10?", n % 2 == 0 and n > 10)


print("Ejercicio 26")
# ------------------------------------------------------------
# Pide dos números y muestra True si ambos son positivos.
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("¿Ambos son positivos?", a > 0 and b > 0)


print("Ejercicio 27")
# ------------------------------------------------------------
# Pide dos números y muestra True si:
# - uno es mayor a 100
# - o el otro es menor a 50
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("¿Uno mayor a 100 o el otro menor a 50?", a > 100 or b < 50)


print("Ejercicio 28")
# ------------------------------------------------------------
# Pide un número y muestra True si NO es múltiplo de 3.
# (usar operador lógico NOT)
# ------------------------------------------------------------
n = int(input("Ingresa un número: "))
print("¿No es múltiplo de 3?", not (n % 3 == 0))


print("Ejercicio 29")
# ------------------------------------------------------------
# Pide tres números y muestra True si el primero es
# el promedio de los otros dos.
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
print("¿El primero es el promedio de los otros dos?", a == (b + c) / 2)


print("Ejercicio 30")
# ------------------------------------------------------------
# Pide dos números y muestra True si:
# - su suma es mayor que 50
# - y ambos son distintos
# ------------------------------------------------------------
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("¿La suma > 50 y distintos?", (a + b > 50) and (a != b))
