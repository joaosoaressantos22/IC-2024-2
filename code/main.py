from adjacency_tensor import Hypergraph

def main():
    h = Hypergraph([[4, 6], [3, 9],  [1, 2, 3]]) #Definiçao do hipergrafo 
    h.printa_pesos()
if __name__ == "__main__":
    main()