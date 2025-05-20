from itertools import permutations, product, combinations_with_replacement
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

def matriz_esparsa(tuplas_permutadas, pesos, alfas):
  
  # print(tuplas_permutadas)
  
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
  
  return matriz_esparsa

def print_permutations(p): #Funcao de teste somente
    
    print("[", end="")
    for i, item in enumerate(p):
        print(f"{item:.3f}", end="")
        if i < len(p) - 1:
            print(", ", end="")
        
    print("]")