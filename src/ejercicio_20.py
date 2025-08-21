mayor = -1
edad = int(input("Ingresa una edad (-1 para terminar): "))

while edad != -1:
    if edad > mayor:
        mayor = edad
    edad = int(input("Ingresa una edad (-1 para terminar): "))

print("La edad mayor ingresada es:", mayor)