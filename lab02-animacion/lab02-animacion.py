import arcade
import random #Para que la lluvia vaya por sitios aleatorios y parezca realista

SCREEN_WIDTH = 800 #Ancho
SCREEN_HEIGHT = 600 #Alto

class MiJuego(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "ANIMACIÓN LLUVIA")
        arcade.set_background_color(arcade.color.MIDNIGHT_BLUE) #Color del fondo
        
        #Variable que se incrementará cada vez que se invoque on_draw para hacer la animación
        self.contador = 0
        
        #Creamos lista de gotas
        self.lista_gotas = []
        #Generamos 65 gotas de agua
        for i in range(65):
            x = random.randrange(0, SCREEN_WIDTH) #Posición x aleatoria por todo el ancho de la ventana
            y = random.randrange(0, SCREEN_HEIGHT) #Posición y aleatoria por todo el ancho de la ventana
            self.lista_gotas.append([x, y]) #Añadimos a la lista cada gota generada

    #Función donde está el código del dibujo
    def on_draw(self):
        self.clear() 
        
        #Dibujamos la hierba del suelo
        arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.ENGLISH_GREEN)  

        #Dibujamos la lluvia
        for gota in self.lista_gotas:
            x = gota[0]
            y = gota[1]

            #Actualizamos la variable y (la altura de la gota) restandole el contador para crear el efecto de animacion de las gotas cayendo
            y_actual = y - self.contador

            #Lógica para que si las gotas salen de la pantalla por debajo vuelvan a aparecer por arriba
            if y_actual < 0:
                gota[1] = SCREEN_HEIGHT + self.contador


            #Dibujamos una línea hacia abajo para simular la gota cayendo
            arcade.draw_line(x, y_actual, x, y_actual-15, arcade.color.LIGHT_BLUE)

        #Incrementamos el contador cada vez que se ejecuta la función on_draw
        self.contador += 5

if __name__ == "__main__":
    juego = MiJuego()
    arcade.run()