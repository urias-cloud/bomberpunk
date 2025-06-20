import pygame
#clase que representa un personaje grafico en la pantalla 

class PersonajeGrafico:
    """metodo constructor para inicializarse recibe de parametros la posicion y el color y un modelo de personaje"""
    def __init__(self, x, y, color, modelo):
        self.rect = pygame.Rect(x, y, 60, 60)
        self.color = color
        self.modelo = modelo
    def mover(self, direccion, cantidad, ANCHO, ALTO):
        """metodo para mover a personaje,sus parametros son el ancho y alto de la pantalla ,cantidad de desplazamineto y direccion de movimiento """
        if direccion == "arriba":
            self.rect.y -= cantidad
        elif direccion == "abajo":
            self.rect.y += cantidad
        elif direccion == "izquierda":
            self.rect.x -= cantidad
        elif direccion == "derecha":
            self.rect.x += cantidad
    
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > ANCHO:
            self.rect.right = ANCHO
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > ALTO:
            self.rect.bottom = ALTO

    def dibujar(self, pantalla):
        """metodo para dibujar al personaje donde se le pasa la pantalla que debe dibujarlo"""
        pygame.draw.rect(pantalla, self.color, self.rect)


    def colisiona_con(self, otro):  
        """metodo para saber si se produce colicion(ennemigo ,pared),retorna true si sucede"""
        return self.rect.colliderect(otro.rect)
      
    def actualizar_posicion(self):
        """metodo que actualiza la posicion del rectangulo grafico asi coincide con la posici�n
            almacenada en el modelo """
        self.rect.x = self.modelo.pos_x
        self.rect.y = self.modelo.pos_y