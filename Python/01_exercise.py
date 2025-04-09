### ejercicios alura latam

# Ejercicio 1

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

if num1 > num2:
    print(f"El número mayor es: {num1}")
elif num2 > num1:
    print(f"El número mayor es: {num2}")
else:
    print("Los números son iguales")

### Ejercicio crecimiento de produccion

porcentaje = float(input("Ingrese el porcentaje de crecimiento de produc.: "))

if porcentaje > 0:
    print("Hubo crecimiento (porcentaje positivo)")
elif porcentaje < 0:
    print("Hubo decrecimiento (porcentaje negativo)")
else:
    print("No hubo crecimiento (porcentaje cero)")

### Ejercicio 3

letra = input("Ingrese una letra: ").lower()
if letra in["a", "e", "i", "o", "u"]:
    print("La letra es una vocal")
elif letra.isalpha():
    print("La letra es una consonante")
else:
    print("No es una letra válida")

### Ejercicio 4 precio automoviles

precio1 = float(input("Ingrese el precio del primer automóvil: "))
precio2 = float(input("Ingrese el precio del segundo automóvil: "))
precio3 = float(input("Ingrese el precio del tercer automóvil: "))
precio4 = float(input("Ingrese el precio del cuarto automóvil: "))

maximo = max(precio1, precio2, precio3, precio4)
minimo = min(precio1, precio2, precio3, precio4)

print(f"El precio máximo es: {maximo}")
print(f"El precio mínimo es: {minimo}")

### Ejercicio 5 producto mas barato
precio1 = float(input("Ingrese el precio promedio primer año: "))
precio2 = float(input("Ingrese el precio promedio segundo año: "))
precio3 = float(input("Ingrese el precio promedio tercer año: "))

mas_barato = min(precio1, precio2, precio3)

print(f"El precio más barato es: {mas_barato}")

### Ejercicio 6 Orden Desendente

num4 = int(input("Ingrese el primer número: "))
num5 = int(input("Ingrese el segundo número: "))
num6 = int(input("Ingrese el tercer número: "))

numeros = [num4, num5, num6]
numeros_ordenados = sorted(numeros, reverse=True)

print("Los números en orden descendente son:", numeros_ordenados)

### Ejercicio 7 Saludos por turno

turno = input("Ingrese el turno estudias? (mañana, tarde, noche): ").lower()

if turno == "mañana":
    print("¡Buenos dias!")
elif turno == "tarde":
    print("¡Buenas tardes!")
elif turno == "noche":
    print("¡Buenas noches!")
else:
    print("Turno no válido")
    
### Ejercicio 8 par o impar
numero = int(input("Ingrese un número: "))
if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
    
### Ejercicio 9 entero o decimal
numero = input("Ingrese un número: ")
if numero.isdigit():
    print("El número es entero")
else:
    print("El número es decimal")

