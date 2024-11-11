base = float(input("Ingresa la base: "))
exponente = int(input("Inngresa el exponente: "))
if exponente > 0:
    resultado = base ** exponente
    print(f"La potencia de {base} elevado a {exponente} es: {resultado}")
elif exponente == 0:
    print("Cualquier número elevado a 0 es 1.")
else:  
    resultado = 1 / (base ** abs(exponente))
    print(f"La potencia de {base} elevado a {exponente} es: {resultado}")