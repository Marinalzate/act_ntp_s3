import random

numero_secreto = random.randint(1, 10)
adivinado = False

while not adivinado:
    intento = int(input("Adivina el numero (1-10): "))
    if intento == numero_secreto:
        adivinado = True

print("¡Felicidades! Adivinaste el numero.")        