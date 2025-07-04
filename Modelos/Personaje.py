class Personaje:
    """clase personaje , es l personaje principal del juego , de esta clase jugador y enemigo heredan sus metodos y atributos"""
    def __init__(self, nombre, vida, pos_x, pos_y):
        """metodo constructor de la clase recibe nombre la vida y las posiciones del personaje """
        self.nombre = nombre
        self.vida = vida
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direccion = "derecha" #atributo para la animacion
    def mover(self, nueva_x, nueva_y):
        """metodo mover, se le pasan de parametros las nuevas posicones  a donde debe moverse el personaje"""
        self.pos_x = nueva_x
        self.pos_y = nueva_y#asiganamos las nuevas posiciones

    def recibir_danio(self, cantidad):
        """metodo q recibe daño, se le pasa como parametro la cantidad de daño a recibir y se la resta a la vida del personaje"""
        self.vida -= cantidad
        if self.vida < 0:#si vida es menor la iguala 0 , ya que no puede ser negativo
            self.vida = 0

    def esta_vivo(self):
        """metodo que retorna si el personaje esta vivo"""
        return self.vida > 0

    def get_posicion(self):
        """metodo que retorna la posion (se puede usar parea otros metodos)"""
        return (self.pos_x, self.pos_y)
