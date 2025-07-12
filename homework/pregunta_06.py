"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    final = {}
    with open("files/input/data.csv") as doc:
        for i in doc:
            separar = i.strip().split('\t')  #obtener columna 5 
            div = separar[4].split(',')  #dividimos con la coma
            for j in div:
                a1 = j.split(':')[0]
                a2 = j.split(':')[1]
                a2 = int(a2)
                if a1 not in final:
                    final[a1] = [a2, a2]
                else:
                    final[a1][0] = min(final[a1][0], a2)
                    final[a1][1] = max(final[a1][1], a2)
    sinnombre = []
    for k in final:
        sinnombre.append((k, final[k][0], final[k][1]))

    return sorted(sinnombre)  






    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
