import time
from modelos.pocion import Pocion

def test_explosion_despues_tiempo():
    pocion = Pocion(0, 0, timer=1) #creamos la pocion para que explote en 1 segundo
    pocion.tiempo_inicial -= 1.5 #le restamos a tiempo inicial(cuando se coloco) mas de 1 segundo
    pocion.actualizar() #al llamar la funcion actualizar, la bomba ya exploto
    self.assertTrue(pocion.explotada)
