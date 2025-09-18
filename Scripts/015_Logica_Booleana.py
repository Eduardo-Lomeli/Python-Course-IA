
#Operador 	Descripción
#== 	Igual que
#!= 	Diferente que
#< 	Menor que
#> 	Mayor que
#<= 	Menor o igual que
#>= 	Mayor o igual que

a = 10
b = 15
comparacion = a == b

print(comparacion)

a = 10
b = 10
comparacion = a == b

print(comparacion)

a = 10
b = 15
comparacion = a != b

print(comparacion)

a = 10
b = 15
comparacion = a > b

print(comparacion)


a = 10
b = 15
comparacion = a < b

print(comparacion)

a = 10
b = 10
comparacion = a >= b

print(comparacion)

a = 10
b = 15
comparacion = a <= b

print(comparacion)

a = 15
b = 17
c = 13

# Comparaciones
comparacion_1 = a < b and b > c
comparacion_2 = a > b and b > c

# Comprobamos los resultados
print(comparacion_1)
print(comparacion_2)


a = 15
b = 17
c = 13

# Comparaciones
comparacion_1 = a < b or b > c
comparacion_2 = a == b or b < c

# Comprobamos los resultados
print(comparacion_1)
print(comparacion_2)

a = 5
b = 3

# Comparación
comparacion = a == b

# Comprobamos los resultados
print(comparacion)

print(not (10 > 7 and (10 == 11 or 11 != 10)))