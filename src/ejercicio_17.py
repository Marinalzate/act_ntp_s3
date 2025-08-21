num = int(input("Ingresa un numero entero positivo: "))
suma = 0

for digito in str(num):
    suma += int(digito)

print("La suma de los digitos es:", suma)