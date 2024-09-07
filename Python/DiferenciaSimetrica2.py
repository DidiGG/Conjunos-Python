"""Funcion que recibe a los dos conjuntos a evaluar y por medio de cuatro ciclos, revisa si los conjuntos tienen elementos iguales,
 si es asi, no se agrega el elemento al nuevo conjunto diferencia simetrica"""
def realizarDiferenciaSimetrica(conjuntoA,conjuntoB):
    diferenciaSimetrica=set()
    contador=0
    for elementoA in conjuntoA:
        for elementoB in conjuntoB:
            if elementoA == elementoB:
                contador+=1
        if contador==0:
            diferenciaSimetrica.add(elementoA)
        contador=0
    for elementoB in conjuntoB:
        for elementoA in conjuntoA:
            if elementoB == elementoA:
                contador += 1
        if contador == 0:
            diferenciaSimetrica.add(elementoB)
        contador = 0
    return diferenciaSimetrica

conjuntoA=[1,2,5,7]
conjuntoB=[5,6,7,4,9,2,1]
conjuntoC=[8,2,6,3]
diferenciaSimetrica=realizarDiferenciaSimetrica(conjuntoA,conjuntoB)
"""Se envia el conjunto diferencia simetrica, porque, es el resultado de la diferencia simetrica entre los conjuntos A-B, porque, es la que se va a operar con el conjunto C"""
diferenciaSimetrica=realizarDiferenciaSimetrica(diferenciaSimetrica,conjuntoC)
print(diferenciaSimetrica)

