# ============================================================
# 📘 TEMA 3: ESTRUCTURAS CONDICIONALES SIMPLES (if - else)
# ============================================================
# En programación, necesitamos que un programa tome decisiones.
# Para eso usamos las estructuras condicionales.
#
# En Python, la más básica es el "if", y puede ir acompañado de "else".
# ============================================================


# ------------------------------------------------------------
# 📌 1. Sintaxis básica de if
# ------------------------------------------------------------
# if condicion:
#     # código si la condición es True
# ------------------------------------------------------------

edad = 20
if edad >= 18:
    print("Eres mayor de edad")  # Se ejecuta porque la condición es verdadera


# ------------------------------------------------------------
# 📌 2. Sintaxis básica de if - else
# ------------------------------------------------------------
# if condicion:
#     # código si la condición es True
# else:
#     # código si la condición es False
# ------------------------------------------------------------

edad = 15
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")  # Se ejecuta porque la condición es falsa


# ------------------------------------------------------------
# 📌 3. Condiciones con operadores relacionales
# ------------------------------------------------------------
# ==   igual a
# !=   diferente a
# >    mayor que
# <    menor que
# >=   mayor o igual que
# <=   menor o igual que
# ------------------------------------------------------------

numero = 10
if numero == 10:
    print("El número es igual a 10")
else:
    print("El número no es igual a 10")


# ------------------------------------------------------------
# 📌 4. Condiciones con operadores lógicos
# ------------------------------------------------------------
# and → True si ambas condiciones son verdaderas
# or  → True si al menos una condición es verdadera
# not → Invierte el valor lógico
# ------------------------------------------------------------

edad = 25
if edad >= 18 and edad <= 30:
    print("Tienes entre 18 y 30 años")
else:
    print("No estás entre 18 y 30 años")


# ------------------------------------------------------------
# 📌 5. Uso de variables booleanas
# ------------------------------------------------------------
es_estudiante = True
if es_estudiante:
    print("Eres estudiante")
else:
    print("No eres estudiante")


# ------------------------------------------------------------
# 📌 6. if - else con input del usuario
# ------------------------------------------------------------
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")


# ------------------------------------------------------------
# 📌 7. Ejemplo práctico: verificar contraseña
# ------------------------------------------------------------
contrasena = "python123"
ingreso = input("Ingresa tu contraseña: ")
if ingreso == contrasena:
    print("Acceso concedido")
else:
    print("Acceso denegado")


# ============================================================
# ✅ Resumen del Tema 3
# ============================================================
# - if permite ejecutar código solo si una condición es verdadera.
# - if - else nos permite ejecutar un bloque alternativo cuando
#   la condición es falsa.
# - Operadores relacionales y lógicos permiten construir condiciones.
# - Las condiciones se pueden basar en variables, cálculos o input.
# ============================================================
