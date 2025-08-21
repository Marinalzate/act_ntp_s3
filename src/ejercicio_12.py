try:
    n = int(input("Introduce un número entero no negativo para calcular su factorial: "))
except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")
else:
    if n < 0:
        print("El factorial no está definido para números negativos.")
    elif n == 0:
        print("El factorial de 0 es 1.")
    else:
        factorial = 1
        contador = 1
        
        while contador <= n:
            factorial *= contador
            contador += 1
            
        print(f"El factorial de {n} es {factorial}.")
   