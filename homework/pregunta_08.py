"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_08():
    final = {}
    with open("files/input/data.csv") as doc:
        for i in doc:
            separar = i.strip().split('\t') #separaaa
            letra = separar[0]
            num = int(separar[1]) #columna 2
            if num not in final:
                final[num] = set()
            final[num].add(letra)
    lista = []  #la lista de tuplas
    for num in sorted(final): #se ordenaaaa
        letras_ordenadas = sorted(final[num])
        lista.append((num, letras_ordenadas))  #le agregamos los datos
    return lista



    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
