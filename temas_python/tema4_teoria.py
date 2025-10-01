# ============================================================
# 📘 TEMA 4.1: CONDICIONALES COMPUESTAS (if – elif – else)
# ============================================================

# 🔹 Introducción
# Hasta ahora vimos el uso de "if" y "else".
# Pero a veces no solo existen 2 posibilidades, sino varias.
# En estos casos, usamos "elif" (else if).
#
# Sintaxis:
# if condicion1:
#     # código si se cumple la condicion1
# elif condicion2:
#     # código si se cumple la condicion2
# elif condicion3:
#     # código si se cumple la condicion3
# else:
#     # código si ninguna condicion se cumple


# 🔹 Ejemplo 1: Clasificación por edad
edad = 20

if edad < 12:
    print("Eres un niño")
elif edad < 18:
    print("Eres un adolescente")
elif edad < 60:
    print("Eres un adulto")
else:
    print("Eres un adulto mayor")


# 🔹 Ejemplo 2: Calificaciones
nota = 15

if nota >= 18:
    print("Excelente")
elif nota >= 14:
    print("Bueno")
elif nota >= 11:
    print("Regular")
else:
    print("Desaprobado")


# 🔹 Ejemplo 3: Selección de menú
opcion = 2

if opcion == 1:
    print("Has elegido Pizza")
elif opcion == 2:
    print("Has elegido Hamburguesa")
elif opcion == 3:
    print("Has elegido Ensalada")
else:
    print("Opción no válida")

# ============================================================
# 📘 TEMA 4.2: CONDICIONALES ANIDADAS
# ============================================================

# 🔹 Introducción
# Una condicional anidada significa tener un "if" dentro de otro.
# Esto permite evaluar condiciones más específicas después
# de que se cumple una condición general.
#
# Sintaxis:
# if condicion1:
#     if condicion2:
#         # código si se cumplen ambas
#     else:
#         # código si solo se cumple la primera
# else:
#     # código si no se cumple la primera


# 🔹 Ejemplo 1: Verificar mayor de edad y nacionalidad
edad = 20
nacionalidad = "Peruana"

if edad >= 18:
    if nacionalidad == "Peruana":
        print("Eres mayor de edad en Perú")
    else:
        print("Eres mayor de edad pero extranjero")
else:
    print("Eres menor de edad")


# 🔹 Ejemplo 2: Clasificación de números
numero = -5

if numero >= 0:
    if numero % 2 == 0:
        print("Número positivo par")
    else:
        print("Número positivo impar")
else:
    if numero % 2 == 0:
        print("Número negativo par")
    else:
        print("Número negativo impar")


# 🔹 Ejemplo 3: Acceso según usuario y contraseña
usuario = "admin"
password = "1234"

if usuario == "admin":
    if password == "1234":
        print("Acceso concedido")
    else:
        print("Contraseña incorrecta")
else:
    print("Usuario no válido")

