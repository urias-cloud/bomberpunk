"""Clase personaje con sus atributos y sus metodos"""

class Personaje:
  """Metodo constructor ,recibe como parametro nombre ,vida"""
  def __init__(self, nombre, vida,pos_x, pos_y):
    self.nombre = nombre
    self.vida = vida
    self.pos_x = pos_x # Posicion en el eje X
    self.pos_y = pos_y # Posicion en el eje Y
    self.esta_vivo = True

  def atacar(self):
    """Metodo atacar,luego sera sobreescrito por las subclases :jugador y enemigo """
  pass # por el momento no hace nada por defecto debido a que cada personaje ataca diferente
  
  def mostrar_estado(self):
    """Metodo que muestra el nombre y la vida actual del personaje"""
    return f"{self.nombre} - Vida: {self.vida}"
 
  def mostrar_posicion(self):
    """Metodo que retorna poscion del jugador, que sirve para colocar las bombas""" 
    posicion = (self.pos_x, self.pos_y)
    return posicion

  def mover(self, nueva_pos_x, nueva_pos_y):
    """metodo actualiza la posicion logica"""
    self.pos_x = nueva_pos_x
    self.pos_y = nueva_pos_y


  
  def recibir_danio(self, cantidad_danio):
      """Metodo que reduce la vida de personaje y verifica estado de vida"""
      self.vida -= cantidad_danio
      if self.vida <= 0:
        self.vida = 0
      else:
          self.esta_vivo = False
          print(f"{self.nombre}eliminado!!")

  def esta_vivo(self):
	    if self.vida > 0:
	      return True