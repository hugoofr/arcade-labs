class Room:
    #Constructor
    def __init__(self, description = "", north = 0, east = 0, south = 0, west = 0):
        
        #Definimos los atributos
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west
    

def main():
    #Matriz 
    room_list = []

    #HABITACIÓN 0:
    room = Room("Estás en el dormitorio 2. Hay un pasillo a tu derecha y otra habitación al norte.", 3, 1, None, 0)
    room_list.append(room)

    #HABITACIÓN 1:
    room = Room("Estás en el pasillo sur. Puedes ir al norte, al este o volver al oeste.", 4, 2, None, 0)
    room_list.append(room)

    #HABITACIÓN 2:
    room = Room("Te encuentras en el comedor. Hay un paso al norte y un pasillo al oeste.", 5, None, None, 1)
    room_list.append(room)

    #HABITACIÓN 3:
    room = Room("Estás en el dormitorio 1. Hay un pasillo al este y otro dormitorio al sur.", None, 4, 0, None)
    room_list.append(room)

    #HABITACIÓN 4:
    room = Room("Estás en el pasillo norte. Puedes volver al dormitorio 1 al oeste, ir a la cocina que está a tu derecha, ir al pasillo sur o incluso salir al balcón al norte.", 6, 5, 1, 3)
    room_list.append(room)

    #HABITACIÓN 5:
    room = Room("Estás en la cocina. Puedes ir al pasillo a la izquierda o ir al comedor después de comer al sur.", None, None, 2, 4)
    room_list.append(room)

    #HABITACIÓN 6:
    room = Room("Estás en el balcón tomando el aire. Solo te puedes comunicar con el pasillo norte si te das la vuelta.", None, None, 4, None)
    room_list.append(room)