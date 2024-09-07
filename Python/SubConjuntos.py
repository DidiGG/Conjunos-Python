from ExcepcionMayor import InicialMayorQueFinal
from Outlimit import ValoresFueraDeLosLimitesException


def sacarSubconjunto(conjuntoGenerico):
    subConjuntoB = set()
    conjuntoGenerico=list(conjuntoGenerico)
    inicioSubConjunto=0
    finalSubConjunto=0
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
    except InicialMayorQueFinal as e1:
        print(e1.message)
    else:
        inicioSubConjunto -= 1
        while inicioSubConjunto < finalSubConjunto:
            subConjuntoB.add(conjuntoGenerico[inicioSubConjunto])
            inicioSubConjunto += 1

    return subConjuntoB

conjuntoA={1,2,3,4,5,6,7,8,9,0}
print(conjuntoA)
subConjuntoB=sacarSubconjunto(conjuntoA)
if len(subConjuntoB)>0:
    print(subConjuntoB)