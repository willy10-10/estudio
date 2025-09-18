#SUMA DE NUMEROS DEL UNO 1 AL 50
#Con while
i = 1
suma = 0
while i <= 50:
    suma += i
    i += 1
print(suma)
#Con for
suma = 0
for i in range(1,51):
    suma += i
print(suma)

#SUMA DE NUMEROS PARES DEL 1 AL 50
#Con while
i = 1
suma = 0
while i <= 50:
    if i % 2 == 0:
        suma += i
    i += 1
print(suma)
#Con for
suma = 0
for i in range(1,51):
    if i % 2 == 0:
        suma += i
print(suma)

#IMPRIME LOS NUMEROS IMPARES DEL 1 AL 50
#Con while
i = 1
while i <= 50:
    if i % 2 != 0:
        print(i)
    i += 1
#Con for
for i in range(1,51):
    if i % 2 != 0:
        print(i)
