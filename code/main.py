from hypergraph import Hypergraph
import numpy as np

def main():
                        #0      1       2       3               0   2       2       0       1           3           4
    h = Hypergraph([[1,2,3], [3,4, 5], [5,6,7], [1, 2]])#Funcional utilizando o tradutor 
    print(h.primeira_fatia_frontal_laplaciana)
    h.plot_hipergrafo_spiral_layout()
    h.plot_hipergrafo_spring_layout()    

if __name__ == "__main__":
    main()
