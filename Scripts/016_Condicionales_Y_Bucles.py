x = 5

if x > 0:
    print("x es positivo")


x = 5
if x > 0:
    print("x es positivo")

for i in range(1, 11):
print(i)


a = 3

if a == 10:
    print("Se ejecuta el código del if.")
    print("Esto también es código del bloque if")

print("Este print está fuera del if.")

# Se guarda una edad
edad = 25

# Evaluamos si es mayor de edad
if edad >= 18:
    print("Es mayor de edad.")


    # Se guarda una edad
edad = 16

# Evaluamos si es mayor de edad
if edad >= 18:
    print("Es mayor de edad.")
else:
    print("Es menor de edad.")


    edad = int(input("Introduzca su edad: "))

resultado = "Es usted mayor de edad" if edad >= 18 else "Es usted menor de edad"

print(resultado)



codigo = int(input("Introduzca un código HTTP: "))

match codigo:
    case 100 | 101 | 102:
        print("Código de tipo informativo.")
    case 200 | 201 | 202 | 203:
        print("Código de éxito")
    case 300 | 301 | 302 | 303:
        print("Código de redirección.")
    case 400 | 404 | 407:
        print("Código de error en el cliente.")
    case 500 | 502 | 599:
        print("Código de error en el servidor.")
    case _:
        print("Código no disponible.")



if codigo == "200":
    print("Todo ok.")
elif codigo == "301":
    print("Movimiento permanente de la página.")
elif codigo == "302":
    print("Movimiento temporal de la página.")
elif codigo == "404":
    print("Página no encontrada.")
elif codigo == "500":
    print("Error interno del servidor.")
elif codigo == "503":
    print("Servicio no disponible.")
else:
    print("Código no disponible.")



for i in range(5):
    print("Soy una frase repetitiva.")