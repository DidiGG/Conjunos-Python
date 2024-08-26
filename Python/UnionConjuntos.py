import matplotlib.pyplot as plt
from matplotlib_venn import venn3

#Conjuntos para realizar la unión
conjuntoA = {"A", "B" , "C", "D", "E"}
conjuntoB = {"B", "G", "G", "J"}
conjuntoC = {"Z", "D", "X", "G", "B"}

#Unión de los conjuntos
unionABC =  conjuntoA.union(conjuntoB, conjuntoC)

#Vemos la unión de conjuntos
print(unionABC)

venn = venn3([conjuntoA, conjuntoB, conjuntoC], ('Conjunto A', 'Conjunto B', 'Conjunto C'))
 
plt.show()



import matplotlib.pyplot as plt
from matplotlib_venn_wordcloud import venn3_wordcloud

# Definir los conjuntos
conjuntoA = {"A", "B", "C", "D", "E"}
conjuntoB = {"B", "G", "J"}  # Los duplicados se eliminan automáticamente
conjuntoC = {"Z", "D", "X","B"}

# Crear el diagrama de Venn
venn = venn3_wordcloud([conjuntoA, conjuntoB, conjuntoC], ('Conjunto A', 'Conjunto B', 'Conjunto C'))

# Mostrar el diagrama
plt.show()