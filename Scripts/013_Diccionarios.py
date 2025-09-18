camiseta = {
"color" : "rojo",
"talla" : "L",
"precio" : 100,
"unidades" : 10
}

# Obtiene el valor asociado a la clave "color"
dato_obtenido = camiseta["color"]

# Vemos el resultado
print(dato_obtenido)

camiseta = {
"color" : "rojo",
"talla" : "L",
"precio" : 100,
"unidades" : 10
}

# Comprobamos el stock
print(f"Hay {camiseta['unidades']} unidades en el almacén.")

# Se modifica el valor de "unidades"
camiseta['unidades'] = 25

# Comprobamos el stock de nuevo
print(f"Hay {camiseta['unidades']} unidades en el almacén.")