import matplotlib.pyplot as plt
from matplotlib_venn_wordcloud import venn3_wordcloud
from wordcloud import WordCloud
import matplotlib.pyplot as plt

#Conjuntos                  
conjuntoA = {"A", "B", "C", "D", "E"}
conjuntoB = {"B", "G", "J"} 
conjuntoC = {"Z", "D", "X","B"}

#Funcion para realizar la Union entre conjuntos
def diferencia_conjuntos(conjunto1, conjunto2, conjunto3):
    # Paso 1: Calcular la unión de conjunto2 y conjunto3
    union_BC = set(conjunto2)  # Empezar con conjunto2
    for elemento in conjunto3:
        union_BC.add(elemento)  # Añadir los elementos de conjunto3 a la unión
    
    # Paso 2: Calcular la diferencia entre conjunto1 y la unión de conjunto2 y conjunto3
    resultado = set(conjunto1)  # Empezar con conjunto1
    for elemento in union_BC:
        if elemento in resultado:
            resultado.discard(elemento)  # Eliminar los elementos que están en la unión
    
    return resultado


#Realizamos el resultado de la union
difenciaABC = diferencia_conjuntos(conjuntoA, conjuntoB, conjuntoC)
print("Diferencia: ", difenciaABC)

#Creación diagrama de Venn, con está libreria los 
#duplicados se eliminan automaticamente
venn = venn3_wordcloud([conjuntoA, conjuntoB, conjuntoC],
                       ('Conjunto A', 'Conjunto B', 'conjunto C'))
plt.show()

#Creamos una cadena de texto vacia para listar los elementos de la difencia
union_txt = ''.join(difenciaABC)

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