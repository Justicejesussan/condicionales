"""
condiciones if
    Evaluan expresiones booleanas

Estructura:
    if expresion:
        instrucciones
    
    if expresion:
        instrucciones
    else:
        instrucciones

    if expresiones:
        instrucciones
    elif expresion:
        instrucciones
    else:
        instrucciones
"""

print("programa que verifica si un numero es positivo")
num = int(input("ingresa un numero: "))
if num > 0:
    print("el numero es positivo")
else:
    print("el numero es negativo")
print("fin del programa")

print("programa que verifica si un numero es par")
num = int(input("ingresa un numero: "))
if num % 2 == 0:
    print("es un numero par")
else:
    print("es un numero impar")
print("fin del programa")