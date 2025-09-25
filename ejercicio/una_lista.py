print("Con una sola lista")

num = [1,2,3,4,5,6,7,8,9,10]

print("Ejercicio 1")
#imprime todos los elementos con un for
for i in num:
    print(i)

print("Ejercicio 2")
#recorre toda la lista num y muestra solo los pares
for i in num:
    if i % 2 == 0:
        print(i)

print("Ejercicio 3")
#calcula la suma de todos los elemento de num
suma = 0
for i in num:
    suma = suma + i
print(suma)

print("Ejercicio 4")
#eleva al cuadrado todo los elementos de num
for i in num:
    valores = i ** 2
    print(valores)

print("Ejercicio 5")
#pide al usario que ingrese 5 numeros, guardalos en una lista y imprimelo al revès
numeros = []
for i in range(5):
    n = int(input("Ingresa un numero: "))
    numeros.append(n)
print(numeros[::-1])





