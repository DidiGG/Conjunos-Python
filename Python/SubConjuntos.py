from Python.InicialMayorQueFinalException import InicialMayorQueFinal
from Python.ValoresFueraDeLosLimitesException import ValoresFueraDeLosLimitesException


def sacarSubconjunto(conjuntoGenerico):
    subConjuntoB = []
    try:
        inicioSubConjunto = int(input("Ingrese desde que posicion del conjunto quiere que inicie su nuevo subconjunto"))
        finalSubConjunto = int(input("Ingrese la posicion donde finalizara su nuevo subconjunto"))
        if inicioSubConjunto >= len(conjuntoGenerico):
            raise ValoresFueraDeLosLimitesException()
        if finalSubConjunto > len(conjuntoGenerico):
            raise ValoresFueraDeLosLimitesException()
        if inicioSubConjunto >= finalSubConjunto:
            raise InicialMayorQueFinal()
    except TypeError:
        print("El inicio y el final del subconjunto deben ser numeros enteros")
    except ValoresFueraDeLosLimitesException as e:
        print(e.message)
    else:

        else:
            inicioSubConjunto -= 1
            while inicioSubConjunto < finalSubConjunto:
                subConjuntoB.append(conjuntoGenerico[inicioSubConjunto])
                inicioSubConjunto+=1
    return subConjuntoB

conjuntoA=["Hola",",","no","quiero","hacer","la","tarea","de","tlf"]
subConjuntoB=sacarSubconjunto(conjuntoA)
if subConjuntoB!=None:
    print(subConjuntoB)