"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    diccionario = {}
    with open("files/input/data.csv") as doc:
        for i in doc:
            separar = i.strip().split('\t') #dividimos 
            if len(separar) < 5:  #para que sea hasta la columna 5
                continue
            datos = separar[4].split(',')  #dividir colum 5 por coma
            for i in datos:
                clave = i.split(':')[0]
                if clave in diccionario:
                    diccionario[clave] += 1
                else:
                    diccionario[clave] = 1
    return diccionario


    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
