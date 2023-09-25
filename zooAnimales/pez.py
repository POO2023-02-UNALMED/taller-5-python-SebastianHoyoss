from zooAnimales.animal import Animal
class Pez(Animal):
    _listaPeces = []
    salmones = 0
    bacalaos = 0
    def __init__(self, nombre, edad, habitat, genero, escamas, aletas):
        super().__init__(nombre, edad, habitat, genero)
        self._colorEscamas = escamas
        self._cantidadAletas = aletas
        Pez._listaPeces.append(self)
    @staticmethod
    def cantidadPeces():
        return len(Pez._listaPeces)
    @staticmethod
    def movimiento():
        return "nadar"
    @classmethod
    def crearSalmon(cls, nombre, edad, genero):
        cls.salmones += 1
        return cls(nombre, edad, "oceano", genero, "rojo", 6)
    @classmethod
    def crearBacalao(cls, nombre, edad, genero):
        cls.bacalaos += 1
        return cls(nombre, edad, "oceano", genero, "gris", 6)
    def getColorEscamas(self):
        return self._colorEscamas
    def setColorEscamas(self, colorEscamas):
        self._colorEscamas = colorEscamas
    def getCantidadAletas(self):
        return self._cantidadAletas
    def setCantidadAletas(self, cantidadAletas):
        self._cantidadAletas = cantidadAletas