"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    diccionario = {}
    with open("files/input/data.csv", "r") as doc:
        for i in doc:
            separar = i.strip().split('\t') #separo, practicamente en todos se hace lo mismo al inicio
            n = int(separar[1]) #si voy a sumar necesitor que sean numeros
            letra = separar[3].split(',') #separo la columna 4 por coma
            for j in letra:
                if j in diccionario:
                    diccionario[j] += n
                else:
                    diccionario[j] = n

    resultado = {}
    for m in sorted(diccionario):
        resultado[m] = diccionario[m]
    return resultado

    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
