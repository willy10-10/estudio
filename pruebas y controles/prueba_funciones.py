# Ejercicio 1:
# Define la función incrementar que tome un número y lo incremente en 1.
# Declara una variable global llamada contador e intenta incrementarla dentro de la función.
# Observa qué sucede y ajusta el código para usar la variable global correctamente.

contador = 0  # variable global

def incrementar():
    global contador  # indicamos que se usará la variable global
    contador = contador + 1
    print("Contador dentro de la función:", contador)

incrementar()
print("Contador fuera de la función:", contador)
print("----")


# Ejercicio 2:
# Crea una función saludar que tenga un parámetro predefinido llamado nombre
# que por defecto sea “amigo”.
# Si se pasa un argumento a la función, este debe reemplazar el valor por defecto.

def saludar(nombre="amigo"):
    print(f"Hola, {nombre}!")

saludar()            # usa el valor por defecto
saludar("Roberto")   # usa el argumento pasado
print("----")


# Ejercicio 3:
# Crea una función es_par_o_impar que determine si un número es par o impar
# usando control de flujo if-else.
# La función debe devolver “par” si el número es par y “impar” si es impar.

def es_par_o_impar(numero):
    if numero % 2 == 0:   # if-else
        return "par"
    else:
        return "impar"

print("4 es", es_par_o_impar(4))
print("7 es", es_par_o_impar(7))
print("0 es", es_par_o_impar(0))
print("----")


# Ejercicio 4:
# Crea una función es_primo que tome un número entero y devuelva True si es primo
# o False en caso contrario.
# Un número primo es aquel que solo es divisible por 1 y por sí mismo.

def es_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

print("2 es primo?", es_primo(2))
print("15 es primo?", es_primo(15))
print("17 es primo?", es_primo(17))
print("1 es primo?", es_primo(1))
print("----")


# Ejercicio 5:
# Crea una función sumar_lista que tome una lista de números
# y devuelva la suma de todos sus elementos.
# La función debe manejar listas vacías devolviendo 0.

def sumar_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        suma = 0
        for numero in lista:
            suma += numero
        return suma

print("Suma [1, 2, 3, 4]:", sumar_lista([1, 2, 3, 4]))
print("Suma []:", sumar_lista([]))
print("Suma [10, -5, 7]:", sumar_lista([10, -5, 7]))
