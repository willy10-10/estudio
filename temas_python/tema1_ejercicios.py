# -------------------------
# 📌 EJERCICIOS BÁSICOS (1–5)
# -------------------------

print("Ejercicio 1")
# ------------------------------------------------------------
# Escribe un programa que muestre en pantalla el texto:
# "¡Hola, mundo!"
# ------------------------------------------------------------
print("¡Hola, mundo!")


print("Ejercicio 2")
# ------------------------------------------------------------
# Pide al usuario su nombre y muéstralo en pantalla.
# ------------------------------------------------------------
nombre = input("Ingresa tu nombre: ")
print("Tu nombre es:", nombre)


print("Ejercicio 3")
# ------------------------------------------------------------
# Pide tu edad y muéstrala en pantalla.
# ------------------------------------------------------------
edad = input("Ingresa tu edad: ")
print("Tu edad es:", edad)


print("Ejercicio 4")
# ------------------------------------------------------------
# Pide tu nombre y edad, y muéstralos juntos en un mensaje.
# ------------------------------------------------------------
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
print("Te llamas", nombre, "y tienes", edad, "años.")


print("Ejercicio 5")
# ------------------------------------------------------------
# Declara una variable llamada ciudad y asígnale un valor.
# Luego muestra en pantalla la ciudad.
# ------------------------------------------------------------
ciudad = "Lima"
print("Ciudad:", ciudad)


# -------------------------
# 📌 EJERCICIOS INTERMEDIOS (6–10)
# -------------------------

print("Ejercicio 6")
# ------------------------------------------------------------
# Pide dos números enteros y muéstralos en pantalla.
# ------------------------------------------------------------
n1 = int(input("Ingresa el primer número: "))
n2 = int(input("Ingresa el segundo número: "))
print("Número 1:", n1)
print("Número 2:", n2)


print("Ejercicio 7")
# ------------------------------------------------------------
# Declara tres variables: país, capital y población.
# Asigna valores y muéstralos en pantalla.
# ------------------------------------------------------------
pais = "Perú"
capital = "Lima"
poblacion = 33000000
print("País:", pais)
print("Capital:", capital)
print("Población:", poblacion)


print("Ejercicio 8")
# ------------------------------------------------------------
# Pide al usuario su color favorito y guárdalo en una variable.
# Luego muestra un mensaje con ese color.
# ------------------------------------------------------------
color = input("Ingresa tu color favorito: ")
print("Tu color favorito es:", color)


print("Ejercicio 9")
# ------------------------------------------------------------
# Declara una variable booleana (True o False) llamada estudiante.
# Asigna True si eres estudiante, y muéstralo en pantalla.
# ------------------------------------------------------------
estudiante = True
print("¿Eres estudiante?", estudiante)


print("Ejercicio 10")
# ------------------------------------------------------------
# Pide tu nombre y edad, y crea un mensaje concatenando ambas variables.
# Ejemplo: "Me llamo Ana y tengo 20 años."
# ------------------------------------------------------------
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
mensaje = "Me llamo " + nombre + " y tengo " + edad + " años."
print(mensaje)


# -------------------------
# 📌 EJERCICIOS AVANZADOS (11–15)
# -------------------------

print("Ejercicio 11")
# ------------------------------------------------------------
# Pide dos números enteros y guarda su suma en una variable.
# Luego muestra el resultado.
# ------------------------------------------------------------
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
suma = a + b
print("La suma es:", suma)


print("Ejercicio 12")
# ------------------------------------------------------------
# Pide al usuario su nombre completo y muéstralo en mayúsculas.
# ------------------------------------------------------------
nombre = input("Ingresa tu nombre completo: ")
print("En mayúsculas:", nombre.upper())


print("Ejercicio 13")
# ------------------------------------------------------------
# Pide una palabra y muestra cuántas letras tiene usando len().
# ------------------------------------------------------------
palabra = input("Ingresa una palabra: ")
print("La palabra tiene", len(palabra), "letras.")


print("Ejercicio 14")
# ------------------------------------------------------------
# Declara una variable con tu año de nacimiento y calcula tu edad
# suponiendo que estamos en 2025.
# ------------------------------------------------------------
anio_nacimiento = int(input("Ingresa tu año de nacimiento: "))
edad = 2025 - anio_nacimiento
print("Tu edad aproximada es:", edad)


print("Ejercicio 15")
# ------------------------------------------------------------
# Pide dos números decimales y calcula su promedio.
# ------------------------------------------------------------
n1 = float(input("Ingresa el primer número decimal: "))
n2 = float(input("Ingresa el segundo número decimal: "))
promedio = (n1 + n2) / 2
print("El promedio es:", promedio)

