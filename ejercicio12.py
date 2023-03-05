entrada = input("Introduce una lista de países separados por coma (,):")

paises_ordenados = sorted(set(entrada.replace(" ", "").split(",")))

print(", ".join(paises_ordenados))
