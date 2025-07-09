from adjacency_tensor import Hypergraph
import numpy as np

def main():
                        #0      1       2       3               0   2       2       0       1           3           4
    h = Hypergraph([[0,1,2], [3,4,5], [6,7,8]]) #Funcional utilizando o tradutor 
    print(h.tensor_de_adjacencia)
    print(h.tensor_adjacencia_to_array())
    
if __name__ == "__main__":
    main()
