print("con varias listas")

tabla = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Ejercicio 1")
#recorre todos los elementos e inprimelos uno por uno
for i in tabla:
    for j in i:
        print(j)

print("Ejercicio 2")
#imprime solo la primera fila de la tabla
print(tabla[0])

print("Ejercicio 3")
#imrprime solo la ultima columna de la tabla
for i in range(len(tabla)):
    print(tabla[i][2])

print("Ejercicio 4")
#calcula la suma de todos los elementos de la tabla
suma = 0
for i in range(len(tabla)):
    for j in range(len(tabla[i])):
        suma += tabla[i][j]
print(suma)

print("Ejercicio 5")
#convierte todo los elementos de la tabla en su cuadrado
for i in tabla:
    nueva_tabla = []
    for j in i:
        nueva_tabla.append(j ** 2)
    print(nueva_tabla)







