num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
num3 = int(input("Introduce el tercer número: "))
numeros = [num1, num2, num3]
numeros.sort(reverse=True)
print("Los números ordenados de mayor a menor son:", numeros)