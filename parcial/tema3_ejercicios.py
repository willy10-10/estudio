# ==========================================================
# 🔹 EJERCICIOS BÁSICOS (1–10)
# ==========================================================

print("Ejercicio 1")
# Programa que determine si un número es positivo o negativo.
num = -5
if num >= 0:
    print("El número es positivo")
else:
    print("El número es negativo")

print("Ejercicio 2")
# Verificar si una persona es mayor o menor de edad.
edad = 17
if edad >= 18:
    print("Mayor de edad")
else:
    print("Menor de edad")

print("Ejercicio 3")
# Programa que indique si un número es par o impar.
n = 8
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

print("Ejercicio 4")
# Determinar si una contraseña es correcta.
password = "1234"
if password == "1234":
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

print("Ejercicio 5")
# Decidir si se aprueba un examen (nota mínima 11).
nota = 9
if nota >= 11:
    print("Aprobado")
else:
    print("Desaprobado")

print("Ejercicio 6")
# Verificar si una persona puede votar (>=18 años).
edad = 20
if edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")

print("Ejercicio 7")
# Programa que indique si un número es múltiplo de 5.
x = 25
if x % 5 == 0:
    print("Es múltiplo de 5")
else:
    print("No es múltiplo de 5")

print("Ejercicio 8")
# Comparar dos números e indicar cuál es mayor.
a, b = 7, 10
if a > b:
    print("a es mayor")
else:
    print("b es mayor")

print("Ejercicio 9")
# Determinar si un número es igual a cero o no.
n = 0
if n == 0:
    print("El número es cero")
else:
    print("El número no es cero")

print("Ejercicio 10")
# Verificar si un número ingresado está en un rango (1 a 10).
n = 15
if 1 <= n <= 10:
    print("Está en el rango")
else:
    print("Fuera de rango")


# ==========================================================
# 🔹 EJERCICIOS INTERMEDIOS (11–20)
# ==========================================================

print("Ejercicio 11")
# Verificar si un número es divisible entre 3.
num = 9
if num % 3 == 0:
    print("Es divisible entre 3")
else:
    print("No es divisible entre 3")

print("Ejercicio 12")
# Programa que indique si una letra es vocal o consonante.
letra = "b"
if letra.lower() in "aeiou":
    print("Es vocal")
else:
    print("Es consonante")

print("Ejercicio 13")
# Determinar si un año es mayor a 2000.
anio = 1995
if anio > 2000:
    print("Es posterior al año 2000")
else:
    print("Es anterior o igual al 2000")

print("Ejercicio 14")
# Verificar si un número es de dos dígitos.
n = 45
if 10 <= abs(n) <= 99:
    print("Es de dos dígitos")
else:
    print("No es de dos dígitos")

print("Ejercicio 15")
# Calcular si un número es par o impar y mostrar mensaje personalizado.
num = 13
if num % 2 == 0:
    print("El número", num, "es par")
else:
    print("El número", num, "es impar")

print("Ejercicio 16")
# Determinar si una persona puede acceder a un descuento (edad >= 60).
edad = 62
if edad >= 60:
    print("Tiene descuento")
else:
    print("No tiene descuento")

print("Ejercicio 17")
# Indicar si un número ingresado es mayor a 100.
num = 150
if num > 100:
    print("Mayor a 100")
else:
    print("Menor o igual a 100")

print("Ejercicio 18")
# Comparar dos cadenas y verificar si son iguales.
s1, s2 = "python", "Python"
if s1 == s2:
    print("Son iguales")
else:
    print("Son diferentes")

print("Ejercicio 19")
# Verificar si un número es positivo y par al mismo tiempo.
n = 6
if n > 0 and n % 2 == 0:
    print("Es positivo y par")
else:
    print("No cumple ambas condiciones")

print("Ejercicio 20")
# Indicar si un número termina en 0.
num = 130
if num % 10 == 0:
    print("Termina en 0")
else:
    print("No termina en 0")


# ==========================================================
# 🔹 EJERCICIOS AVANZADOS (21–30)
# ==========================================================

print("Ejercicio 21")
# Verificar si una persona puede entrar a una discoteca (>=18 años).
edad = 17
if edad >= 18:
    print("Puede ingresar")
else:
    print("No puede ingresar")

print("Ejercicio 22")
# Determinar si un número está entre -10 y 10.
n = -5
if -10 <= n <= 10:
    print("Está en el rango -10 a 10")
else:
    print("Fuera de rango")

print("Ejercicio 23")
# Verificar si una cadena no está vacía.
texto = "Hola"
if texto != "":
    print("La cadena tiene contenido")
else:
    print("La cadena está vacía")

print("Ejercicio 24")
# Indicar si un número es negativo o cero.
n = 0
if n < 0:
    print("Negativo")
else:
    print("Cero o positivo")

print("Ejercicio 25")
# Calcular si una persona puede jubilarse (>=65 años).
edad = 70
if edad >= 65:
    print("Puede jubilarse")
else:
    print("No puede jubilarse aún")

print("Ejercicio 26")
# Verificar si un número es mayor que otro y múltiplo de este.
a, b = 20, 5
if a > b and a % b == 0:
    print(a, "es múltiplo de", b)
else:
    print("No cumple la condición")

print("Ejercicio 27")
# Determinar si una palabra empieza con "a".
palabra = "amigo"
if palabra.lower().startswith("a"):
    print("Empieza con 'a'")
else:
    print("No empieza con 'a'")

print("Ejercicio 28")
# Verificar si una lista contiene más de 5 elementos.
lista = [1, 2, 3, 4, 5, 6]
if len(lista) > 5:
    print("La lista tiene más de 5 elementos")
else:
    print("La lista tiene 5 o menos elementos")

print("Ejercicio 29")
# Indicar si un número es positivo y mayor a 50.
num = 75
if num > 0 and num > 50:
    print("Es positivo y mayor a 50")
else:
    print("No cumple las condiciones")

print("Ejercicio 30")
# Verificar si dos números son iguales y positivos.
x, y = 10, 10
if x == y and x > 0:
    print("Son iguales y positivos")
else:
    print("No cumplen ambas condiciones")
