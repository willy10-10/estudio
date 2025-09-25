print("Ejercicio 1")
#Dada una matriz, calcula el promedio de todos sus elementos
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

suma = 0
cantidad = 0

for fila in matriz:
    for elemento in fila:
        suma += elemento
        cantidad += 1

promedio = suma / cantidad
print(promedio)

print("Ejercicio 2")
#Dada una matriz, calcula la suma de cada una de sus filas y muestra el resultado.
#primer metodo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    print(sum(fila))
#segundo metodo
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for fila in matriz:
    suma = 0
    for elemento in fila:
        suma += elemento
    print(suma)

print("Ejercicio 3")
#Dada una matriz, calcula el promedio de cada columna.
matriz = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

filas = len(matriz)
columnas = len(matriz[0])

for j in range(columnas):
    suma = 0
    for i in range(filas):
        suma += matriz[i][j]
    print(suma / filas)

print("Ejercicio 4")
#Escribe un programa que muestre los elementos de la
#diagonal principal de una matriz cuadrada.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

filas = len(matriz)

for i in range(filas):
    print(matriz[i][i])

print("Ejercicio 5")
#Dada una matriz cuadrada, calcula la suma de los elementos
#de la diagonal secundaria.
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matriz)
suma = 0

for i in range(n):
    suma += matriz[i][n - 1 - i]

print(suma)

print("Ejercicio 6")
#Escribe un programa que obtenga la matriz transpuesta de
#una matriz dada.
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

filas = len(matriz)
columnas = len(matriz[0])

for j in range(columnas):
    fila_transpuesta = []
    for i in range(filas):
        fila_transpuesta.append(matriz[i][j])
    print(fila_transpuesta)

print("Ejercicio 7")
#Dadas dos matrices de dimensiones compatibles, calcule su
#producto.
A = [[1, 2],
     [3, 4]]

B = [[2, 0],
     [1, 2]]

C = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            C[i][j] = C[i][j] + A[i][k] * B[k][j]

for fila in C:
    print(fila)




