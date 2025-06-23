from .Pared import Pared

class Mapa:
    def __init__(self, datos_mapa, tamano_celda):
        self.matriz = datos_mapa
        self.tamano_celda = tamano_celda
        self.paredes_logicas = []
        self._inicializar_paredes()

    def _inicializar_paredes(self):
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[0])):
                tipo = self.matriz[fila][col]
                x = col * self.tamano_celda
                y = fila * self.tamano_celda
                if tipo == 'x':
                    self.paredes_logicas.append(Pared(x, y, "no_destruible"))
                elif tipo == 'd':
                    self.paredes_logicas.append(Pared(x, y, "destruible"))

    def obtener_paredes_activas(self):
        return [p for p in self.paredes_logicas if not p.esta_destruida()]
