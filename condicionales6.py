cadena = input("Introduce una letra: ")


if len(cadena) == 1 and cadena.isupper():
    print("La letra es mayúscula.")
else:
    print("La letra no es mayúscula o la entrada no es válida.")