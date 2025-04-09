### operacion  con numeros

num10 = float(input("ingrese el primer numero: "))
num20 = float(input("ingrese el segundo numero: "))
operation = input("Que operacion realizaras? (+, -, *, /): ")

if operation == "+":
    result = num10 + num20
elif operation == "-":
    result = num10 - num20
elif operation == "*":
    result = num10 * num20
elif operation == "/":
    if num20 != 0:
        result = num10 / num20
    else:
        print("Error: Division por cero")
        exit()
else:
    print("Error: Operacion no valida")
    exit()

### Determinar caracteristicas del resultado
print(f"\El resultado es: {result}")

## par o  impar

if result == int(result):
    if int(result) % 2 == 0:
        print("Es un número par")
    else:
        print("Es un número impar")
else:
    print("No es un número entero (no se puede determinar par/impar)")

# Positivo o negativo
if result > 0:
    print("Es positivo")
elif result < 0:
    print("Es negativo")
else:
    print("Es cero")

# Entero o decimal
if result == int(result):
    print("Es un número entero")
else:
    print("Es un número decimal")