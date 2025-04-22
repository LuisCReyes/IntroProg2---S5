#Calculo del consumo de agua 

total_litros = float(input("Ingrese el total de litros consumidos en un mes en una vivienda: "))
personas = int(input("Ingresar la cantidad de personas que viven en una vivienda: "))

consumo_mensual_por_persona = total_litros / personas
consumo_diario_por_persona = consumo_mensual_por_persona / 30

print("-" * 40)

print(f"""Consumo total por mes: {total_litros}
Camtidad de personas en la vivienda: {personas}
Consumo mensual por persona: {consumo_mensual_por_persona:.2f}
Consumo diario por persona: {consumo_diario_por_persona:.2f}""")

print("-" * 40)