"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    #los mismooo
    diccionario = {}
    with open("files/input/data.csv", "r") as doc:
        for i in doc:
            separar = i.strip().split("\t") #separoo
            clave = separar[0] #como clave la columna 1 
            valor = separar[4].split(",") #la suma de los valores de la columna 5 sobre todo el archivo
            for j in valor:
                suma = 0
                suma += int(j[4:])
                if clave in diccionario:
                    diccionario[clave] += suma
                else:
                    diccionario[clave] = suma
    return diccionario
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
