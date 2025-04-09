### ejercicio 8

ids = []

for i in range(10):
    id_productos = int(input(f'ingresa el ID del producto {i+1}'))
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