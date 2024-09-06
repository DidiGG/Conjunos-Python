import matplotlib.pyplot as plt
from matplotlib_venn_wordcloud import venn3_wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Conjuntos                  
conjuntoA = {"A", "B", "C", "D", "E"}
conjuntoB = {"B", "G", "J", "D"} 
conjuntoC = {"Z", "D", "X","B", "D"}

def interseccion_conjuntos(conjunto1, conjunto2, conjunto3):
    # Crear un conjunto con todos los elementos del primer conjunto
    resultado = set(conjunto1)

    # Mantener solo los elementos que también están en el segundo conjunto
    resultado = {elemento for elemento in resultado if elemento in conjunto2}
    
    # Mantener solo los elementos que también están en el tercer conjunto
    resultado = {elemento for elemento in resultado if elemento in conjunto3}

    return resultado


interseccionABC = interseccion_conjuntos(conjuntoA, conjuntoB, conjuntoC)
print("Interseccion: ", interseccionABC)

#Creación diagrama de Venn, con está libreria los 
#duplicados se eliminan automaticamente
venn = venn3_wordcloud([conjuntoA, conjuntoB, conjuntoC],
                       ('Conjunto A', 'Conjunto B', 'conjunto C'))
plt.show()

#Creamos una cadena de texto vacia para listar los elementos de la Interseccion
union_txt = ''.join(interseccionABC)

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

