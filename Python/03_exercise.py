### Analisi de ventas

ventas_2022 = float(input("Ingrese la cantidad de ventas en 2022: "))
ventas_2023 = float(input("Ingrese la cantidad de ventas en 2023: "))

if ventas_2022 == 0:
    print("No se puede calcular variación con ventas cero en 2022")
    exit()

variacion = ((ventas_2023 - ventas_2022) / ventas_2022) * 100

print(f"\nVariación porcentual: {variacion:.2f}%")

if variacion > 20:
    print("Recomendación: bonificación para el equipo de ventas")
elif 2 <= variacion <= 20:
    print("Recomendación: pequeña bonificación para el equipo de ventas")
elif -10 <= variacion < 2:
    print("Recomendación: planificación de políticas de incentivo a las ventas")
else:
    print("Recomendación: recorte de gastos")