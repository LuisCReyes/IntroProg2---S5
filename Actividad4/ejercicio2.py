import datetime as dt

fecha_ingreso = input("Fecha ingreso YYYY-MM-DD")
fecha_ingreso = dt.datetime.strptime(fecha_ingreso, "%Y-%M-%d")

fecha_actual = dt.datetime.now()
dias = (fecha_actual - fecha_ingreso).days
print(fecha_actual)
print(fecha_ingreso)
print("días ",dias)

if dias > 30:
    print("Cuenta inactiva")