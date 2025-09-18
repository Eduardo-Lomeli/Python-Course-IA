#La sintaxis de una tupla es muy parecida a la de una lista. La única diferencia que hay, es que se escriben con paréntesis (), en lugar de con corchetes. 

tupla_colores = ("rojo", "verde", "azul")

# Se imprime toda la tupla
print(tupla_colores)

tupla_colores = ("rojo", "verde", "azul")

# Se imprime la posición 2 del índice
print(tupla_colores[2])

tupla_colores = ("rojo", "verde", "azul")

# Se busca la posición de índice de un elemento
print(tupla_colores.index("rojo"))

tupla_colores = ("rojo", "verde", "azul", "rojo", "amarillo")

# Se cuentan las veces que está el elemento
print(tupla_colores.count("rojo"))

# Tupla para desempaquetar
numeros = (10, 20, 30, 40)

# Desempaquetado en variables
numero_1, numero_2, numero_3, numero_4, = numeros

# Comprobamos el resultado
print(numero_1)
print(numero_2)
print(numero_3)
print(numero_4)

# Tupla con varios valores
numeros = (10, 20, 30, 40)

# Desempaquetado con una variable para capturar el exceso de valores
numero_1, numero_2, *resto = numeros

# Resultado
print(numero_1)
print(numero_2)
print(resto)