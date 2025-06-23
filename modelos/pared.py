class Pared:
    def __init__(self, pos_x, pos_y, tipo):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tipo = tipo
        self.destruida = False

    def destruir(self):
        if self.tipo == "destruible" and not self.destruida:
            self.destruida = True
            return True
        return False

    def esta_destruida(self):
        return self.destruida
