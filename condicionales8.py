nota = int(input("Ingresa la nota: "))
edad = int(input("Ingresa la edad: "))
sexo = input("Ingresa el sexo (F/M): ").upper()
if nota >= 5 and edad >= 18:
    if sexo == 'F':
        print("ACEPTADA")
    elif sexo == 'M':
        print("POSIBLE")
    else:
        print("NO ACEPTADA")
else:
    print("NO ACEPTADA")