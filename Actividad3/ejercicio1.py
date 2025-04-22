calificacion1 = int(input("ingrese la calificación 1: "))
calificacion2 = int(input("ingrese la calificación 2: "))
calificacion3 = int(input("ingrese la calificación 3: "))

suma = calificacion1 + calificacion2 + calificacion3
promedio = suma / 3

print("-"* 25)

print(f"""Calificación 1: {calificacion1:>3}
Calificación 2: {calificacion2:>3}
Calificación 3: {calificacion3:>3}
{"Promedio: ":<15} {promedio:>3.0f} """)

print("-" * 25)