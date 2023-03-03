class Vehiculo:

    def __init__(self):
        color = self.color
        ruedas = self.ruedas
        puertas = self.puertas


class Coche(Vehiculo):
    velocidad = 0
    cilindrada = 0

    def __init__(self):
        Velocidad = self.velocidad
        Cilindrada = self.cilindrada


N370z = Coche()
N370z.color = "Platino"
N370z.ruedas = 4
N370z.puertas = 3
N370z.Velocidad = 250
N370z.Cilindrada = 3.7


print(
    f"El Nissan 370z viene en color {N370z.color}, tiene {N370z.ruedas} ruedas y {N370z.puertas} puertas. Alcanza una velocidad máxima de {N370z.Velocidad} km/h con una cilindrada de {N370z.Cilindrada} CC")
