import os
from .PersonajeGrafico import PersonajeGrafico # Importa la clase base
from modelos.animacion import Animacion
class EnemigoGrafico(PersonajeGrafico):
    """clase modelo grafico ,hereda de personaje grafico"""
    def __init__(self, modelo, tamano_celda):
        ruta_idle = os.path.join ("assets", "skeleton-idle.png")
        ruta_run = os.path.join("assets", "skeleton-walk.png")

        self.animacion = Animacion(32,32, ruta_idle, ruta_run)
        super().__init__(modelo, tamano_celda)

    def actualizar_posicion(self):
        """Metodo que sirve para actualizar la posicion del enemigo"""
        super().actualizar_posicion()
        # Detectamos movimiento (si cambió de posición)
        self.animacion.actualizar(self.modelo.direccion, caminando=True)

    def dibujar(self, pantalla):
        """Metodo para dibujar al enemigo"""
        if self.modelo.esta_vivo():
            imagen = self.animacion.imagen_actual
            pantalla.blit(imagen, self.rect) 
       