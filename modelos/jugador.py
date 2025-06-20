from modelos import Personaje
from modelos import Bomba

# Clase jugador representa nuestro personaje principal
class Jugador(Personaje):
    """Método constructor: recibe los parámetros de la superclase y se añade cantidad de bombas"""
    def __init__(self, nombre, vida, x, y):
        super().__init__(nombre, vida, x, y)
        self.bomba_activa = None
        self.alcance = 40

    def atacar(self):
        """metodo atacar: coloca bombas (puede atacar enemigos o muros)
        Retorna:
        - instancia de bomba si se acaba de colocar,
        - daño de la bomba explotada
        - None si no coloco bomba (porque ya hay una activa que no exploto)"""
        if self.bomba_activa is None:
            posicion = self.mostrar_posicion()  # se asigna la posición a colocar la bomba
            bomba = Bomba(posicion[0], posicion[1], "normal") #crea bomba pasando los parametros
            self.bomba_activa = bomba  # se asigna la bomba creada a bomba_activa cambiando estado de None
            return bomba  # retornamos la bomba para poder usarla
        else:
            if self.bomba_activa.estadoBomba():  # si bomba_activa tiene bomba calcula el daño y retorna
                danio_causado = self.bomba_activa.calcular_danio()
                self.bomba_activa = None # cambia el estado de bomba_activa(vuelve a none, ya esta vacia)
                return danio_causado  # retorna el daño para poder usarlo
            else:
                return None  # la bomba todavia no exploto
