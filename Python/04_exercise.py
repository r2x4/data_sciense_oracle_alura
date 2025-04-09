### EJERCICIO 12

tipo = input("Ingrese el tipo de combustible (E para etanol, D para diésel): ").upper()
litros = float(input("Ingrese la cantidad de litros vendidos: "))

PRECIO_ETANOL = 150000
PRECIO_DIESEL = 180000

if tipo == 'E':
    precio = PRECIO_ETANOL
    if litros <= 15:
        descuento = 0.02
    else:
        descuento = 0.04
elif tipo == 'D':
    precio = PRECIO_DIESEL
    if litros <= 15:
        descuento = 0.03
    else:
        descuento = 0.05
else:
    print("Tipo de combustible no válido")
    exit()

valor_descuento = precio * litros * descuento
valor_a_pagar = (precio * litros) - valor_descuento

print(f"\nValor sin descuento: R$ {precio * litros:.2f}")
print(f"Descuento aplicado: {descuento * 100}%")
print(f"Valor del descuento: R$ {valor_descuento:.2f}")
print(f"Valor a pagar: R$ {valor_a_pagar:.2f}")