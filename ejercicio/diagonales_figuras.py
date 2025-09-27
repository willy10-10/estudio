#Mini ejemplos
#crear una matriz 2x2

matriz = [
    [1,2],
    [3,4]
]

print("Ejemplo 1")
#imprimir la matriz
print(matriz)

print("Ejemplo 2")
#acceder a un elemento especifico
print(matriz[0][1])

print("Ejemplo 3")
#modificar un elemento
matriz[0][1] = 10
print(matriz)

print("Ejemplo 4")
#recorrer la matriz con for anidada
for fila in matriz:
    for elemento in fila:
        print(elemento)

print("Ejemplo 5")
#crear matriz nxn automaticamente con for
n = 3
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)

#Ejercicios
print("Ejercicio 1")
#crea una matriz 3x3 con la diganal principal de 1 y el resto de 0
n = 3
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i == j:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)

print("Ejercicio 2")
n = 3
matriz = []
for i in range(n):
    fila = []
    for j in range(n):
        if i + j == n - 1:
            fila.append(1)
        else:
            fila.append(0)
    matriz.append(fila)

for fila in matriz:
    print(fila)
