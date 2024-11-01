
from matplotlib import pyplot as plt
from itertools import permutations, product, combinations_with_replacement
import numpy as np

def calculate_m(vetores):
    max = 0
    for n in vetores:
        if (len(n) > max):
            max = len(n)
    return max

def calculate_alpha(vetores, m):
    print(m)
    pos = 0
    values = [None]*len(vetores)
    for n in vetores:
        if (m == len(n)):
            values[pos] = len(list(permutations(n))) 
            print_permutations(list(permutations(n))) 
        else:
            newArray = n
            for j in range((m - len(n))):
                newArray = np.append(newArray, newArray[j])
            #print(len(list(permutations(newArray))))
            values[pos] = len(list(permutations(newArray)))
            print_permutations(list(permutations(newArray))) 
            print("SAIU! {}\n")
            print(values[pos])
        pos+= 1
    return values


def calculate_permutations(*lista, m):
    values = [None]*m
    
def print_permutations(p):
    for i in list(p):
        print(i)

v1 = np.array([1,2, 7])
v4 = np.array([3, 6, 5, 4])
vetores = [v1, v4]
m = calculate_m(vetores)
alfas = calculate_alpha(vetores, m)