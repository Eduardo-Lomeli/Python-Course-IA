#Mutabilidad

#Los objetos mutables (cambiantes) son aquellos cuyos valores internos pueden ser modificados después de su creación. 


lista = [10, 10, 30, 40]

# Reasigna el valor 20 a la posición 1 de la lista
lista[1] = 20

print(lista)

#Inmutabilidad

#Los objetos inmutables (no cambiantes) son aquellos cuyos valores internos no pueden ser modificados después de su creación. 

tupla = (10, 10, 30, 40)

# Intenta reasignar el valor 20 a la posición 1 de la tupla
tupla[1] = 20
print(tupla)

#Hashabilidad

#Para que un objeto sea hashable, debe ser inmutable, tener un valor de hash constante en tiempo de ejecución y que sea comparable con otros objetos de su tipo para determinar si son iguales. 

saludo = "Hola"

# Imprime el hash del objeto
print(hash(saludo))


#Iterabilidad

#La iterabilidad es la capacidad de un objeto en ser recorrido con posiciones de índice. Por ejemplo, una lista, una tupla o una cadena, son objetos iterables, porque tienen índice de posición. 

numeros = [10, 20, 30]

# Imprime la posición 0 de la lista
print(numeros[0])