#Función que toma una pregunta y sus opciones y devuelve un diccionario estructurado
def extraer_pregunta(pregunta: str) -> dict:
    
    partes = pregunta.strip().split("|")
    
    texto_pregunta = partes[0].strip()
    
    #Tal y como esta definido el archivo, la primera opción siempre es la correcta
    texto_correcta = partes[1].strip()

    #Lista con las opciones de cada pregunta
    lista_opciones = [
        partes[1].strip(),
        partes[2].strip(),
        partes[3].strip(),
        partes[4].strip(),
    ]

    #Devolvemos el diccionario formateado
    return {
        "pregunta": texto_pregunta,
        "correcta": texto_correcta,
        "opciones": lista_opciones
    }

#Lista vacía que será nuestro banco de preguntas final
lista_banco_preguntas = []

#Abrimos el archivo y lo procesamos
with open("lab03-preguntas/preguntas.txt", 'r', encoding = 'utf-8') as archivo:
    for linea in archivo:

        if linea.strip():
            #Lista de diccionarios que contiene todas las preguntas almacenadas enel banco de preguntas
            diccionario_pregunta = extraer_pregunta(linea)
            #Metemos el diccionario en la lista general
            lista_banco_preguntas.append(diccionario_pregunta)
        
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
