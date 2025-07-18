"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    colector = {}

    with open("files/input/data.csv", "r") as doc:
        for i in doc:
            p = i.strip().split("\t")
            letra = p[0]
            if letra in colector:
                colector[letra] += 1
            else:
                colector[letra] = 1

    resultado = sorted(colector.items())
    return resultado

    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
