# 4
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("Suma:", a + b)

# 5
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))
print("Suma:", a + b + c)

# 6
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("Resta:", a - b)

# 7
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
print("Multiplicación:", a * b)

# 8
a = float(input("Ingresa el numerador: "))
b = float(input("Ingresa el denominador: "))
if b != 0:
    print("División:", a / b)
else:
    print("Error: el denominador no puede ser 0.")

# 9
base = float(input("Ingresa la base: "))
exponente = float(input("Ingresa el exponente: "))
print("Potencia:", base ** exponente)

# 10
a = int(input("Ingresa el numerador: "))
b = int(input("Ingresa el denominador: "))
if b != 0:
    print("División entera:", a // b)
else:
    print("Error: el denominador no puede ser 0.")

# 11
a = int(input("Ingresa el numerador: "))
b = int(input("Ingresa el denominador: "))
if b != 0:
    print("Resto de la división:", a % b)
else:
    print("Error: el denominador no puede ser 0.")

# 12
nota1 = float(input("Ingresa la primera nota: "))
nota2 = float(input("Ingresa la segunda nota: "))
nota3 = float(input("Ingresa la tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print("Promedio:", promedio)

# 13
prom_ponderado = (5*1 + 12*2 + 20*3 + 15*4) / (1+2+3+4)
print("Promedio ponderado:", prom_ponderado)
