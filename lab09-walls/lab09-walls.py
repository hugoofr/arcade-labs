""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        #Lista de Sprites
        self.player_list = None
        self.wall_list = None

        #Configuramos el jugador
        self.player_sprite = None

        #Variable que contiene nuestro sencillo "motor de física"
        self.physics_engine = None

    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        #Listas de Sprites
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        #Reiniciamos la puntuación
        self.score = 0

        #Creamos el jugador
        self.player_sprite = arcade.Sprite("lab09-walls/jugador.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

        #Formamos muros de cajas 
        coordinate_list = [[400, 500],
                           [470, 500]]
        
        for coordinate in coordinate_list:
            wall = arcade.Sprite("lab09-walls/caja.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

 
    def on_draw(self):
        self.clear()        
        
        #Dibujamos los Sprites
        self.wall_list.draw()
        self.player_list.draw()

    def on_key_press(self, key, modifiers):
        """Función que se ejecuta cada vez que se pulsa una tecla"""

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Función que se ejecuta cada vez que se suelta una tecla"""

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0 

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()