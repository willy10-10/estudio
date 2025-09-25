print("Ejercicio 1")
#imprime los numeros del 1 al 10
x = 1
while x <= 10:
    print(x)
    x = x + 1

print("Ejercicio 2")
#imprime los numeros del 10 al 1
x = 10
while x >= 1:
    print(x)
    x = x - 1

print("Ejercicio 3")
#calcula la suma de los numeros 1 al 100
suma = 0
x = 1
while x <= 100:
    suma = suma + x
    x = x + 1
print(suma)

print("Ejercicio 4")
#imprime los numeros pares del 1 al 50
x = 1
while x <= 50:
    if x % 2 == 0:
        print(x)
    x = x + 1

print("Ejercicio 5")
#pide un numero al usario y muestra su tabla de multiplicar del 1 al 10
n = int(input("Ingresa un numero: "))
i = 1
while i <= 10:
    print(i * n)
    i = i + 1

print("Ejercicio 6")
#pide al usario una palabra y que termine el bucle al escribir "salir"
texto = ""
while texto != "salir":
    texto = input("Ingresa un palabra: ")
    print(texto)


