from adjacency_tensor import Hypergraph
import numpy as np

def main():
    np.set_printoptions(suppress=True)
    h = Hypergraph() #Definiçao do hipergrafo 
    print(f"N_ESIMA_FATIA1 = \n{h.primeira_fatia_frontal_laplaciana}\n")
    h.retorna_plot_hipergrafo()
if __name__ == "__main__":
    main()