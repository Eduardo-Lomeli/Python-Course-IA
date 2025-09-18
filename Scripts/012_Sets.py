set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}

print(set_colores)

# Añade un elemento al set
set_colores.add("marrón")

print(set_colores)

# Se elimina un valor del set
set_colores.remove("azul")

print(set_colores)


# Se elimina un valor del set
set_colores.discard("cian")

print(set_colores)

set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}

# Se cuentan los elementos
cantidad_elementos = len(set_colores)

print(f"El objeto tiene {cantidad_elementos} elementos.")


set_colores = {100, 6578, 54, 4, 56, 2}

# Se busca el valor más bajo del conjunto
valor_minimo = min(set_colores)

print(f"El valor mínimo del conjunto es: {valor_minimo}")


set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}

# Se busca el color más "pequeño" alfabéticamente
color = min(set_colores)

print(color)

set_colores = {"rojo", "verde", "azul", "amarillo", "naranja", "negro", "rosa"}

# Se busca el color más "grande" alfabéticamente
color = max(set_colores)

print(color)

numeros = frozenset([1, 2, 3, 4, 5])

print(numeros)