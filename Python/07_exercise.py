### ejercicio 1

lista = [2172.54, 3701.35, 3518.09, 3456.61, 3249.38, 2840.82, 3891.45, 3075.26, 2317.64, 3219.08]

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)
print(promedio(lista))

### ejercicio 2

total_compras = len(lista)
compras_mayores = 0

for i in lista:
    if i > 3000:
        compras_mayores += 1

porcentaje_mayores = (compras_mayores / total_compras) * 100

print(f"Total de compras: {total_compras}")
print(f"Compras mayores a 3000: {compras_mayores}")
print(f"Porcentaje de compras mayores a 3000: {porcentaje_mayores:.2f}%")

### ejercicio 3

numero = []
for i in range(5):
    num = (float(input(f"Ingrese el número {i}: ")))
    numero.append(num)
print("Los números ingresados son:", numero)

### ejercicio 4 al reves
def al_reves(lista):
    lista_reversa = []
    for i in range(len(lista)-1, -1, -1):
        lista_reversa.append(lista[i])
    return lista_reversa
print("los Numero ingresados inverso: ", al_reves(numero))