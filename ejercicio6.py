class Vehiculo:

    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas


class Coche(Vehiculo):

    def __init__(self, velocidad, cilindrada):
        self.velocidad = velocidad
        self.cilindrada = cilindrada


N370z = Coche(250, 3.7)
N370z.color = "Platino"
N370z.ruedas = 4
N370z.puertas = 3


print(
    f"El Nissan 370z viene en color {N370z.color}, tiene {N370z.ruedas} ruedas y {N370z.puertas} puertas. Alcanza una velocidad máxima de {N370z.velocidad} km/h con una cilindrada de {N370z.cilindrada} CC")
