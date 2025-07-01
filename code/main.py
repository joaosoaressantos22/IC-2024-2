from adjacency_tensor import Hypergraph
import numpy as np

def main():
    np.set_printoptions(suppress=True)
    h = Hypergraph([[0,1,2],[4,5,3], [6,7,8,9], [10, 11]]) #Definiçao do hipergrafo Por algum motivo funciona até 11
    print(f"N_ESIMA_FATIA1 = \n{h.primeira_fatia_frontal_laplaciana}\n")
    h.retorna_plot_hipergrafo()
if __name__ == "__main__":
    main()
