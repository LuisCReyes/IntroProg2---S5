# Calculo interés compuesto

capital_inicial =  float(input("Ingrese su capital actuaL: "))
tasa_interes = float(input("Ingrese la tasa de interés anual (porcentaje):"))
cantidad_annios = int(input("Ingrese la cantidad de años: "))

tasa_porcentual_interes = tasa_interes / 100
interes_compuesto = (1 + tasa_porcentual_interes) ** cantidad_annios
monto_final = capital_inicial * interes_compuesto
interes_obtenido = monto_final - capital_inicial

print("+" * 29)

print(f""" Capital inicial: {capital_inicial:.2f}
{"Tasa:":>17} {tasa_interes:.2f}
{"Cantidad de años:":>17} {cantidad_annios}
{"Monto final:":>17} {monto_final:.2f} 
{"Interes ganado:":>17} {interes_obtenido:.2f}""")

print("+" * 29)