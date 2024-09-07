"""Recibe el conjunto universal y el conjunto A y verifica cuales son los elementos que le faltan a A para ser igual que universal
, tener en cuenta que la funcion devuelve un conjunto con los elementos que le faltan a A para ser igual que el universal"""

def definirConjuntComplemento(conjuntoUniversal,conjuntoA):
    conjuntoComplemento=set()
    contador=0
    for elementoUniversal in conjuntoUniversal:
        for elementoA in conjuntoA:
            if elementoUniversal==elementoA:
                contador+=1
        if contador==0:
            conjuntoComplemento.add(elementoUniversal)
        contador=0
    return conjuntoComplemento

"""Instancia el conjunto universal y el A. Creo una variable donde guardar el conjunto resultante y
envio por parametro los dos conjuntos al metodo definirConjuntComplemento """
conjuntoUniversal={'A','B','C','D','E','F'}
conjuntoA={'A','E'}
conjuntoComplemento=definirConjuntComplemento(conjuntoUniversal,conjuntoA)
print(conjuntoComplemento)