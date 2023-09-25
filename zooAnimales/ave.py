from zooAnimales.animal import Animal
class Ave(Animal):
    _listaAves = []
    aguilas = 0
    halcones = 0
    def __init__(self, nombre, edad, habitat, genero, pluma):
        super().__init__(nombre, edad, habitat, genero)
        self._colorPlumas = pluma
        Ave._listaAves.append(self)
    @staticmethod
    def cantidadAves():
        return len(Ave._listaAves)
    @staticmethod
    def movimiento():
        return "volar"
    @classmethod
    def crearHalcon(cls, nombre, edad, genero):
        cls.halcones += 1
        return cls(nombre, edad, "montana", genero, "cafe glorioso")
    @classmethod
    def crearAguila(cls, nombre, edad, genero):
        cls.aguilas += 1
        return cls(nombre, edad, "montana", genero, "blanco y amarillo")
    def getColorPlumas(self):
        return self._colorPlumas
    def setColorPlumas(self, colorPlumas):
        self._colorPlumas = colorPlumas