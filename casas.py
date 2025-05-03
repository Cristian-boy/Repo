class Casa:
    def __init__(self, ventanas, puertas, techo, color):
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.color = color

    def mostrar_info(self):
        print(f"Casa con {self.ventanas} ventanas, {self.puertas} puertas, techo {self.techo} y color {self.color}.")


class ViviendaFamiliar(Casa):
    def __init__(self, ventanas, puertas, techo, color, num_habitaciones):
        super().__init__(ventanas, puertas, techo, color)
        self.num_habitaciones = num_habitaciones

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Vivienda familiar con {self.num_habitaciones} habitaciones.")


class Apartamento(Casa):
    def __init__(self, ventanas, puertas, techo, color, piso):
        super().__init__(ventanas, puertas, techo, color)
        self.piso = piso

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Apartamento ubicado en el piso {self.piso}.")


class Bungalow(Casa):
    def __init__(self, ventanas, puertas, techo, color, jardin):
        super().__init__(ventanas, puertas, techo, color)
        self.jardin = jardin

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Bungalow con jardín: {'Sí' if self.jardin else 'No'}.")

class CasaCampo(Casa):
    def __init__(self, ventanas, puertas, techo, color, pasto):
        super().__init__(ventanas, puertas, techo, color)
        self.pasto = pasto

    def mostrar_info(self):
        super().mostrar_info()
        print(f"casa de campo con monte y parque de diversiones: {'Sí' if self.pasto else 'No'}.")

# Ejemplo de uso
if __name__ == "__main__":
    casa1 = ViviendaFamiliar(4, 2, "a dos aguas", "blanco", 3)
    casa2 = Apartamento(2, 1, "plano", "gris", 5)
    casa3 = Bungalow(6, 2, "a dos aguas", "beige", True)
    casa4 = CasaCampo(6, 2, "pasto verde", "cafe", True)
    casa1.mostrar_info()
    print()
    casa2.mostrar_info()
    print()
    casa3.mostrar_info()
    print()
    casa4.mostrar_info()
    print()