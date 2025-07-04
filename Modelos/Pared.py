class Pared:
    """clase pared , es la pared logica ,l as cuales se crearan en el mapa y maneja metodos de destrucion  y estados de las paredes"""
    def __init__(self, pos_x, pos_y, tipo):
        """constructor de la clase recibe las posiciones  y el tipo de pared(destruible o no destruible"""
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tipo = tipo
        self.destruida = False#estado de la pared: si sesta o no destruida 

    def destruir(self):
        """metodo para destruir una pared, sio su tipo es destruible y
        no se encuentra destruida , cambia su estado de no destruida a destruida(sel.destuida=true)"""
        if self.tipo == "destruible" and not self.destruida:
            self.destruida = True
            return True
        return False#sino es destruible o ya esta destruida retorna false

    def esta_destruida(self):
        """metodo que retorna si la pared esta destruida"""
        return self.destruida
