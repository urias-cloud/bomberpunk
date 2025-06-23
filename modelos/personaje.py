class Personaje:
    def __init__(self, nombre, vida, pos_x, pos_y):
        self.nombre = nombre
        self.vida = vida
        self.pos_x = pos_x
        self.pos_y = pos_y

    def mover(self, nueva_x, nueva_y):
        self.pos_x = nueva_x
        self.pos_y = nueva_y

    def recibir_danio(self, cantidad):
        print(f"[DAÑO] {self.nombre} recibió {cantidad} de daño. Vida restante: {self.vida}")
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def esta_vivo(self):
        return self.vida > 0

    def mostrar_posicion(self):
        return (self.pos_x, self.pos_y)
