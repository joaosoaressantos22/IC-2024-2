from adjacency_tensor import Hypergraph

def main():
    h = Hypergraph([[4, 6, 3, 9], [3, 9, 5],  [1, 2, 3, 7, 8]]) #Definiçao do hipergrafo 
    h2 = Hypergraph([[1, 2, 5], [2, 4],  [4, 6]])
    h.printa_pesos()
    h2.printa_pesos()
    
if __name__ == "__main__":
    main()