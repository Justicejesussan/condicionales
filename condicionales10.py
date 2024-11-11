num_alumnos = int(input("Introduce el número de alumnos: "))

if num_alumnos >= 100:
    costo_por_alumno = 65
elif num_alumnos >= 50:
    costo_por_alumno = 70
elif num_alumnos >= 30:
    costo_por_alumno = 95
else:
    costo_por_alumno = 4000

if num_alumnos < 30:
    print(f"El costo de la renta del autobús es de 4000 euros.")
else:

    total_pago_alumnos = costo_por_alumno * num_alumnos

    total_pago_compania = costo_por_alumno * num_alumnos

    print(f"El costo por alumno es {costo_por_alumno} euros.")
    print(f"El total que deben pagar los alumnos es {total_pago_alumnos} euros.")
    print(f"El total que debe pagar la compañía de autobuses es {total_pago_compania} euros.")