from adjacency_tensor import Hypergraph
import numpy as np

def main():
                        #0      1       2       3               0   2       2       0       1           3           4
    h = Hypergraph([["Joao", "Aline", "Ana"], ["Alcebiades","Joao","Ana"], ["Maria","Joana","Aline"], ["Alcebiades","Fabiano"]]) #Funcional utilizando o tradutor 
    h.plot_hipergrafo_spiral_layout()
    h.plot_hipergrafo_spring_layout()

if __name__ == "__main__":
    main()
