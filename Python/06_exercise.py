# Ejercicio 6: Promedio de temperaturas

suma = 0
contador = 0

print("Ingrese temperaturas en °C (escriba -273 para finalizar):")

while True:
    temp = float(input("Temperatura: "))
    if temp == -273:
        break
    suma += temp
    contador += 1

if contador > 0:
    promedio = suma / contador
    print(f"\nTemperaturas registradas: {contador}")
    print(f"Promedio: {promedio:.2f}°C")
else:
    print("\nNo se ingresaron temperaturas válidas.")

# Ejercicio 7: factorial

# Solicitar un número al usuario
numero = int(input("Ingrese un número para calcular su factorial: "))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

###  ejercicio 6 tablas de multiplicar

numero = int(input("Ingrese un número entero tu tabla de multiplicar (1 al 10): "))

if 1 <= numero <= 10:
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número fuera del rango. Por favor, ingrese un número del 1 al 10.")

