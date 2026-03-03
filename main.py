import random

numero_secreto = random.randint(1, 10)
intento = 0

print(" Adivina el número (del 1 al 10)")

while intento != numero_secreto:
    intento = int(input("Escribe tu número: "))
    
    if intento < numero_secreto:
        print("Muy bajo ⬇")
    elif intento > numero_secreto:
        print("Muy alto ⬆")
    else:
        
        print("¡Correcto!")