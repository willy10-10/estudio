print("SUMA")
#Suma de matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

resultado = [[0, 0],
             [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        resultado[i][j] = A[i][j] + B[i][j]

for fila in resultado:
    print(fila)

print("RESTA")
#Resta de matrices
A = [[5, 6],
     [7, 8]]

B = [[1, 2],
     [3, 4]]

resultado = [[0, 0],
             [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        resultado[i][j] = A[i][j] - B[i][j]

for fila in resultado:
    print(fila)

print("MULTIPLICACION")
#Multiplicaión de matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

resultado = [[0, 0],
             [0, 0]]

for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            resultado[i][j] += A[i][k] * B[k][j]

for fila in resultado:
    print(fila)

print("TRANSPUESTA")
#Transpuesta de una matriz
A = [[1, 2, 3],
     [4, 5, 6]]

transpuesta = [[0, 0],
               [0, 0],
               [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        transpuesta[j][i] = A[i][j]

for fila in transpuesta:
    print(fila)

