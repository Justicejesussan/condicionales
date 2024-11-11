numero_dado = int(input("Introduce el número obtenido al lanzar el dado (1-6): "))

if numero_dado == 1:
    print("La cara opuesta es 6.")
elif numero_dado == 2:
    print("La cara opuesta es 5.")
elif numero_dado == 3:
    print("La cara opuesta es 4.")
elif numero_dado == 4:
    print("La cara opuesta es 3.")
elif numero_dado == 5:
    print("La cara opuesta es 2.")
elif numero_dado == 6:
    print("La cara opuesta es 1.")
else:
    print("ERROR: número incorrecto.")