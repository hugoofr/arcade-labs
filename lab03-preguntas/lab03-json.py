import json

#Abrimos el archivo json
with open("lab03-preguntas/preguntas.json", 'r', encoding='utf-8') as archivo:
        lista_banco_preguntas = json.load(archivo)
        
#ÓGICA DEL JUEGO

puntos_jugador = 0 #Variable que almacenará los puntos del jugador

for pregunta in lista_banco_preguntas:
    
    print(pregunta["pregunta"])

    opciones = pregunta["opciones"]
    print("a) " + opciones[0])
    print("b) " + opciones[1])
    print("c) " + opciones[2])
    print("d) " + opciones[3])

    respuesta_jugador = input("Elige la opción correcta (a, b, c o d):").lower()

    #Traducimos la letra que introdujo el jugador al texto de la respuesta
    respuesta_elegida = ""
    if respuesta_jugador == 'a':
        respuesta_elegida = opciones[0]
    elif respuesta_jugador == 'b':
        respuesta_elegida = opciones[1]
    elif respuesta_jugador == 'c':
        respuesta_elegida = opciones[2]
    elif respuesta_jugador == 'd':
        respuesta_elegida = opciones[3]
    else:
        print("Opción no válida. Perdiste tu oportunidad en esta pregunta.")

    #Comprobamos si el jugador ha acertado la pregunta
    if respuesta_elegida == pregunta["correcta"]:
        print("¡Correcto! Sumas 5 puntos.\n")
        puntos_jugador += 5
    else:
        print(f"Incorrecto. La respuesta correcta era: {pregunta["correcta"]}\n")

#Fin del juego
print("¡Terminaste el juego!")
print("Tu puntuación optenida es = ", puntos_jugador)