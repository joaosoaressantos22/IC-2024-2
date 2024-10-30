
from matplotlib import pyplot as plt
from itertools import permutations
from itertools import product
import numpy as np

def calculate_m(vetores):
    max = 0
    for n in vetores:
        if (len(n) > max):
            max = len(n)
    return max

def calculate_alpha(vetores, m):
    pos = 0
    values = [None]*len(vetores) #Copia os valores do tensor de vetores em uma lista
    for n in vetores:
        if (m == len(n)):
            values[pos] = len(list(permutations(n)))
        else:
            values[pos] = (len(list(product(n, repeat=m))) - len(n)) #Ainda a trabalhar quando o M é igual a 4 com 3 está dando o dobro
        pos+= 1
    return values
    
v1 = np.array([1,2])
v2 = np.array([1,2])
v3 = np.array([1, 3, 4, 5])
v4 = np.array([1, 2, 3])
v5 = np.array([1, 2, 3])
vetores = [v1, v2, v3, v4, v5]
m = calculate_m(vetores)
alfas = calculate_alpha(vetores, m)
for i in range(len(alfas)):
    print(alfas[i])