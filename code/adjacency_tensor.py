from auxiliare_functions import calculate_m, calculate_alpha, calculo_pesos, print_permutations, tensor_de_adjacencia, tensor_de_grau, tensor_laplaciano
import numpy as np 

class Hypergraph:
    
    def __init__(self, vetores):
        
        self.lista_de_hiperarestas = vetores 
        self.cardinalidade_maxima = calculate_m(vetores)
        self.aplhas, self.permutacoes = calculate_alpha(vetores, self.cardinalidade_maxima)
        self.lista_de_pesos = calculo_pesos(self.aplhas, vetores)
        self.tensor_de_adjacencia = tensor_de_adjacencia(self.permutacoes, self.lista_de_pesos, self.aplhas)
        self.tensor_de_grau = tensor_de_grau(self.lista_de_hiperarestas, self.cardinalidade_maxima)
        self.tensor_laplaciano = tensor_laplaciano(self.tensor_de_grau, self.tensor_de_adjacencia)
        self.tensor_laplaciano_array = self.to_array()

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
    
    #TODO CONSERTAR ESSA FUNCAO 
    
    def primeira_fatia_frontal_laplace(self):
        print(self.tensor_laplaciano)
        keys = list(self.tensor_laplaciano.keys())

        total_len = (keys[-1][-1]) + 1
        nesima_fatia = np.zeros((total_len, total_len))
        key_atual = 0

        while key_atual <= (total_len + 1):

            for key in keys:

                if key[-1] == key_atual:

                    nesima_fatia[key_atual, key_atual] += self.tensor_laplaciano[key]

            key_atual += 1

        return nesima_fatia

    
    def retorna_plot_hipergrafo(self):
        return None
    