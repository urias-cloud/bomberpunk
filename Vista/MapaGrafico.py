from .ParedGrafica import ParedGrafica

class MapaGrafico:
    def __init__(self, modelo_mapa, tamano_celda):
        self.modelo = modelo_mapa
        self.tamano_celda = tamano_celda
        self.paredes_graficas = []
        self._inicializar_paredes_graficas()

    def _inicializar_paredes_graficas(self):
        for pared_logica in self.modelo.paredes_logicas:
            if pared_logica.tipo == "no_destruible":
                color = (100, 100, 100)
            else:
                color = (150, 75, 0)
            self.paredes_graficas.append(ParedGrafica(
                pared_logica.pos_x,
                pared_logica.pos_y,
                color,
                pared_logica,
                self.tamano_celda
            ))

    def dibujar(self, pantalla):
        for pared in self.paredes_graficas:
            pared.dibujar(pantalla)

    def obtener_paredes_graficas_activas(self):
        return [p for p in self.paredes_graficas if not p.modelo.esta_destruida()]
