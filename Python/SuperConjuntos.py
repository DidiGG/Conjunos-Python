"""Recibe el conjunto universal y el conjunto A y verifica cuales son los elementos que le faltan a A para ser igual que universal
, tener en cuenta que la funcion devuelve un conjunto con los elementos que le faltan a A para ser igual que el universal"""

def definirConjuntComplemento(conjuntoUniversal,conjuntoA):
    conjuntoComplemento=[]
    contador=0
    for elementoUniversal in conjuntoUniversal:
        for elementoA in conjuntoA:
            if elementoUniversal==elementoA:
                contador+=1
        if contador==0:
            conjuntoComplemento.append(elementoUniversal)
        contador=0
    return conjuntoComplemento

"""Instancia el conjunto universal y el A. Creo una variable donde guardar el conjunto resultante y
envio por parametro los dos conjuntos al metodo definirConjuntComplemento """
conjuntoUniversal=["no","quiero","hacer","tareas","especialmente","las de tlf"]
conjuntoA=["no","las de tlf","hacer","tareas","quiero irme a dormir"]
conjuntoComplemento=definirConjuntComplemento(conjuntoUniversal,conjuntoA)
print(conjuntoComplemento)