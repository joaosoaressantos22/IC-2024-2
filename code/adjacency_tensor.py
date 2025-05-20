from auxiliare_functions import calculate_m, calculate_alpha, calculo_pesos, print_permutations, matriz_esparsa

class Hypergraph:
    
    def __init__(self, vetores):
        
        self.lista_de_hiperarestas = vetores 
        self.cardinalidade_maxima = calculate_m(vetores)
        self.aplhas, self.permutacoes = calculate_alpha(vetores, self.cardinalidade_maxima)
        self.lista_de_pesos = calculo_pesos(self.aplhas, vetores)
        self.matriz_esparsa = matriz_esparsa(self.permutacoes, self.lista_de_pesos, self.aplhas)
        # self
        
    def printa_pesos(self):
        print_permutations(self.lista_de_pesos)
    def retorna_matriz_adjacencia(self):
        return NULL
    def retorna_matriz_transformada(self):
        return NULL
    def retorna_plot_hipergrafo(self):
        return NULL