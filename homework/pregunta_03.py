"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    sumatoria = {}

    with open("files/input/data.csv", "r") as doc:
        for linea in doc:
            palabras = linea.strip().split("\t")
            letra = palabras[0]
            valor = int(palabras[1])

            if letra in sumatoria:
                sumatoria[letra] += valor
            else:
                sumatoria[letra] = valor

    final = sorted(sumatoria.items())
    return final












    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
