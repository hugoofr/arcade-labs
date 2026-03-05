""" Lab 7 - User Control """
import arcade

#CONSTANTES
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#FUNCIONES DE DIBUJO DE FONDO
def dibujar_suelo():
    # Izquierda=0, Derecha=800, Abajo=0, Arriba=200
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, 200, arcade.color.SANDY_BROWN)

def dibujar_sol(x, y, escala):
    radio = 40 * escala
    arcade.draw_circle_filled(x, y, radio, arcade.color.YELLOW)
    arcade.draw_circle_outline(x, y, radio, arcade.color.ORANGE, 2 * escala)

def dibujar_piramide(x, y, escala):
    ancho_medio = 100 * escala
    altura = 200 * escala
    arcade.draw_triangle_filled(
        x - ancho_medio, y,
        x + ancho_medio, y,
        x, y + altura,
        arcade.color.BROWN
    )

def dibujar_cactus(x, y, escala):
    ancho = 20 * escala
    alto = 100 * escala
    
    # Calculamos los bordes a partir de un punto base (x, y)
    izq = x - (ancho / 2)
    der = x + (ancho / 2)
    abajo = y
    arriba = y + alto
    
    # Tronco principal
    arcade.draw_lrbt_rectangle_filled(izq, der, abajo, arriba, arcade.color.DARK_GREEN)
    
    # Brazos (Líneas para mantener tu estilo original)
    grosor = 8 * escala
    arcade.draw_line(x, y + 50 * escala, x - 20 * escala, y + 50 * escala, arcade.color.DARK_GREEN, grosor)
    arcade.draw_line(x - 20 * escala, y + 50 * escala, x - 20 * escala, y + 70 * escala, arcade.color.DARK_GREEN, grosor)

def dibujar_piedra(x, y, escala):
    arcade.draw_ellipse_filled(x, y, 80 * escala, 40 * escala, arcade.color.GRAY)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        #Inicialemente el sol estará en el centro
        self.sol_x = 400
        self.sol_y = 300

        #Ocultamos el cursor del ratón 
        self.set_mouse_visible(False)

    def on_draw(self):
        self.clear()

        #LLAMAMOS A NUESTRAS FUNCIONES PARA CREAR EL PAISAJE
        # Suelo
        dibujar_suelo()
        
        # Sol
        dibujar_sol(self.sol_x, self.sol_y, 1.0)
        
        # Pirámides
        dibujar_piramide(200, 200, 1.0)
        dibujar_piramide(450, 200, 0.7)
        
        # Cactus
        dibujar_cactus(100, 180, 0.8)
        dibujar_cactus(650, 200, 1.2)
        
        # Piedras
        dibujar_piedra(550, 100, 1.0)
        dibujar_piedra(720, 120, 0.5)

    #Función para mover con el ratón el sol (La función se activa cada vez que el ratón se mueve)
    def on_mouse_motion(self, x, y, dx, dy):
        #Actualizamos las variables con la posición del ratón
        self.sol_x = x
        self.sol_y = y

def main():
    window = MyGame()
    arcade.run()


main()