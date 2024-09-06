import matplotlib.pyplot as plt
from matplotlib_venn_wordcloud import venn3_wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

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

#Creación diagrama de Venn, con está libreria los 
#duplicados se eliminan automaticamente
venn = venn3_wordcloud([conjuntoA, conjuntoB],
                       ('Conjunto A', 'Conjunto B'))
plt.show()

#Creamos una cadena de texto vacia para listar los elementos de la Interseccion
union_txt = ''.join(diferenciaSimetrica)

wordcloud = WordCloud(
    width=500,                    
    height=250,                   
    background_color='white',     
    colormap='rainbow',           
    contour_color='white',        
    contour_width=2               
).generate(union_txt)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")  # Ocultar los ejes
plt.show()


