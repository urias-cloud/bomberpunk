from .Personaje import Personaje
from .Bomba import Bomba


class Jugador(Personaje):
    """clase jugador logico donde herda la clase Personaje, tambien importa clase bomba para utilizarla en el metodo atacar"""
    def __init__(self, nombre, vida, x, y):
        """constructor hereda los atributos de la clase Personaje """
        super().__init__(nombre, vida, x, y)
        self.bomba_activa = None#atributo del jugador para llevar el control si coloco bomba o no , si esta none es q no coloco ninguna bomba cuando ataco

    def atacar(self, tiempo_actual):
        """metodo que ataca a enenmigo o pared , recibe tiempo que se pasa como parametro a bomba para controlar la explosion"""
        if not self.esta_vivo():
            return None
        if self.bomba_activa is None:
            pos = self.get_posicion()#metodo de la clase personaje(superclase) retorna la posion asi la usamos para asignar la posion de la bomba ( la misma que jugador)
            bomba = Bomba(pos[0], pos[1], "normal", tiempo_actual)
            self.bomba_activa = bomba#cambia el atributo de bomba activa , pasa de no tener ninuguna(None) a tener una bomba
            return bomba
        return None
