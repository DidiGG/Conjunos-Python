import matplotlib.pyplot as plt
from matplotlib_venn_wordcloud import venn3_wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Se crea una funcion que une dos conjuntos y retorna un conjunto auxiliar
def crearConjuntoAuxiliar(conjuntoA,conjuntoB):
    conjuntoAuxiliar=conjuntoA
    for elementoB in conjuntoB:
        conjuntoAuxiliar.append(elementoB)
    return conjuntoAuxiliar

"""Funcion que recibe el conjunto auxiliar y por medio de dos ciclos, se recorre asi mismo y se pregunta si
cada uno de los elementos esta mas de una vez dentro del conjunto, si no es asi, agrega ese elemento a otro arreglo,
 que el metodo retornara despues"""
def realizarDiferenciaSimetrica(conjuntoAuxiliar):
    diferenciaSimetrica=[]
    contador=0
    for elementoAuxiliar in conjuntoAuxiliar:
        for elementoAuxiliar2 in conjuntoAuxiliar:
            if elementoAuxiliar == elementoAuxiliar2:
                contador+=1
        if contador==1:
            diferenciaSimetrica.append(elementoAuxiliar)
        contador=0
    return diferenciaSimetrica

conjuntoA=[1,2,5,7]
conjuntoB=[5,6,7,4]
conjuntoC=[8,2,6,3]
conjuntoAuxiliar=crearConjuntoAuxiliar(conjuntoA,conjuntoB)
print(conjuntoAuxiliar)
conjuntoAuxiliar=crearConjuntoAuxiliar(conjuntoAuxiliar,conjuntoC)
print(conjuntoAuxiliar)
diferenciaSimetrica=realizarDiferenciaSimetrica(conjuntoAuxiliar)
print(diferenciaSimetrica)




