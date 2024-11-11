duracion_llamada = int(input("Introduce la duración de la llamada en minutos: "))
dia_semana = int(input("Introduce el día de la semana (1 = lunes, 7 = domingo): "))
turno = input("Introduce el turno (mañana/tarde): ").lower()


if duracion_llamada <= 5:
    costo_llamada = 1
elif duracion_llamada <= 8:
    costo_llamada = 1 + (duracion_llamada - 5) * 0.80
elif duracion_llamada <= 10:
    costo_llamada = 1 + 3 * 0.80 + (duracion_llamada - 8) * 0.70
else:
    costo_llamada = 1 + 3 * 0.80 + 2 * 0.70 + (duracion_llamada - 10) * 0.50

if dia_semana == 7:
    costo_llamada *= 1.03
elif turno == "mañana":
    costo_llamada *= 1.15
elif turno == "tarde":
    costo_llamada *= 1.10

print(f"El costo de la llamada es: {costo_llamada:.2f} euros.")