from .Pared import Pared

class Mapa:
    datos_mapa = [
    ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
    ['x',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ',' ',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x'],
    ['x',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x'],
    ['x','d',' ',' ','d',' ',' ',' ','d',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ','d',' ',' ',' ','d',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x'],
    ['x',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','d',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x'],
    ['x',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x'],
    ['x',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ',' ',' ','d',' ',' ',' ','x'],
    ['x',' ','x',' ','x',' ','x',' ','x','d','x','d','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x',' ','x'],
    ['x',' ','d','d','d','d',' ',' ',' ','d',' ',' ',' ','d','d','d','d','d',' ',' ',' ',' ',' ',' ',' ',' ','x'],
    ['x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x','x'],
    ]
    def __init__(self, tamano_celda):
        """constructor de la clase ,recibe los tamaños de las celdas , se crean listas para guardar las paredes """
        self.tamano_celda = tamano_celda
        self.paredes_logicas = []#lista que guarda las paredes creadas(en "x" y "d" de datos_mapa)
        self.num_filas = len(self.datos_mapa) #dimensiones del mapa 
        self.num_columnas = len(self.datos_mapa[0])
        self.inicializar_paredes()#metodo que crea laas paredes del mapa
    

    def inicializar_paredes(self):
        """metodo q crea las paredes del mapa(dato_mapa) segun su tipo(destructible -no destructible) recorriendo cada celda con un for"""
        for fila in range(self.num_filas): # Usa self.num_filas
            for col in range(self.num_columnas): # Usa self.num_columnas
                tipo = self.datos_mapa[fila][col] # Accede a datos_mapa como atributo de clase
                x = col * self.tamano_celda #coordenadas  donde se colocara la pared
                y = fila * self.tamano_celda
                if tipo == 'x':
                    self.paredes_logicas.append(Pared(x, y, "no_destruible"))#las paredes las guarda en la lista de paredes logicas
                elif tipo == 'd':
                    self.paredes_logicas.append(Pared(x, y, "destruible"))

    def obtener_paredes_activas(self):
        """metodo que obtiene las que no estan destruidas(guardadas en la lista de paredes logicas"""
        return [p for p in self.paredes_logicas if not p.esta_destruida()]
    
    def celda_ocupada(self, fila, columna):
        """metodo para comprobar si la celda se encuentra ocupada , recibe la fila y columna a comprobar"""
        if 0 <= fila < self.num_filas and 0 <= columna < self.num_columnas:#  verifica si las coordenadasestan dentro de limites del mapa
            return self.datos_mapa[fila][columna] != ' '  # si la celda es "x o y "en datos_mapa significa que hay una pared
        return True # si estafuera de los limites  se la considera ocupada
