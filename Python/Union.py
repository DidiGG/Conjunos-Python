import matplotlib.pyplot as plt
from matplotlib_venn_wordcloud import venn3_wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Conjuntos                  
conjuntoA = {"A", "B", "C", "D", "E"}
conjuntoB = {"B", "G", "J"} 
conjuntoC = {"Z", "D", "X","B"}

#Funcion para realizar la Union entre conjuntos
def union_conjuntos(*conjuntos):
    resultado = set()  # Crear un conjunto vacío para almacenar el resultado
    # Iterar sobre cada conjunto en el argumento
    for conjunto in conjuntos:
        # Agregar todos los elementos del conjunto actual al resultado
        for elem in conjunto:
            resultado.add(elem)
    return resultado


#Realizamos el resultado de la union
unionABC = union_conjuntos(conjuntoA, conjuntoB, conjuntoC)
print("Union: ", unionABC)

#Creación diagrama de Venn, con está libreria los 
#duplicados se eliminan automaticamente
venn = venn3_wordcloud([conjuntoA, conjuntoB, conjuntoC],
                       ('Conjunto A', 'Conjunto B', 'conjunto C'))
plt.show()

#Creamos una cadena de texto vacia para listar los elementos de la Union
union_txt = ''.join(unionABC)

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




