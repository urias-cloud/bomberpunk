import random
from .Personaje import Personaje

class Enemigo(Personaje):
    def __init__(self, nombre, vida, pos_x, pos_y, velocidad, tipo):
        super().__init__(nombre, vida, pos_x, pos_y)
        self.velocidad = velocidad
        self.tipo = tipo
        self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
        self.ultimo_ataque_logico = 0
        self.tiempo_entre_ataques = 1000
        self.ultimo_cambio_direccion = 0
        self.tiempo_cambio_direccion = 1500
        self.valor_danio = {
            "normal": 30,
            "oscuridad": 50,
            "voladores": 20,
            "infierno": 40
        }

    def calcular_danio(self):
        return self.valor_danio.get(self.tipo, 0)

    def atacar(self, otro, tiempo_actual):
        if tiempo_actual - self.ultimo_ataque_logico >= self.tiempo_entre_ataques:
            otro.recibir_danio(self.calcular_danio())
            self.ultimo_ataque_logico = tiempo_actual

    def mover_ia(self, tiempo):
        if tiempo - self.ultimo_cambio_direccion > self.tiempo_cambio_direccion:
            self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])
            self.ultimo_cambio_direccion = tiempo

        dx, dy = 0, 0
        if self.direccion == "arriba":
            dy = -self.velocidad
        elif self.direccion == "abajo":
            dy = self.velocidad
        elif self.direccion == "izquierda":
            dx = -self.velocidad
        elif self.direccion == "derecha":
            dx = self.velocidad

        return self.pos_x + dx, self.pos_y + dy
