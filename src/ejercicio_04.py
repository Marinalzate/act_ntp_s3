suma = 0
num = int(input("Ingresa un numero (0 para terminar): "))

while num != 0:
    suma += num
    num = int(input("Ingresa un numero (0 para terminar): "))

print("La suma total de los numeros ingresados es:", suma)    