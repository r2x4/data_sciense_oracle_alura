### ejercicio 8

ids = []

for i in range(10):
    id_productos = int(input(f'ingresa el ID del producto {i+1}:'))
    ids.append(id_productos)
    
dulces = 0
amargos = 0

for id in ids:
    if id % 2 == 0:
        dulces += 1
    else:
        amargos += 1
        
print(f"\nTotal de productos ingresados: {len(ids)}")
print(f"Productos dulces (ID par): {dulces}")
print(f"Productos amargos (ID impar): {amargos}")

### ejercicio 9 

# Clave de respuestas correctas
respuestas_correctas = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']

# Respuestas dadas por el estudiante (las que escribiste)
respuestas_estudiante = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']

# Contador de aciertos
puntos = 0

print("Resultado del examen:\n")

for i, (correcta, estudiante) in enumerate(zip(respuestas_correctas, respuestas_estudiante), start=1):
    RESULTADO = "Correcta" if estudiante == correcta else "Incorrecta"
    print(f"{i:02} - Estudiante: {estudiante} | Correcta: {correcta} --> {RESULTADO}")

    if estudiante == correcta:
        puntos += 1

print(f"\nPuntuación final: {puntos} de {len(respuestas_correctas)}")

