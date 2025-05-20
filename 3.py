calificaciones = []
for i in range(8):
    calificacion = float(input(f"Ingrese la calificación {i+1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)
print("Promedio de calificaciones:", promedio)
