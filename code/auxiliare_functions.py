from itertools import permutations, product, combinations_with_replacement
from collections import Counter
from math import factorial

def calculate_m(vetores): #Funcionando
    maiorLength = max([len(vetores[i]) for i in range(len(vetores))])
    return maiorLength

def unique_permutations(lst):

    return tuple(set(permutations(lst)))

def calculo_pesos(alfas, vetores): #Funcionando

    pesos = [0]*len(vetores)
    l = 0
    for i in range (len(vetores)):
        pesos[l] = (len(vetores[i])/alfas[i])
        l+= 1
    return pesos


def calculate_alpha(vetores, m): #Adiciono posteriormente o retorno da lista das permutações dos termos

    pos = 0

    values = [0]*len(vetores)
    
    lista_de_permutacoes = []

    permutacoes = ()

    for n in vetores:

        if (m == len(n)):

            values[pos] = len(list(unique_permutations(n))) 
            lista_de_permutacoes.append(unique_permutations(n))

        else: 
            count = m - len(n) #Quanto que um termo tem que se repetir 

            for elementos_adicionados in combinations_with_replacement(n, count): # Gera todas as permutacoes dos elementos com repeticao de n - count elementos
                
                newArray = n + list(elementos_adicionados)
                values[pos] += len(list(unique_permutations(newArray)))
                lista_de_permutacoes.append(unique_permutations(newArray))

        pos+= 1

    return values, tuple(lista_de_permutacoes)

def tensor_de_adjacencia(tuplas_permutadas, pesos, alfas):
    
  matriz_esparsa = {}
  
  j = 0
  
  combinacoes_atuais = 0
  
  for item in tuplas_permutadas:
  
    combinacoes_atuais += len(item) #UM ITEM MENOR QUE TEM QUE IR SOMANDO ATÉ BATER O NEGOCIO

    for tupla in item:
  
      matriz_esparsa[tupla] = "{:.5f}".format(pesos[j])
  
    if combinacoes_atuais == alfas[j]:
      
      j += 1
  
      combinacoes_atuais = 0
  
  matriz_esparsa = {k: float(v) for k, v in matriz_esparsa.items()} 
  
  return matriz_esparsa

def tensor_de_grau(vetores, cardinalidade_maxima):
    
    dictionary = dict(Counter(x for xs in vetores for x in set(xs)))
    
    real_dict = {}
    
    for x in dictionary:
        string_to_change = (str(x)*cardinalidade_maxima)
        real_dict[tuple(int(digit) for digit in string_to_change)] = dictionary[x]
        
    return dict(sorted(real_dict.items()))
    
def tensor_laplaciano(tensor_de_grau, tensor_de_adjacencia):

    diff_dict = {}
    #2 - 1
    for key, value in tensor_de_adjacencia.items():
        if key in tensor_de_grau:

            diff_dict[key] = tensor_de_grau[key] - value
        else:

            diff_dict[key] = -value

    for key, value in tensor_de_grau.items():
        if key not in tensor_de_adjacencia:

            diff_dict[key] = value

    return diff_dict 
    
def print_permutations(p): #Funcao de teste somente
    
    print("[", end="")
    for i, item in enumerate(p):
        print(f"{item:.3f}", end="")
        if i < len(p) - 1:
            print(", ", end="")
        
    print("]")