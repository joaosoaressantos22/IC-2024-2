from itertools import permutations, product, combinations_with_replacement

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


def calculate_alpha(vetores, m): #Adiciono posteriormente o retorno da lista das permutações dos termos

    pos = 0

    values = [0]*len(vetores)

    for n in vetores:

        if (m == len(n)):

            values[pos] = len(list(unique_permutations(n))) 
            #print_permutations(unique_permutations(n))

        else: 
            count = m - len(n) #Quanto que um termo tem que se repetir 

            for elementos_adicionados in combinations_with_replacement(n, count): # Gera todas as permutacoes dos elementos com repeticao de n - count elementos
                
                newArray = n + list(elementos_adicionados)

                #print("\n")
                values[pos] += len(list(unique_permutations(newArray)))
                # print(values[pos])
                #print(values[pos])
                perm = unique_permutations(newArray) 
                #print_permutations(perm)
                #print("\n")

                

        pos+= 1

    return values
    
def print_permutations(p): #Funcao de teste somente
    
    print("[", end="")
    for i, item in enumerate(p):
        print(f"{item:.3f}", end="")
        if i < len(p) - 1:
            print(", ", end="")
        
    print("]")