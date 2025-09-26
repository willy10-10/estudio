# Pregunta 1
# Escribe la función piramide_numeros que reciba un número entero n
# y genere una pirámide de números de 1 hasta n en formato lista.
def piramide_numeros(n):
    piramide = []
    for i in range(1, n + 1):
        fila = []
        for j in range(1, i + 1):
            fila.append(j)
        piramide.append(fila)
    return piramide

print("Pregunta 1:", piramide_numeros(4))


# Pregunta 2
# Implementa la función sumar_diagonal_secundaria que tome una matriz cuadrada
# y devuelva la suma de los números que están en su diagonal secundaria.
def sumar_diagonal_secundaria(matriz):
    n = len(matriz)
    suma = 0
    for i in range(n):
        suma += matriz[i][n - 1 - i]
    return suma

print("Pregunta 2:", sumar_diagonal_secundaria([[1, 2, 3], [4, 5, 6], [17, 18, 19]]))


# Pregunta 3
# Implementa la función sumar_cifras_fecha que reciba una fecha en formato DD/MM/AAAA
# y devuelva la suma de todas las cifras numéricas de la fecha.
def sumar_cifras_fecha(fecha):
    suma = 0
    for caracter in fecha:
        if caracter.isdigit():
            suma += int(caracter)
    return suma

print("Pregunta 3:", sumar_cifras_fecha("22/09/2024"))


# Pregunta 4
# Escribe la función espiral que tome un número entero n
# y devuelva una lista con los números del 1 al n organizados en forma de espiral.
# Ejemplo: espiral(5) -> [1,2,3,4,5,10,9,8,7,6]
def espiral(n):
    lista = []  # aquí vamos guardando el resultado

    # Primero agregamos los números del 1 hasta n
    for i in range(1, n + 1):
        lista.append(i)

    # Después agregamos los números desde 2*n hasta n+1 (pero en orden descendente)
    for i in range(2 * n, n, -1):
        lista.append(i)

    return lista

print("Pregunta 4:", espiral(5))


# Pregunta 5
# Escribe la función numero_espejo recursiva que tome un número
# y devuelva su número espejo (invertido).
def numero_espejo(num):
    num_str = str(num)
    if len(num_str) == 1:
        return int(num_str)
    else:
        return int(num_str[-1] + str(numero_espejo(int(num_str[:-1]))))

print("Pregunta 5:", numero_espejo(1234))


# Pregunta 6
# Crea la función tablero_ajedrez que reciba un número n
# y genere un patrón de tablero de ajedrez de n x n usando listas.
def tablero_ajedrez(n):
    tablero = []
    for i in range(n):
        fila = []
        for j in range(n):
            if (i + j) % 2 == 0:
                fila.append("B")
            else:
                fila.append("N")
        tablero.append(fila)
    return tablero

print("Pregunta 6:", tablero_ajedrez(3))


# Pregunta 7
# Implementa la función sumar_impares_diagonal que tome una matriz cuadrada
# y devuelva la suma de los números impares que están en su diagonal principal.
def sumar_impares_diagonal(matriz):
    n = len(matriz)
    suma = 0
    for i in range(n):
        if matriz[i][i] % 2 != 0:
            suma += matriz[i][i]
    return suma

print("Pregunta 7:", sumar_impares_diagonal([[1, 2, 3], [5, 4, 6], [7, 8, 9]]))


# Pregunta 8
# Crea una función que reciba un número entero y lo transforme en una lista
# de todos sus divisores, usando iteración.
def divisores_numero(n):
    divisores = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisores.append(i)
    return divisores

print("Pregunta 8:", divisores_numero(12))


# Pregunta 9
# Implementa la función eliminar_digitos_repetidos que reciba un número
# y elimine los dígitos repetidos, dejando solo una ocurrencia de cada uno.
def eliminar_digitos_repetidos(num):
    resultado = ""
    for digito in str(num):
        if digito not in resultado:
            resultado += digito
    return int(resultado)

print("Pregunta 9:", eliminar_digitos_repetidos(122333))


# Pregunta 10
# Crea la función sumar_pares que reciba una lista de números
# y sume solo los números en las posiciones pares de la lista.
def sumar_pares(lista):
    suma = 0
    for i in range(0, len(lista), 2):
        suma += lista[i]
    return suma

print("Pregunta 10:", sumar_pares([10, 20, 30, 40, 50]))


# Pregunta 11
# Implementa la función rota_elementos que tome una lista
# y la "traslade" k posiciones a la derecha.
def rota_elementos(lista, k):
    k = k % len(lista)
    return lista[-k:] + lista[:-k]

print("Pregunta 11:", rota_elementos([1, 2, 3, 4, 5], 2))
