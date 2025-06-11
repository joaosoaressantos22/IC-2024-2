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

    @staticmethod
    def to_array(tensor):
        
        #Funcionando para 3 dimensões
        #TODO DEIXAR PARA QUALQUER DIMENSÃO 
        #TODO DEIXAR O ARRAY NÃO ESPARSO

        tensor_to_array = [] #Tensor vazio

        _ = (list(tensor.keys()))
        if len(_[0]) > 3:
            return None
        lista_de_chaves = [x[0] for x in _]

        lista_de_chaves = list(dict.fromkeys(lista_de_chaves))
        
        i = 0
        
        lista_para_adicionar = []

        for tupla in tensor:

            if tupla[0] == lista_de_chaves[i]:
                
                lista_para_adicionar.append(tensor[tupla])
            
            else:
                
                tensor_to_array.append(lista_para_adicionar)
                lista_para_adicionar = []
                lista_para_adicionar.append(tensor[tupla])

                i += 1

        tensor_to_array.append(lista_para_adicionar)
            
        return tensor_to_array
        
    def retorna_plot_hipergrafo(self):
        return None