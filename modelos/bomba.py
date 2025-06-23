class Bomba:
    def __init__(self, pos_x, pos_y, tipo, tiempo_colocada):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tipo = tipo
        self.tiempo_colocada = tiempo_colocada
        self.explotada = False
        self.alcance = 30
        self.danio = {
            "normal": 30,
            "electrica": 50,
            "hielo": 20,
            "fuego": 40
        }
        self.tiempo_explosion = {
            "normal": 3000,
            "electrica": 4500,
            "hielo": 3500,
            "fuego": 4000
        }[tipo]

    def calcular_danio(self):
        return self.danio.get(self.tipo, 0)

    def estado_bomba(self, tiempo_actual):
        if not self.explotada and (tiempo_actual - self.tiempo_colocada) >= self.tiempo_explosion:
            self.explotada = True
            return True
        return False

    def mostrar_posicion(self):
        return (self.pos_x, self.pos_y)
