###########################################
#   TEMA 4: CONDICIONALES COMPUESTAS Y 
#           ANIDADAS (if – elif – else)
###########################################

### NIVEL BÁSICO ###

# Ejercicio 1
# Pedir un número al usuario y mostrar si es
# positivo, negativo o cero.
print("Ejercicio 1")
num = int(input("Ingrese un número: "))
if num > 0:
    print("El número es positivo")
elif num < 0:
    print("El número es negativo")
else:
    print("El número es cero")

# Ejercicio 2
# Pedir la edad de una persona y decir si es
# menor de edad, mayor de edad o adulto mayor.
print("Ejercicio 2")
edad = int(input("Ingrese su edad: "))
if edad < 18:
    print("Eres menor de edad")
elif edad < 60:
    print("Eres mayor de edad")
else:
    print("Eres adulto mayor")

# Ejercicio 3
# Pedir una nota (0 a 20) y mostrar:
# - Aprobado si es mayor o igual a 11
# - Caso contrario, Desaprobado.
print("Ejercicio 3")
nota = int(input("Ingrese su nota (0-20): "))
if nota >= 11:
    print("Aprobado")
else:
    print("Desaprobado")

# Ejercicio 4
# Pedir un número entero y decir si es:
# - Par positivo
# - Par negativo
# - Impar
print("Ejercicio 4")
n = int(input("Ingrese un número: "))
if n % 2 == 0 and n > 0:
    print("Es par positivo")
elif n % 2 == 0 and n < 0:
    print("Es par negativo")
else:
    print("Es impar")

# Ejercicio 5
# Pedir el nombre de un día de la semana
# y decir si es:
# - Día laboral
# - Fin de semana
print("Ejercicio 5")
dia = input("Ingrese un día de la semana: ").lower()
if dia in ["lunes", "martes", "miércoles", "miercoles", "jueves", "viernes"]:
    print("Es un día laboral")
elif dia in ["sábado", "sabado", "domingo"]:
    print("Es fin de semana")
else:
    print("Día no válido")

# Ejercicio 6
# Pedir un número del 1 al 12 y mostrar el mes
# correspondiente. Caso contrario, mensaje de error.
print("Ejercicio 6")
mes = int(input("Ingrese un número del 1 al 12: "))
if mes == 1:
    print("Enero")
elif mes == 2:
    print("Febrero")
elif mes == 3:
    print("Marzo")
elif mes == 4:
    print("Abril")
elif mes == 5:
    print("Mayo")
elif mes == 6:
    print("Junio")
elif mes == 7:
    print("Julio")
elif mes == 8:
    print("Agosto")
elif mes == 9:
    print("Septiembre")
elif mes == 10:
    print("Octubre")
elif mes == 11:
    print("Noviembre")
elif mes == 12:
    print("Diciembre")
else:
    print("Número inválido")

# Ejercicio 7
# Pedir dos números y mostrar cuál es mayor
# o si son iguales.
print("Ejercicio 7")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
if a > b:
    print("El primero es mayor")
elif b > a:
    print("El segundo es mayor")
else:
    print("Son iguales")

# Ejercicio 8
# Pedir un número y mostrar si está en el
# rango de 1 a 100, o fuera de rango.
print("Ejercicio 8")
num = int(input("Ingrese un número: "))
if 1 <= num <= 100:
    print("Está dentro del rango (1-100)")
else:
    print("Fuera de rango")

# Ejercicio 9
# Pedir la calificación de un examen (0-20)
# y clasificar:
# - Excelente: 18-20
# - Bueno: 14-17
# - Regular: 11-13
# - Insuficiente: 0-10
print("Ejercicio 9")
nota = int(input("Ingrese su nota (0-20): "))
if 18 <= nota <= 20:
    print("Excelente")
elif 14 <= nota <= 17:
    print("Bueno")
elif 11 <= nota <= 13:
    print("Regular")
else:
    print("Insuficiente")

# Ejercicio 10
# Pedir un número y decir si es divisible
# entre 2, 3 o ninguno.
print("Ejercicio 10")
num = int(input("Ingrese un número: "))
if num % 2 == 0 and num % 3 == 0:
    print("Es divisible entre 2 y 3")
elif num % 2 == 0:
    print("Es divisible entre 2")
elif num % 3 == 0:
    print("Es divisible entre 3")
else:
    print("No es divisible entre 2 ni 3")



### NIVEL INTERMEDIO ###

# Ejercicio 11
# Pedir tres números y mostrar el mayor.
print("Ejercicio 11")
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
if a >= b and a >= c:
    print("El mayor es:", a)
elif b >= a and b >= c:
    print("El mayor es:", b)
else:
    print("El mayor es:", c)

# Ejercicio 12
# Pedir el año y verificar si es bisiesto.
print("Ejercicio 12")
anio = int(input("Ingrese un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("Es bisiesto")
else:
    print("No es bisiesto")

# Ejercicio 13
# Pedir una letra y decir si es vocal o consonante.
print("Ejercicio 13")
letra = input("Ingrese una letra: ").lower()
if letra in "aeiou":
    print("Es una vocal")
elif letra.isalpha():
    print("Es una consonante")
else:
    print("No es una letra")

# Ejercicio 14
# Pedir el peso y la altura de una persona
# y calcular su IMC.
# Clasificar:
# - Bajo peso: <18.5
# - Normal: 18.5 - 24.9
# - Sobrepeso: 25 - 29.9
# - Obesidad: >=30
print("Ejercicio 14")
peso = float(input("Ingrese su peso (kg): "))
altura = float(input("Ingrese su altura (m): "))
imc = peso / (altura**2)
if imc < 18.5:
    print("Bajo peso")
elif imc < 25:
    print("Normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidad")

# Ejercicio 15
# Pedir un número del 1 al 7 y mostrar el día
# de la semana correspondiente.
print("Ejercicio 15")
n = int(input("Ingrese un número del 1 al 7: "))
if n == 1:
    print("Lunes")
elif n == 2:
    print("Martes")
elif n == 3:
    print("Miércoles")
elif n == 4:
    print("Jueves")
elif n == 5:
    print("Viernes")
elif n == 6:
    print("Sábado")
elif n == 7:
    print("Domingo")
else:
    print("Número inválido")

# Ejercicio 16
# Pedir dos números y una operación (+,-,*,/)
# y mostrar el resultado.
print("Ejercicio 16")
x = float(input("Ingrese primer número: "))
y = float(input("Ingrese segundo número: "))
op = input("Ingrese operación (+,-,*,/): ")
if op == "+":
    print("Resultado:", x + y)
elif op == "-":
    print("Resultado:", x - y)
elif op == "*":
    print("Resultado:", x * y)
elif op == "/":
    if y != 0:
        print("Resultado:", x / y)
    else:
        print("Error: división entre cero")
else:
    print("Operación inválida")

# Ejercicio 17
# Pedir un número y decir si es múltiplo
# de 5 y de 7 al mismo tiempo.
print("Ejercicio 17")
num = int(input("Ingrese un número: "))
if num % 5 == 0 and num % 7 == 0:
    print("Es múltiplo de 5 y 7")
elif num % 5 == 0:
    print("Es múltiplo de 5")
elif num % 7 == 0:
    print("Es múltiplo de 7")
else:
    print("No es múltiplo de 5 ni de 7")

# Ejercicio 18
# Pedir la hora en formato 24h y mostrar
# el saludo correspondiente:
# - Buenos días: 5-11
# - Buenas tardes: 12-18
# - Buenas noches: 19-23 y 0-4
print("Ejercicio 18")
hora = int(input("Ingrese la hora (0-23): "))
if 5 <= hora <= 11:
    print("Buenos días")
elif 12 <= hora <= 18:
    print("Buenas tardes")
elif (19 <= hora <= 23) or (0 <= hora <= 4):
    print("Buenas noches")
else:
    print("Hora inválida")

# Ejercicio 19
# Pedir tres notas y mostrar el promedio.
# Indicar si está aprobado (>=11) o desaprobado.
print("Ejercicio 19")
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))
prom = (n1 + n2 + n3) / 3
if prom >= 11:
    print("Aprobado con promedio:", prom)
else:
    print("Desaprobado con promedio:", prom)

# Ejercicio 20
# Pedir dos ángulos de un triángulo y calcular
# el tercero. Luego clasificar el triángulo:
# - Equilátero
# - Isósceles
# - Escaleno
print("Ejercicio 20")
a1 = int(input("Ingrese ángulo 1: "))
a2 = int(input("Ingrese ángulo 2: "))
a3 = 180 - (a1 + a2)
print("El tercer ángulo es:", a3)
if a1 == a2 == a3:
    print("Es un triángulo equilátero")
elif a1 == a2 or a1 == a3 or a2 == a3:
    print("Es un triángulo isósceles")
else:
    print("Es un triángulo escaleno")
