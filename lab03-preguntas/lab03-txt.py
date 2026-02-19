#Lógica para visualizar línea a línea el archivo con el banco de preguntas
with open("lab03-preguntas/preguntas.txt", 'r', encoding = 'utf-8') as archivo:
    for linea in archivo:
        print(linea.strip())

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
