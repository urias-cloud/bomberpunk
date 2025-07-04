class Bomba:
    """ clase bomba logica"""
    def __init__(self, pos_x, pos_y, tipo, tiempo_colocada):
        """metodo constructo recibe las posiciones de x e y, el tipo de bomba y el el tiemmpo que fue colocada"""
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tipo = tipo
        self.tiempo_colocada = tiempo_colocada
        self.explotada = False#atributo  para saber el estado de una bomba si exploto o no
        self.alcance = 30#alcanze del daño de la bomba
        self.danio = {
            #diccionartio con los valores de daño segun su tipo
            "normal": 30,
            "electrica": 50,
            "hielo": 20,
            "fuego": 40
        }
        self.tiempo_explosion = {
            #diccionario con el tiempo que tarda en explotar la bomba segun su tipo
            "normal": 2500,
            "electrica": 4500,
            "hielo": 3500,
            "fuego": 4000
        }[tipo]

    def calcular_danio(self):
        """metodo calcula el dañio que causa una bomba , lo obtien del diccionario de daños"""
        return self.danio.get(self.tipo, 0)

    def estado_bomba(self, tiempo_actual):
        """metodo que recibe el tiempo actual y comprobamos el estado de la bomba (explotada o no)"""
        if not self.explotada and (tiempo_actual - self.tiempo_colocada) >= self.tiempo_explosion:
            self.explotada = True
            return True
        return False

    def mostrar_posicion(self):
        """metodo que retorna la posicon de la bomba"""
        return (self.pos_x, self.pos_y)
