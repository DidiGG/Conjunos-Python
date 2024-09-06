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

conjuntoUniversal=["no","quiero","hacer","tareas","especialmente","las de tlf"]
conjuntoA=["no","las de tlf","hacer","tareas","quiero irme a dormir"]
conjuntoComplemento=definirConjuntComplemento(conjuntoUniversal,conjuntoA)
print(conjuntoComplemento)