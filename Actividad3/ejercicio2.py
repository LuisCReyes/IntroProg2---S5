cantidad_inicial = int(input("Ingrese la cantidad inicial en inventario: "))
productos_recibidos = int(input("Ingrese la cantidad de productos recibidos: "))
productos_vendidos = int(input("Ingrese la cantidad de productos vendidos: "))
suma = productos_recibidos + cantidad_inicial
inventario_actual = suma - productos_vendidos

print("-" * 45)

print(f"{"Inventario inicial:":<20} {cantidad_inicial:>20}")
print(f"{"Productos recibidos:":<20} {productos_recibidos:>20}")
print(f"{"Productos vendidos:":<20} {productos_vendidos:>20}")
print(f"{"Inventario final:":<20} {inventario_actual:>20}")

print ("-" * 45)