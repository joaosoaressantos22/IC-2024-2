from adjacency_tensor import Hypergraph

def main():
    h = Hypergraph([[4, 6], [9],  [1, 2, 3]]) #Definiçao do hipergrafo 
        # h.printa_pesos()
    print(f"Tensor de grau é: {h.tensor_de_grau}")
    print(f"Tensor de adjacência é {h.tensor_de_adjacencia}")
    print(f"Tensor laplaciano é: {h.tensor_laplaciano}")
    
if __name__ == "__main__":
    main()