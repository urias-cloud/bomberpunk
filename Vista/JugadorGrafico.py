import pygame
import os 
from .PersonajeGrafico import PersonajeGrafico
from Modelos.animacion import Animacion

class JugadorGrafico(PersonajeGrafico):
    """Clase para representar gráficamente al jugador con animaciones."""

    def __init__(self, modelo, tamano_celda):
        # Rutas a spritesheets de animaciones
        ruta_idle = os.path.join("assets", "player-idle.png")
        ruta_run = os.path.join("assets", "player-run.png")

        self.animacion = Animacion(32, 32, ruta_idle, ruta_run)
        super().__init__(modelo, tamano_celda)

    def actualizar_posicion(self):
        """Actualiza la posición gráfica y la animación del jugador."""
        super().actualizar_posicion()
        # Lógica: si se mueve, animación de caminar; si no, idle
        # Podés ajustar esto si usás flags de teclas
        self.animacion.actualizar(self.modelo.direccion, caminando=True)

    def dibujar(self, pantalla):
        """Dibuja al jugador animado si está vivo."""
        if self.modelo.esta_vivo():
            imagen = self.animacion.imagen_actual
            pantalla.blit(imagen, self.rect)
