import pygame

class Bomba:
    
    def __init__(self, pos_x, pos_y, tipo_bomba):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tipoBomba = tipo_bomba #agregamos tipoBomba para diferenciar el daño
        self.alcance = 30
        self.tiempo_colocada = pygame.time.get_ticks()  #tiempo en que la bomba fue colocada
        self.explotada = False
        self.danosBombas = {
            "normal": 30,
            "electrica": 50,
            "hielo": 20,
            "fuego": 40
        }  #diccionario para mapear tipos de bomba a valores de daño
        self.tiempoExplosion = {
            "normal": 3000,
            "electrica": 4500,
            "hielo": 3500,
            "fuego": 4000
        }  #diccionario con el tiempo que tarda en explotar cada bomba
        self.tiempo_explosion = self.tiempoExplosion[self.tipoBomba]

    """metodo que retorna el daño causado por la bomba (según su tipo)"""
    def calcular_danio(self):
        return self.danosBombas.get(self.tipoBomba)

    #verifica si la bomba debe explotar y, si lo hace, retorna True.
    #logica: comprobar si no ha explotado ya, y si el tiempo transcurrido desde su colocacion es suficiente
    def estadoBomba(self):
        if not self.explotada and pygame.time.get_ticks() - self.tiempo_colocada >= self.tiempo_explosion:
            return self.explotar()
        return False

    """metodo que cambia el estado de la bomba (servira para el método activarBomba)"""
    def explotar(self):
        self.explotada = True

    """metodo que retorna la posición del jugador, que sirve para colocar las bombas"""
    def mostrar_posicion(self):
        posicion = (self.pos_x, self.pos_y)
        return posicion

        

    