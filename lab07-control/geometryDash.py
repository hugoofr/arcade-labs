import arcade

#CONSTANTES
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5 #Velocidad a la que se moverá el cubo
CUBE_SIZE = 50 #Tamaño del cubo

GROUND_HEIGHT = 200 #Altura del suelo


#CLASE CUBO (Objeto que podremos controlar con el teclado y con el mando)
class Cubo:
    def __init__(self):
        """Constructor"""
        self.size = CUBE_SIZE
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = GROUND_HEIGHT + (self.size / 2) #Lo colocamos justo encima del suelo 
        
        #Velocidad inicial
        self.change_x = 0 
        self.change_y = 0

    def update(self):
        """Método que actualiza la posición del cubo y comprueba las colisiones con los bordes"""
        self.center_x += self.change_x
        self.center_y += self.change_y

        #--- Límites de la pantalla ---
        #Izquierda y derecha
        if self.center_x < self.size / 2:
            self.center_x = self.size / 2   
        elif self.center_x > SCREEN_WIDTH - self.size / 2:
            self.center_x = SCREEN_WIDTH - self.size / 2
        #Suelo
        if self.center_y < GROUND_HEIGHT + (self.size / 2):
            self.center_y = GROUND_HEIGHT + (self.size / 2)
        #Techo    
        elif self.center_y > SCREEN_HEIGHT - self.size / 2:
            self.center_y = SCREEN_HEIGHT - self.size / 2

    def draw(self):
        """Dibujamos la cara del cubo usando formas geométricas"""
        #Calculamos los bordes absolutos
        left = self.center_x - (self.size / 2)
        right = self.center_x + (self.size / 2)
        bottom = self.center_y - (self.size / 2)
        top = self.center_y + (self.size / 2)

        #Borde exterior negro
        arcade.draw_lrbt_rectangle_outline(left, right, bottom, top, arcade.color.BLACK, border_width = 6)
        #Relleno amarillo
        arcade.draw_lrbt_rectangle_filled(left, right, bottom, top, arcade.color.YELLOW)
        #Ojo izquierdo
        arcade.draw_lrbt_rectangle_filled(self.center_x - 14, self.center_x - 4, self.center_y + 4, self.center_y + 14, arcade.color.CYAN)
        arcade.draw_lrbt_rectangle_outline(self.center_x - 14, self.center_x - 4, self.center_y + 4, self.center_y + 14, arcade.color.BLACK, border_width = 2.5)
        #Ojo derecho
        arcade.draw_lrbt_rectangle_filled(self.center_x + 4, self.center_x + 14, self.center_y + 4, self.center_y + 14, arcade.color.CYAN)
        arcade.draw_lrbt_rectangle_outline(self.center_x + 4, self.center_x + 14, self.center_y + 4, self.center_y + 14, arcade.color.BLACK, border_width = 2.5)
        #Boca
        arcade.draw_lrbt_rectangle_filled(self.center_x - 18, self.center_x + 18, self.center_y - 14, self.center_y - 4, arcade.color.CYAN)
        arcade.draw_lrbt_rectangle_outline(self.center_x - 18, self.center_x + 18, self.center_y - 14, self.center_y - 4, arcade.color.BLACK, border_width = 2.5)
        
#FUNCIONES DE DIBUJO DE FONDO
def dibujar_suelo():
    arcade.draw_lrbt_rectangle_filled(0, SCREEN_WIDTH, 0, 200, arcade.color.BLUE)


class MyGame(arcade.Window):
    """ Clase principal que controla la ventana """

    def __init__(self):
        """ Constructor """
        #Creamos la ventana
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "GEOMETRY DASH")
        #Color de fondo
        arcade.set_background_color(arcade.color.BABY_BLUE)
                                                                                                                                                                                                                                                                                                                                                               
        self.cubo = Cubo() #Creamos el cubo
         
        #Para jugar con el mando
        joysticks = arcade.get_game_controllers() #Pedimos al sistema operativo una lista de los mandos que están conectados al ordeandor

        if joysticks:
            #Si hay al menos uno, nos guardamos el primero [0]
            self.joystick = joysticks[0] #Tomamos el primer mando que encontremos 
            self.joystick.open() #Abrimos la comunicación con este mando
            print("Mando detectado correctamente.")
        else:
            print("No hay mandos conectados.")
            self.joystick = None

    def on_draw(self):
        self.clear()

        #LLAMAMOS A NUESTRAS FUNCIONES DE DIBUJO
        # Suelo
        dibujar_suelo()
        #Dibujamos el cubo
        self.cubo.draw()

    def on_key_press(self, key, modifiers):
        """Función que se llama cada vez que se pulsa una tecla"""
        if key == arcade.key.UP or key == arcade.key.W:
            self.cubo.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.cubo.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.cubo.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.cubo.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Se ejecuta al solatar una tecla"""
        if key in (arcade.key.UP, arcade.key.W, arcade.key.DOWN, arcade.key.S):
            self.cubo.change_y = 0
        elif key in (arcade.key.LEFT, arcade.key.A, arcade.key.RIGHT, arcade.key.D):
            self.cubo.change_x = 0        
        
    def on_update(self, delta_time):
        """Lógica del juego y movimiento"""
        self.cubo.update()

def main():
    window = MyGame()
    arcade.run()


main()