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
        print(linea.strip())

        if linea.strip():
            #Lista de diccionarios que contiene todas las preguntas almacenadas enel banco de preguntas
            diccionario_pregunta = extraer_pregunta(linea)
            #Metemos el diccionario en la lista general
            lista_banco_preguntas.append(diccionario_pregunta)
        



