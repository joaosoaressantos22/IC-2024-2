from auxiliare_functions import calculate_m, calculate_alpha, calculo_pesos, print_permutations, tensor_de_adjacencia, tensor_de_grau, tensor_laplaciano, lista_traduzida
import numpy as np 
import networkx as nx
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 

class Hypergraph:
    
    def __init__(self, hypergraphs=[[3, 4], [5],  [0, 1, 2]]):
        

        hypergraphs = lista_traduzida(hypergraphs) #TRADUTOR DA LISTA, PODEM SER STRINGS OU OBJETOS, QUALQUER COISA 
        self.lista_de_hiperarestas = lista_traduzida(hypergraphs)
        self.cardinalidade_maxima = calculate_m(hypergraphs)
        self.aplhas, self.permutacoes = calculate_alpha(hypergraphs, self.cardinalidade_maxima)
        self.lista_de_pesos = calculo_pesos(self.aplhas, hypergraphs)
        self.tensor_de_adjacencia = tensor_de_adjacencia(self.permutacoes, self.lista_de_pesos, self.aplhas)
        self.tensor_de_grau = tensor_de_grau(self.lista_de_hiperarestas, self.cardinalidade_maxima)
        self.tensor_laplaciano = tensor_laplaciano(self.tensor_de_grau, self.tensor_de_adjacencia)
        self.primeira_fatia_frontal_laplaciana = self.primeira_fatia_frontal_laplace()
        self.auto_vetores_fatia_frontal = (np.linalg.eigh(self.primeira_fatia_frontal_laplaciana)[-1])
        self.auto_valores_fatia_frontal = (np.linalg.eigh(self.primeira_fatia_frontal_laplaciana)[0])

    def printa_pesos(self):
        print_permutations(self.lista_de_pesos)

    def tensor_laplace_to_array(self):

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
    

    #TODO ALTERAR PARA O GRAFO VIRAR UM ATRIBUTO DA CLASSE, EVITAR REPETICOES NO GERAL DO SPRING PARA O SPIRAL

    def plot_hipergrafo_spring_layout(self, clusters=3, nx_draw=True):

        spectral_embedding = self.auto_vetores_fatia_frontal[:, :clusters]        
        kmeans = KMeans(n_clusters=clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(spectral_embedding)

        G = nx.Graph()
        for hiperaresta in self.lista_de_hiperarestas:
            for i in range(len(hiperaresta)):
                for j in range(i + 1, len(hiperaresta)):
                    G.add_edge(hiperaresta[i], hiperaresta[j]) #[0, 1, 2] → arestas: (0,1), (0,2), (1,2)

        pos_dict = nx.spring_layout(G, seed=42) #Garante realizará com o spring_layout

        node_order = sorted(G.nodes()) #Ordena 
        node_colors = [cluster_labels[node] for node in sorted(G.nodes())]
        
        pos = np.array([pos_dict[node] for node in node_order])

        plt.figure(figsize=(10, 8))
        if nx_draw != True:
            if spectral_embedding.shape[1] >= 2:
                scatter = plt.scatter(pos[:, 0], 
                                    pos[:, 1], 
                                    c=cluster_labels, 
                                    cmap='viridis',
                                    s=100,
                                    alpha=0.7)
            else:
                scatter = plt.scatter(spectral_embedding[:, 0], 
                                    range(len(spectral_embedding)),
                                    c=cluster_labels,
                                    cmap='viridis',
                                    s=100,
                                    alpha=0.7)

            plt.title(f'Spectral Clustering do Hipergrafo (k={clusters})')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.legend(*scatter.legend_elements(), title="Clusters")
            plt.grid(True, alpha=0.3)
            plt.show()

        else: #MUITO MAIS TRANQUILO DE UTILIAR 

            nx.draw(G, 
            pos, 
            with_labels=True,
            node_color=node_colors,
            cmap=plt.cm.viridis,
            node_size=500,
            edge_color='gray',
            alpha=0.8,
            font_size=10)
            plt.title(f'Spectral Clustering of Hypergraph (k={clusters})')
            plt.grid(True, alpha=0.3)
            plt.show()

    #REPETE O CÓDIGO ANTERIOR, SÓ TROCA DE SPRING PARA SPIRAL
    #TODO EVITAR REPETIÇÕES COMO ESSA PARA A SEMANA QUE VEM, DIMIUIR O TAMANHO DO CÓDIGO QUE JÁ ESTA EXTENSO
    def plot_hipergrafo_spiral_layout(self, clusters=3, nx_draw=True):

        spectral_embedding = self.auto_vetores_fatia_frontal[:, :clusters]        
        kmeans = KMeans(n_clusters=clusters, random_state=42)
        cluster_labels = kmeans.fit_predict(spectral_embedding)

        G = nx.Graph()
        for hiperaresta in self.lista_de_hiperarestas:
            for i in range(len(hiperaresta)):
                for j in range(i + 1, len(hiperaresta)):
                    G.add_edge(hiperaresta[i], hiperaresta[j]) #[0, 1, 2] → arestas: (0,1), (0,2), (1,2)

        pos_dict = nx.spiral_layout(G) #Garante realizará com o spiral_layout

        node_order = sorted(G.nodes()) #Ordena 
        node_colors = [cluster_labels[node] for node in sorted(G.nodes())]
        pos = np.array([pos_dict[node] for node in node_order])

        plt.figure(figsize=(10, 8))
        if nx_draw != True:
            if spectral_embedding.shape[1] >= 2:
                scatter = plt.scatter(pos[:, 0], 
                                    pos[:, 1], 
                                    c=cluster_labels, 
                                    cmap='viridis',
                                    s=100,
                                    alpha=0.7)
            else:
                scatter = plt.scatter(spectral_embedding[:, 0], 
                                    range(len(spectral_embedding)),
                                    c=cluster_labels,
                                    cmap='viridis',
                                    s=100,
                                    alpha=0.7)

            plt.title(f'Spectral Clustering do Hipergrafo (k={clusters})')
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.legend(*scatter.legend_elements(), title="Clusters")
            plt.grid(True, alpha=0.3)
            plt.show()

        else:
            nx.draw(G, 
            pos, 
            with_labels=True,
            node_color=node_colors,
            cmap=plt.cm.viridis,
            node_size=500,
            edge_color='gray',
            alpha=0.8,
            font_size=10)
            plt.title(f'Spectral Clustering of Hypergraph (k={clusters})')
            plt.grid(True, alpha=0.3)
            plt.show()