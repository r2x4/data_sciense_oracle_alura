### Ejercicio 6: Promedio de temperaturas

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
