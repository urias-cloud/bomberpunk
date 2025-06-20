# Clase pared que tendrá características: destruible y no destruible

class Pared:
    """Método constructor: recibe la posición y tipo de pared (destruible o no) y define su estado"""
    def __init__(self, pos_x, pos_y, tipo_pared):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tipo_pared = tipo_pared
        self.destruida = False  # Estado inicial: la pared no esta destruida

    def destruir(self):
        """Método que destruye la pared si es destruible y no fue destruida aún"""
        if self.tipo_pared == "destruible" and not self.destruida:
            self.destruida = True
            return True
        return False

    def mostrar_posicion(self):
        """Retorna la posición como tupla (pos_x, pos_y)"""
        return (self.pos_x, self.pos_y)

    def esta_destruida(self):
        """Retorna si la pared está o no destruida"""
        return self.destruida
