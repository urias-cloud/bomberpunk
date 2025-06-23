from .Personaje import Personaje
from .Bomba import Bomba

class Jugador(Personaje):
    def __init__(self, nombre, vida, x, y):
        super().__init__(nombre, vida, x, y)
        self.bomba_activa = None
        self.velocidad = 5

    def atacar(self, tiempo_actual):
        if self.bomba_activa is None:
            pos = self.mostrar_posicion()
            bomba = Bomba(pos[0], pos[1], "normal", tiempo_actual)
            self.bomba_activa = bomba
            return bomba
        return None
