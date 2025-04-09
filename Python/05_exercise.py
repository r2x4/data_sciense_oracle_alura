# escribe un programa que solicite dos numeros enteros  e imprima todos los enteros entre ellos

numero1 = int(input("Ingrese el primer número entero: "))
numero2 = int(input("Ingrese el segundo número entero: "))

inicio = min(numero1, numero2)
fin = max(numero1, numero2)

if fin - inicio <= 1:
    print("No hay enteros entre los números ingresados.")
else:
    print("Los enteros entre", inicio, "y", fin, "son:")
    for i in range(inicio + 1, fin):
        print(i)


# ejercicio 2

bacteria_a = 4
bacteria_b = 10
tasa_a = 0.03
tasa_b = 0.015
dias = 0

while bacteria_a < bacteria_b:
    bacteria_a += bacteria_a * tasa_a
    bacteria_b += bacteria_b * tasa_b
    dias += 1
print(f"Las bacterias A alcanzan a las bacterias B en {dias} días.")
print("Población A:", round(bacteria_a, 2))
print("Población B:", round(bacteria_b, 2))

# 3 ejercicio

contador = 0

while contador < 15:
    calificacion = int(input(f"Ingrese la calificación #{contador + 1} (0 a 5): "))
    if 0 <= calificacion <= 5:
        print("Calificación válida.")
        contador += 1
    else:
        print("Calificación inválida. Debe estar entre 0 y 5.")


