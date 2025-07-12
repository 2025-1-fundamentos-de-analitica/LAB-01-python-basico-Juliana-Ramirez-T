"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    colector= {}
    with open("files/input/data.csv", "r") as doc:
       for i in doc:
           total = i.strip().split("\t") #separar y quitar espacio en blancooo
           letra = total[0] #La letra de la primera columna A, B, ...
           numer = int(total[1]) #Los números, luego mirar si los max o min

           if letra in colector:
               #lista = colector[letra]
               colector[letra].append(numer)
           else:
               colector[letra] = [numer]
    

    final = []
    for letra in sorted(colector):
        num_max = max(colector[letra])
        num_min = min(colector[letra])
        final.append((letra, num_max, num_min))

    return final  

         
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
