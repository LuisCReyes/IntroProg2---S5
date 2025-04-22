# Calculo del consumo de combustible

distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
litros_consumidos = float(input("Ingrese la cantidad de litros consumidos: "))
rendimiento = distancia / litros_consumidos
precio_litro = 48.97
gasto_total_combustible = litros_consumidos * precio_litro

print("*" * 50)

print(f"""
{"Distancia recorrida: ":<30} {distancia:>10} Km
{"Litros (L) consumidos: ":<30} {litros_consumidos:>10} L
{"Precio por litro: ":<30} {precio_litro:>10} C$
{"Rendimiento del vehículo: ":<30} {rendimiento:>10.2f} Km/L
{"Gasto total del combustible: ":<30} {gasto_total_combustible:>10.2f} C$
""")

print("*" * 50)