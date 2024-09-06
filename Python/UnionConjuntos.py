import matplotlib.pyplot as plt
from matplotlib_venn_wordcloud import venn3_wordcloud

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Definir los conjuntos
conjuntoA = {"A", "B", "C", "D", "E"}
conjuntoB = {"B", "G", "J"} 
conjuntoC = {"Z", "D", "X","B"}

#Creamos la Union
unionABC =  conjuntoA.union(conjuntoB, conjuntoC)

#Mostramos en consola el resultado de la union
print(unionABC)

# Cracion del diagrama de venn 
# Los duplicados se eliminan automáticamente
venn = venn3_wordcloud([conjuntoA, conjuntoB, conjuntoC], 
                       ('Conjunto A', 'Conjunto B', 'Conjunto C'))


plt.show()

# Crear una cadena de texto con los elementos de la unión
union_text = ' '.join(unionABC)

# Crear la nube de palabras
wordcloud = WordCloud(width=200, height=150, background_color='white', max_font_size=30).generate(union_text)

# Mostrar la nube de palabras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title("Visualización del Conjunto Unión")


# Mostrar el diagrama
plt.show()