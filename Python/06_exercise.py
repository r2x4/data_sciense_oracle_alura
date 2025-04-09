# Ejercicio 4: Promedio de temperaturas

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

# Ejercicio 5: factorial

# Solicitar un número al usuario
numero = int(input("Ingrese un número para calcular su factorial: "))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


resultado = factorial(numero)
print(f"El factorial de {numero} es: {resultado}")

# ejercicio 6 tablas de multiplicar

numero = int(
    input("Ingrese un número entero tu tabla de multiplicar (1 al 10): "))

if 1 <= numero <= 10:
    print(f"\nTabla de multiplicar del {numero}:\n")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
else:
    print("Número fuera del rango. Por favor, ingrese un número del 1 al 10.")


# Ejercicio 7: números primos


numero = int(input("Ingrese un número entero: "))

if numero <= 1:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")


# Ejercicio 8: distribución de edades
rango1 = 0   # 0 - 25
rango2 = 0   # 26 - 50
rango3 = 0   # 51 - 75
rango4 = 0   # 76 - 100

print("Ingrese edades de clientes (número negativo para finalizar):")

while True:
    edad = int(input("Edad: "))
    if edad < 0:
        break
    elif 0 <= edad <= 25:
        rango1 += 1
    elif 26 <= edad <= 50:
        rango2 += 1
    elif 51 <= edad <= 75:
        rango3 += 1
    elif 76 <= edad <= 100:
        rango4 += 1

print("\nDistribución de edades:")
print(f"[0-25]   : {rango1}")
print(f"[26-50]  : {rango2}")
print(f"[51-75]  : {rango3}")
print(f"[76-100] : {rango4}")


# Ejercicio 9: votación
candidato1 = 0
candidato2 = 0
candidato3 = 0
candidato4 = 0
nulos = 0
blancos = 0

print("Votación (20 empleados):")
print("1-4: Candidatos\n5: Nulo\n6: Blanco")

for i in range(1, 21):
    voto = int(input(f"Voto del empleado #{i}: "))
    if voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1
    elif voto == 4:
        candidato4 += 1
    elif voto == 5:
        nulos += 1
    elif voto == 6:
        blancos += 1
    else:
        print("Voto inválido. Se contará como nulo.")
        nulos += 1

total_votos = candidato1 + candidato2 + \
    candidato3 + candidato4 + nulos + blancos

print("\nResultados:")
print(f"Candidato 1: {candidato1} votos")
print(f"Candidato 2: {candidato2} votos")
print(f"Candidato 3: {candidato3} votos")
print(f"Candidato 4: {candidato4} votos")
print(f"Votos nulos: {nulos}")
print(f"Votos en blanco: {blancos}")
print(f"Porcentaje de nulos: {(nulos / total_votos) * 100:.2f}%")
print(f"Porcentaje de blancos: {(blancos / total_votos) * 100:.2f}%")
