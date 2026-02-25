import arcade

arcade.open_window(800, 600, "DIBUJO")

#Color de fondo (cielo)
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

#Dibujamos el suelo
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, arcade.color.SANDY_BROWN)

#Dibujamos el sol
def dibujar_sol(x, y, escala):
    radio = 40 * escala
    grosor_borde = 2 * escala
    arcade.draw_circle_filled(x, y, radio, arcade.color.YELLOW)
    arcade.draw_circle_outline(x, y, radio, arcade.color.ORANGE, grosor_borde)

#Dibujamos una pirámide
def dibujar_piramide(x: int, y: int, escala: float) -> None:
    ancho_medio = 100 * escala
    altura = 200 * escala

    p1_x = x - ancho_medio
    p1_y = y

    p2_x = x + ancho_medio
    p2_y = y

    p2_x = x + ancho_medio
    p2_y = y

    p3_x = x
    p3_y = y + altura
    
    arcade.draw_triangle_filled(p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, arcade.color.BROWN)

#Dibujamos piedras
arcade.draw_ellipse_filled(550, 100, 80, 40, arcade.color.GRAY)
arcade.draw_ellipse_filled(700, 150, 80, 40, arcade.color.GRAY)
arcade.draw_ellipse_filled(700, 50, 80, 40, arcade.color.GRAY)

#Dibujamos un cáctus
arcade.draw_lrbt_rectangle_filled(700, 730, 200, 300, arcade.color.DARK_GREEN)
arcade.draw_line(680, 250, 680, 270, arcade.color.DARK_GREEN, 10)

dibujar_sol(700, 525, 1.0)
dibujar_piramide(200, 200, 1.0)

arcade.finish_render()
arcade.run()
