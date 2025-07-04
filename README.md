# 💣 BOMBERPUNK

**Bomberpunk** es un juego estilo **Bomberman**, desarrollado en **Python** usando **Pygame**, con temática visual **cyberpunk**. El jugador debe moverse estratégicamente por un mapa, esquivar enemigos, destruir paredes con bombas, y sobrevivir a los ataques enemigos.

Este proyecto sigue una arquitectura **MVC (Modelo - Vista - Controlador)** bien estructurada, pensado tanto para aprendizaje como para expansión futura.

## 🧠 ¿Cómo jugar?

🎮 Usa las flechas del teclado para moverte.
🔴 Apreta **ESPACIO** para colocar una bomba.
💥 Las bombas explotan luego de un tiempo y pueden destruir paredes destructibles o eliminar enemigos.
👾 Evita el contacto con enemigos o explosiones, ya que perderas vida.
🧠 ¡Sobrevivi el mayor tiempo posible!

---

## 🚀 Instalación y ejecución

```bash
git clone https://github.com/tuusuario/bomberpunk.git
cd bomberpunk
'### 3. Instala el entorno virtual'
python -m venv venv
'### 4. Activalo'
venv\Scripts\activate #windows
source venv/bin/activate #linux
'### 5. Instala las dependencias'
pip install -r requirements.txt
'### 6. Corre el juego'
python main.py

'### 7. El proyecto contiene test realizados a la parte logica, podes ejecutarlos con el siguiente comando'
python -m unittest discover tests

## 👨‍💻 Desarrolladores

🟥 **Urias Altamirano**
🟩 **Luciano Gil**
#Le agregamos un mapa de fondo y le cambiamos la bomba
#La idea es seguir trabajando en este juego como un proyecto personal y ver hasta donde llega queremos presentarlo en septiembre, por lo tanto esta version va a seguir siendo actualizada hasta ese momento para mejorarlo lo mas que podamos
# METAS A FUTURO:
# Mejorar las fisicas para que el personaje puede desplazarle de una forma fluida sin chocarse tanto
# Que la bomba explote en direcciones(arriba,abajo,izq y der) y que tenga animacion.Agregar mas tipos de bombas  
# Agregar mas enemigos
# Cambiar el personaje y mejorar su animacion ya que el que esta no es uno oficial