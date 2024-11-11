numerador = float(input("Introduce el numerador: "))
denominador = float(input("Introduce el denominador: "))

if denominador != 0:
    division = numerador / denominador
    print(f"La división es: {division}")
else:
    print("Error: No se puede dividir entre cero.")

