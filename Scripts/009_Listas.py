camiseta = ["rojo", "L", 100, 10]

colores = ["azul", "verde", "rojo"]

# Reasigna el valor a la posición 0 de la lista
colores[0] = "amarillo"

# Imprime el resultado
print(colores)

colores = ["azul", "verde", "rojo"]

# Añade el elemento "amarillo" al final de la lista
colores.append("amarillo")

print(colores)

colores = ["azul", "verde", "rojo"]

# Se añade el elemento "amarillo" en la posición 0 del índice
colores.insert(0, "amarillo")

print(colores)


colores1 = ["azul", "verde", "rojo"]
colores2 = ["amarillo", "naranja", "marrón"]

# Extiende la lista
colores1.extend(colores2)

print(colores1)

colores1 = ["azul", "verde", "rojo"]
colores2 = ["amarillo", "naranja", "marrón"]

# Concatena las listas
colores1 = colores1 + colores2

print(colores1)

colores = ["azul", "verde", "rojo"]

# Se elimina el último elemento de la lista
colores.pop()

print(colores)

colores = ["azul", "verde", "rojo"]

# Elimina el elemento de la posición 0
colores.pop(0)

print(colores)

colores = ["azul", "verde", "rojo"]

# Elimina el elemento "rojo"
colores.remove("rojo")

print(colores)


numeros = [87, 10, 5, 7, 378, 10, 10, 65, 10]

# Guardamos lo que devuelve index() en una variable
busca_numero = numeros.index(10)

print(busca_numero)




numeros = [87, 10, 5, 7, 378, 10, 10, 65, 10]

# Especificamos un valor de búsqueda
valor_busqueda = 10

# Buscamos el total de coincidencias
coincidencias = numeros.count(valor_busqueda)

print(f"En total, el valor de búsqueda {valor_busqueda}, tiene {coincidencias} coincidencias.")