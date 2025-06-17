import pygame 

class Jugador:
    """Esta clase representa al jugador dentro del modelo del juego
    No tiene logica visual ni deteccion de teclas
    """
    def __init__(self, x, y, ancho = 32, alto=32 ):
        
        self.x = x
        self.y = y
        self.ancho= ancho
        self.alto= alto
        self.velocidad = 2 #esta es la velocidad del jugador
        self.pociones = [] #este vendria a ser el control de las bombas, ya que en el futuro queremos agregar un boost para poder poner mas bombas a la vez

    """Los siguientes 4 metodos son para implentar la logica
    de movimiento al jugador
    """
    def mover_izquierda(self):
        self.x -= self.velocidad
    def mover_derecha(self):
        self.x += self.velocidad
    def mover_arriba(self):
        self.y -= self.velocidad
    def mover_abajo(self):
        self.y += self.velocidad
    
    """Este metodo sirve para colocar la pocion
    si o si depende de la clase pocion
    """
    def colocar_pocion(self):
        from modelo.pocion import Pocion
        pocion = Pocion(self.rect.x, self.rect.y)
        self.pociones.append(pocion)
        return pocion

