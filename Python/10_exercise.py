### ejercicio 10
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
         "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

temperaturas = []
for mes in meses:
    temp = float(input(f"Ingrese la temperatura media de {mes}: "))
    temperaturas.append(temp)

promedio_anual = sum(temperaturas) / len(temperaturas)
print(f"\nTemperatura media anual: {promedio_anual:.2f}°C")
print("\nMeses con temperatura por encima del promedio:")

for i in range(len(temperaturas)):
    if temperaturas[i] > promedio_anual:
        print(f"{meses[i]}: {temperaturas[i]}°C")
        
### ejercicio 11

ventas = {
    'Producto A': 300,
    'Producto B': 80,
    'Producto C': 60,
    'Producto D': 200,
    'Producto E': 250,
    'Producto F': 30
}

total_ventas = sum(ventas.values())
producto_mas_vendido = max(ventas, key=ventas.get)

print(f"Total de ventas: {total_ventas}")
print(f"Producto más vendido: {producto_mas_vendido} con {ventas[producto_mas_vendido]} ventas")
print("Productos vendidos:")
for producto, cantidad in ventas.items():
    print(f"{producto}: {cantidad} unidades")

### ejercicio 12

votos = {
    "Diseño 1": 1334,
    "Diseño 2": 982,
    "Diseño 3": 1751,
    "Diseño 4": 210,
    "Diseño 5": 1811
}

total_votos = sum(votos.values())
ganador = max(votos, key=votos.get)
porcentaje_ganador = (votos[ganador] / total_votos) * 100

print(f"Diseño ganador: {ganador} con {votos[ganador]} votos")
print(f"Porcentaje de votos: {porcentaje_ganador:.2f}%")
print("Resultados de la votación:")
for diseño, cantidad in votos.items():
    porcentaje = (cantidad / total_votos) * 100
    print(f"{diseño}: {cantidad} votos ({porcentaje:.2f}%)")

### ejercicio 13
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
bonificaciones = {}
total_gasto = 0
minima = 0
bonificacion_maxima = 0

for salario in salarios:
    bonificacion = max(salario * 0.10, 200)
    bonificaciones[salario] = bonificacion
    total_gasto += bonificacion
    if bonificacion == 200:
        minima += 1
    if bonificacion > bonificacion_maxima:
        bonificacion_maxima = bonificacion

print(f"Gasto total en bonificaciones: {total_gasto:.2f}")
print(f"Empleados con bonificación mínima: {minima}")
print(f"Bonificación más alta: {bonificacion_maxima:.2f}")

### ejercicio 14
diversidad = {
    'Área Norte': [2819, 7236],
    'Área Leste': [1440, 9492],
    'Área Sul': [5969, 7496],
    'Área Oeste': [14446, 49688],
    'Área Centro': [22558, 45148]
}

promedios = {}
mayor_diversidad = ''
mayor_promedio = 0

for area, especies in diversidad.items():
    promedio = sum(especies) / len(especies)
    promedios[area] = promedio
    if promedio > mayor_promedio:
        mayor_promedio = promedio
        mayor_diversidad = area

print("Promedio de especies por área:")
for area, promedio in promedios.items():
    print(f"{area}: {promedio:.2f}")

print(f"\nÁrea con mayor diversidad biológica: {mayor_diversidad} con promedio {mayor_promedio:.2f}")

### ejercicio 15

sectores = {
    'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
    'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
    'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
    'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]
}

suma_total = 0
total_personas = 0
media_sector = {}

for sector, edades in sectores.items():
    media = sum(edades) / len(edades)
    media_sector[sector] = media
    suma_total += sum(edades)
    total_personas += len(edades)

media_general = suma_total / total_personas
mayores = 0

for edades in sectores.values():
    for edad in edades:
        if edad > media_general:
            mayores += 1

print("Media de edad por sector:")
for sector, media in media_sector.items():
    print(f"{sector}: {media:.2f} años")

print(f"\nMedia general de edad: {media_general:.2f} años")
print(f"Personas por encima de la media general: {mayores}")
