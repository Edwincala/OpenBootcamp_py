class Vehiculo:
    def __init__(self, marca, ventanas, ruedas, color, velocidad, cilindrada):
        self.marca = marca
        self.ventanas = ventanas
        self.ruedas = ruedas
        self.color = color
        self.velocidad = velocidad
        self.cilindrada = cilindrada


CX5 = Vehiculo("Mazda", 5, 4, "Rojo", 192, 2500)

with open('Mazda_CX5.txt', "w") as f:
    info = f"Marca: {CX5.marca} \nVentanas: {CX5.ventanas} \nRuedas: {CX5.ruedas} \nColor: {CX5.color} \nVelocidad: {CX5.velocidad} km/h \nCilindrada: {CX5.cilindrada} CCs"

    f.write(info)
