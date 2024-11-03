
from matplotlib import pyplot as plt
from itertools import permutations, product, combinations_with_replacement
import numpy as np


def calculate_m(vetores): #Funcionando
    maiorLength = max([len(vetores[i]) for i in range(len(vetores))])
    return maiorLength

def unique_permutations(lst): #Só garante que a lista nao vai ter elementos repetidos, exemplo [1,1] e [1,1]

    perm_set = set(permutations(lst))

    return [list(p) for p in perm_set]

def calculo_pesos(alfas, vetores): #Funcionando
    pesos = [0]*len(vetores)
    l = 0
    for i in range (len(vetores)):
        pesos[l] = (len(vetores[i])/alfas[i])
        l+= 1
    return pesos


def calculate_alpha(vetores, m):

    pos = 0

    values = [0]*len(vetores)

    for n in vetores:

        if (m == len(n)):

            values[pos] = len(list(unique_permutations(n))) 

        else:

            for l in range (len(n)):
                
                newArray = n.copy()

                for j in range((m - len(n))):
                    
                    newArray.append(newArray[l]) #Bugs aqui!

                print_permutations(unique_permutations(newArray))

                values[pos] += len(list(unique_permutations(newArray)))

        pos+= 1

    return values
    
def print_permutations(p): #Funcao de teste somente
    for i in list(p):
        print(i)

v1 = [7, 2, 3]

v4 = [3, 6, 5, 4]

vetores = [v1, v4]

m = calculate_m(vetores)

alfas = calculate_alpha(vetores, m)

pesos = calculo_pesos(alfas, vetores)
