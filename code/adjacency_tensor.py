from auxiliare_functions import calculate_m, calculate_alpha, calculo_pesos, print_permutations, tensor_de_adjacencia, tensor_de_grau, tensor_laplaciano

class Hypergraph:
    
    def __init__(self, vetores):
        
        self.lista_de_hiperarestas = vetores 
        self.cardinalidade_maxima = calculate_m(vetores)
        self.aplhas, self.permutacoes = calculate_alpha(vetores, self.cardinalidade_maxima)
        self.lista_de_pesos = calculo_pesos(self.aplhas, vetores)
        self.tensor_de_adjacencia = tensor_de_adjacencia(self.permutacoes, self.lista_de_pesos, self.aplhas)
        self.tensor_de_grau = tensor_de_grau(self.lista_de_hiperarestas, self.cardinalidade_maxima)
        self.tensor_laplaciano = tensor_laplaciano(self.tensor_de_grau, self.tensor_de_adjacencia)
        
    def printa_pesos(self):
        print_permutations(self.lista_de_pesos)
        
    def retorna_tensor_de_adjacencia(self):
        return self.tensor_de_adjacencia
    
    def retorna_tensor_laplaciano(self):
        return self.tensor_laplaciano
    def retorna_plot_hipergrafo(self):
        return None