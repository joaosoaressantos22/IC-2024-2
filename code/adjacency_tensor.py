from auxiliare_functions import calculate_m, calculate_alpha, calculo_pesos, print_permutations, tensor_de_adjacencia, tensor_de_grau, tensor_laplaciano
import numpy as np 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 

class Hypergraph:
    
    def __init__(self, hypergraphs=[[3, 4], [5],  [0, 1, 2]]):
        
        self.lista_de_hiperarestas = hypergraphs 
        self.cardinalidade_maxima = calculate_m(hypergraphs)
        self.aplhas, self.permutacoes = calculate_alpha(hypergraphs, self.cardinalidade_maxima)
        self.lista_de_pesos = calculo_pesos(self.aplhas, hypergraphs)
        self.tensor_de_adjacencia = tensor_de_adjacencia(self.permutacoes, self.lista_de_pesos, self.aplhas)
        self.tensor_de_grau = tensor_de_grau(self.lista_de_hiperarestas, self.cardinalidade_maxima)
        self.tensor_laplaciano = tensor_laplaciano(self.tensor_de_grau, self.tensor_de_adjacencia)
        self.tensor_laplaciano_array = self.to_array()
        self.primeira_fatia_frontal_laplaciana = self.primeira_fatia_frontal_laplace()
        self.auto_vetores_fatia_frontal = (np.linalg.eigh(self.primeira_fatia_frontal_laplaciana)[-1])
        self.auto_valores_fatia_frontal = (np.linalg.eigh(self.primeira_fatia_frontal_laplaciana)[0])

    def printa_pesos(self):
        print_permutations(self.lista_de_pesos)
        
    def retorna_tensor_de_adjacencia(self):
        return self.tensor_de_adjacencia
    
    def retorna_tensor_laplaciano(self):
        return self.tensor_laplaciano
    
    def to_array(self):

        _ = (list(self.tensor_laplaciano.keys()))

        lista_de_chaves = [x[0] for x in _]

        tupla_para_array = tuple([lista_de_chaves[-1]] * self.cardinalidade_maxima)

        to_array = (np.zeros(tupla_para_array)) 

        for key in self.tensor_laplaciano.keys():

            key_check = tuple(x - 1 for x in key)
            to_array[key_check] = self.tensor_laplaciano[key]

        return to_array
    
    def primeira_fatia_frontal_laplace(self):

        keys = list(self.tensor_laplaciano.keys())
    
        total_len = (keys[-1][-1]) + 1
    
        nesima_fatia = np.zeros((total_len, total_len))

        for key in keys:
            
            nesima_fatia[key[0], key[1]] += self.tensor_laplaciano[key]
        return nesima_fatia
    

    #TODO ENTENDER MELHOR ESSA FUNCAO, FAZER ALGUMAS ALTERACOES FUTURAS 
    def retorna_plot_hipergrafo(self, clusters=3):
        
        keys = list(self.tensor_laplaciano.keys())
        
        total_len = (keys[-1][-1]) + 1
        inertias = [] 
        for i in range(1, total_len):
            kmeans = KMeans(n_clusters=i)
            kmeans.fit(self.auto_vetores_fatia_frontal)
            inertias.append(kmeans.inertia_)
        
        plt.plot(range(1, total_len), inertias, marker='o')
        plt.title('Elbow method')
        plt.xlabel('Number of clusters')
        plt.ylabel('Inertia')
        plt.show() 