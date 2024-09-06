def crearConjuntoAuxiliar(conjuntoA,conjuntoB):
    conjuntoAuxiliar=conjuntoA
    for elementoB in conjuntoB:
        conjuntoAuxiliar.append(elementoB)
    return conjuntoAuxiliar

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
conjuntoAuxiliar=crearConjuntoAuxiliar(conjuntoA,conjuntoB)
diferenciaSimetrica=realizarDiferenciaSimetrica(conjuntoAuxiliar)
print(diferenciaSimetrica)
