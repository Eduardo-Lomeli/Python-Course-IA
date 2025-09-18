numero_1 = 10
numero_2 = 20.5

print(numero_1 + numero_2)

numero = 100.43

numero_entero = int(numero) # Se convierte en int

print(numero)
print(numero_entero)

numero_1 = input("Introduzca el primer número: ")
numero_2 = input("Introduzca el segundo número: ")

suma = numero_1 + numero_2

print(f"El resultado de la suma es: {suma}.")


numero_1 = input("Introduzca el primer número: ")
numero_2 = input("Introduzca el segundo número: ")

numero_1 = int(numero_1)
numero_2 = int(numero_2)

suma = numero_1 + numero_2

print(f"Tipo de numero_1: {type(numero_1)}")
print(f"Tipo de numero_2: {type(numero_2)}")
print(f"Tipo de suma: {type(suma)}")
print("\n")
print(f"El resultado de la suma es: {suma}.")


numero_1 = float(input("Introduzca el primer número: "))
numero_2 = float(input("Introduzca el segundo número: "))

suma = numero_1 + numero_2

print(f"Número 1: {numero_1}")
print(f"Número 2: {numero_2}")
print(f"El resultado de la suma es: {suma}.")


saludo = "Hola"

# Convierte el valor a bool
booleano = bool(saludo)

print(booleano)	

numero = 1000

# Convierte el valor int a str
cadena = str(numero)

print(type(cadena))

decimal = 1000

# Se convierte el decimal en hexadecimal
hexadecimal = hex(decimal)

print(hexadecimal)