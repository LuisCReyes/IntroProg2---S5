calificacion_est = float(input("Ingrese la calificación del estudiante (0-10) : "))

if calificacion_est >= 9 and calificacion_est <= 10:
    print("La calificación es A")
elif calificacion_est >=7 and calificacion_est <=8:
    print("La calificación es B")
elif calificacion_est >= 5 and calificacion_est <= 6:
    print("La calificación es C")
elif calificacion_est >= 3 and calificacion_est <= 4:
    print("La calificación es D")
elif calificacion_est >= 0 and calificacion_est <= 2:
    print("La calificación es F")
else:
    print("Error. La calificación no es válida.")