from adjacency_tensor import Hypergraph

def main():
    h = Hypergraph([[4, 6], [5],  [1, 2, 3]]) #Definiçao do hipergrafo 
    #print(f"Tensor de grau é: {h.tensor_de_grau}")
    #print(f"Tensor de adjacência é {h.tensor_de_adjacencia}")
    #print(f"Tensor laplaciano é: {h.tensor_laplaciano}")

    print(h.to_array(h.tensor_de_adjacencia))

if __name__ == "__main__":
    main()