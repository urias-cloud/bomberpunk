import pygame
import os

class PersonajeGrafico:
    def __init__(self,modelo, tamano_celda,ruta_imagen=None):
        """constructor de la clase recibe r ,modelo(personaje logico :jugador o enemigo)y la ruta de imagen"""
        self.modelo = modelo
        self.tamano_celda = tamano_celda
        #self.rect = pygame.Rect(self.modelo.pos_x, self.modelo.pos_y, tamano_celda, tamano_celda)#el rectangulo inici en la posicion de modelo logico
        ancho_colision = int(tamano_celda * 0.6)
        alto_colision = int(tamano_celda * 0.6)
        self.offset_x = (tamano_celda - ancho_colision) // 2
        self.offset_y = (tamano_celda - alto_colision) // 2

        self.rect = pygame.Rect(
            self.modelo.pos_x + self.offset_x,
            self.modelo.pos_y + self.offset_y,
            ancho_colision,
            alto_colision
        )

        
        
        
        
        self.imagen = None
        if ruta_imagen:
        # cargamos la imagen para escalarlo al tamaño de la celda
            self.imagen = pygame.image.load(ruta_imagen).convert_alpha()
            self.imagen = pygame.transform.scale(self.imagen, (tamano_celda, tamano_celda))
        else:
            self.imagen = None # Si falla, no hay imagen
                
    def actualizar_posicion(self):
        """metodo que actualiza la posciion grafica , donde el grafico(rec) recibe la posicion 
        del modelo actualizada y se la asigna ..asi actualiza la psociion del grafico"""
        #self.rect.topleft = (self.modelo.pos_x, self.modelo.pos_y) # se actulaiza la posicion del rectangulo grafico para que coincida con modelo lgico
        self.rect.topleft = (
            self.modelo.pos_x + self.offset_x,
            self.modelo.pos_y + self.offset_y
        )
    
    def dibujar(self, pantalla):
        """metodo q dibuja el modelo grafico  siempre y cuando el personaje logico(jugador-enemigo) este vivo.
        le pasamos la pantalla donde dibujar con el color a dibujar"""
        if self.modelo.esta_vivo() and self.imagen:
            #pantalla.blit(self.imagen, self.rect)
            pantalla.blit(self.imagen, (self.modelo.pos_x, self.modelo.pos_y))

        elif self.modelo.esta_vivo():
            pygame.draw.rect(pantalla, (255, 0, 255), self.rect) # si no hay imagen crea un rectangulo con color     

    def colisiona_con(self, otro_rect):
        """metodo que colisiona con otro personaje grafico usando la funcion colliderect , recibe como parametro el otro personaje /pared a colisionar"""
        return self.rect.colliderect(otro_rect)
