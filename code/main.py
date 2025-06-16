from adjacency_tensor import Hypergraph
import numpy as np

def main():
    np.set_printoptions(suppress=True)
    h = Hypergraph([[3, 4], [5, 6, 7],  [0, 1, 2]]) #Definiçao do hipergrafo 
    print(f"N_ESIMA_FATIA = {h.primeira_fatia_frontal_laplace()}\nTO_ARRAY = {h.to_array()}")

if __name__ == "__main__":
    main()