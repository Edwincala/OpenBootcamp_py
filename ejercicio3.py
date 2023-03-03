peso = float(input("Por favor digita tu peso en kilogramos:"))
estatura = float(input("Por favor digita tu estatura en metros: "))

imc = peso / (estatura ** 2)

print("Tu índice de masa corporal es", round(imc, 2))
