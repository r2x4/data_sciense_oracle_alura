### ejercicio 5 numeros primos

num1= 1
num2= int(input("Introduce un numero: "))
primos = []
for i in range(num1, num2 + 1):
    if i > 1:
        for j in range(2, i):
            if (i % j) == 0:
                break
        else:
            primos.append(i)
print(f"Los numeros primos entre {num1} y {num2} son: {primos}")

### ejercicio 6 fecha especifica dia mes año
from datetime import datetime
fecha = input("Introduce una fecha (dd/mm/yyyy): ")
try:
    fecha = datetime.strptime(fecha, "%d/%m/%Y")
    dia = fecha.day
    mes = fecha.month
    año = fecha.year
    print(f"Fecha válida para análisis.")
    print(f"Dia: {dia}, Mes: {mes}, Año: {año}")
except ValueError:
    print("Formato de fecha incorrecto. Por favor, usa dd/mm/yyyy.")
    
### ejercicio 7

colonia_bacterias = [1.2, 2.1, 3.3, 5.0, 7.8, 11.3, 16.6, 25.1, 37.8, 56.9]

crecimientos = []  

for i in range(1, len(colonia_bacterias)): # rrs olvida el len que recorre ojo
    muestra_anterior = colonia_bacterias[i - 1]
    muestra_actual = colonia_bacterias[i]
    porcentaje_crecimiento = 100 * (muestra_actual - muestra_anterior) / muestra_anterior
    crecimientos.append(porcentaje_crecimiento)

# van los resultados
for dia, crecimiento in enumerate(crecimientos, start=1):
    print(f"Día {dia}: crecimiento de {crecimiento:.2f}%")

# tipo lista completo pais
print("\nLista de porcentajes de crecimiento diario:", [f"{c:.2f}%" for c in crecimientos])
