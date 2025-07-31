import pygame
import os
class ParedGrafica:
    def __init__(self, x, y, modelo, tamano_celda):
        """Metodo constructo de pared, enlaza las imagenes"""
        self.rect = pygame.Rect(x, y, tamano_celda, tamano_celda)
        self.modelo = modelo
    #asociacion de imagenes segun el tipo de pared
        if modelo.tipo == "no_destruible":
            ruta = os.path.join("assets", "pared_indestructible2.png")
        else: #destruible
            ruta = os.path.join("assets", "pared_destructible2.png")
        self.imagen_original = pygame.image.load(ruta).convert_alpha()#le damos la direccion de la imagen y le sacamos el fondo
        self.imagen = pygame.transform.scale(self.imagen_original, (tamano_celda, tamano_celda)) #recibe la imagen y la transforma a la escala que tiene la pared
    def dibujar(self, pantalla):
        """metodo para dibujar una pared si no esta destruida"""
        if not self.modelo.esta_destruida():
            pantalla.blit(self.imagen, self.rect.topleft)
            #pygame.draw.rect(pantalla, self.color, self.rect)

        
  