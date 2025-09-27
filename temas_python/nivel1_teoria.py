# =========================
# NIVEL 1 - TEORÍA EN PYTHON
# =========================

# 1. Variables en Python
# Una variable es un espacio donde guardamos un valor.
nombre = "Juan"
edad = 25
pi = 3.1416
print(nombre, edad, pi)

# 2. Tipos de datos básicos
# Python maneja diferentes tipos de datos.
entero = 10
flotante = 3.5
cadena = "Hola"
booleano = True
print(entero, flotante, cadena, booleano)

# 3. Operaciones básicas
# Podemos hacer operaciones matemáticas.
a = 5
b = 2
print("Suma:", a + b)
print("Resta:", a - b)
print("Multiplicación:", a * b)
print("División:", a / b)
print("División entera:", a // b)
print("Módulo:", a % b)

# 4. Función type()
# Sirve para saber el tipo de un dato.
print(type(entero))
print(type(flotante))
print(type(cadena))
print(type(booleano))

# 5. Entrada por teclado con input()
# input() permite pedir datos al usuario.
nombre_usuario = input("¿Cómo te llamas? ")
print("Hola", nombre_usuario)

edad_usuario = int(input("¿Cuántos años tienes? "))
print("El próximo año tendrás:", edad_usuario + 1)
