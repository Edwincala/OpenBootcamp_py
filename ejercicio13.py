from functools import reduce

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

filtro = filter(lambda x: x % 2 != 0, lista)

suma = reduce(lambda a, b: a + b, filtro)

print(suma)
