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
  
  return dict(sorted(matriz_esparsa.items()))

def tensor_de_grau(vetores, cardinalidade_maxima):
    
    dictionary = dict(Counter(x for xs in vetores for x in set(xs)))
    real_dict = {}
    
    for x in dictionary:

        repeated_tuple = (x,) * cardinalidade_maxima
        real_dict[repeated_tuple] = dictionary[x]
        
    return dict(sorted(real_dict.items()))
    
def tensor_laplaciano(tensor_de_grau, tensor_de_adjacencia):

    diff_dict = {}

    for key, value in tensor_de_adjacencia.items():
        if key in tensor_de_grau:

            diff_dict[key] = tensor_de_grau[key] - value
        else:

            diff_dict[key] = -value

    for key, value in tensor_de_grau.items():
        if key not in tensor_de_adjacencia:

            diff_dict[key] = value

    return dict(sorted(diff_dict.items())) 
    
def calculate_quantidade_vertices(vetores):
    total = 0
    for ele in range(0, len(vetores)):  # let's not use "ele" as a var name, btw. confusing
        total = total + vetores[ele]   
    return total

def lista_traduzida(hypergraphs):
    vertices_unicos = sorted(set(v for edge in hypergraphs for v in edge))
    
    mapeamento = {v: i for i, v in enumerate(vertices_unicos)}
    
    hypergraphs_renumerado = [[mapeamento[v] for v in edge] for edge in hypergraphs]
    
    return hypergraphs_renumerado

def print_permutations(p): #Funcao de teste somente
    
    print("[", end="")
    for i, item in enumerate(p):
        print(f"{item:.3f}", end="")
        if i < len(p) - 1:
            print(", ", end="")
        
    print("]")