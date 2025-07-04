import random
from .Personaje import Personaje

class Enemigo(Personaje):
    """clase enemigo , que hace referencia al enemigo logico ,recibe los atributos de la clase personaje. se le agrega los parametros 
    velocidad(puede variar segun el tipo de enemigo) y el tipo de enemigo( segun su tipo sera su daño que cause)"""
    def __init__(self, nombre, vida, pos_x, pos_y, velocidad, tipo):
        super().__init__(nombre, vida, pos_x, pos_y)
        self.velocidad = velocidad
        self.tipo = tipo

        self.direccion = random.choice(["arriba", "abajo", "izquierda", "derecha"])#atributo direccion que con la clase random elige un opcion de movimiento para enemigo
        self.ultimo_cambio_direccion = 0 #atributoque almacena el ultimo cambio de movimiento que realizo el enemigo(fundamental para logica de movimiento)
        self.tiempo_cambio_direccion = 2000 # tiwmpo en segundos que tardara el enemigo en cambiar de posion(tambien fundamental para logica movimientpo)
        
        self.valor_danio = {
            "normal": 30,
            "oscuridad": 50,
            "voladores": 20,
            "infierno": 40
        }

    def calcular_danio(self):
        """metodo que calcula el daño que causa enemigo segun su tipo"""
        return self.valor_danio.get(self.tipo, 0)#con el metodo get pide que nos retorne el valor de daño(del diccionario de valores en el constructor) segun su tipo

    def cambiar_direccion(self):
        """metodo que  cambia la direccion del enemigo a una aleatoria"""
        direcciones_posibles = ["arriba", "abajo", "izquierda", "derecha"]
        self.direccion = random.choice(direcciones_posibles)
        
    def mover_ia(self, tiempo):
        """metodo que define el comportamiento autonomo de enemigo, como elige direccion y calcula su proxmima posicon
        recibe tiempo para calcular su movimiento"""
        
        if not self.esta_vivo(): #comprueba si esta vivo
            return self.pos_x, self.pos_y
        # aca cambia su posicion  donde si tiempo menos el ultimo cambio de poscion registrado es mayor al  tiempo de cambio de direcion que asignamos 
        # y a la variable direccion le asigna una nueva direcion con random, y termina actualizando el ultimo cambio de direccion 
        if tiempo - self.ultimo_cambio_direccion > self.tiempo_cambio_direccion:
            self.cambiar_direccion()
            self.ultimo_cambio_direccion = tiempo

        #calcula la posicon tentativa
        dx, dy = 0, 0#valores q representan cuanto se movera enemigo por eje x y eje y(ej: si direccion es "arriba" : dy que vale 0 se le resta velocidad ,dy pasa a ssr negativo es decir sube )
        if self.direccion == "arriba":
            dy = -self.velocidad
        elif self.direccion == "abajo":
            dy = self.velocidad
        elif self.direccion == "izquierda":
            dx = -self.velocidad
        elif self.direccion == "derecha":
            dx = self.velocidad

        if dx > 0:
            self.direccion = "derecha"
        elif dx < 0:
            self.direccion = "izquierda" 

        return self.pos_x + dx, self.pos_y + dy# retorna las posicion tentativa despues el controlador comprueba si hay colisiones copn pared o jugador


   