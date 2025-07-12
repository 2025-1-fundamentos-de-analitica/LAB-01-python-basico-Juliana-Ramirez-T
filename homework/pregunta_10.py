"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    lista = []
    with open("files/input/data.csv", "r") as doc:
        for i in doc:
            separar = i.strip().split("\t") #separooooo
            letra = separar[0] #la letra de la colum 1
            c4 = separar[3].split(",")
            nc4 = len(c4) #cantidad de elemento en la columna 4
            c5 = separar[4].split(",")
            nc5 = len(c5) #cantidad de elemento en la columna 4
            lista.append((letra, nc4, len(c5))) #agregar elementos a la listaa
    return lista


    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
