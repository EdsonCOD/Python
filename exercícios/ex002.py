print("Busca linear")
numeros = [10, 20, 30, 40, 50, "9", "café"]

def busca(lista, elem):         #No pior caso, verifica todos os elementos
    for i in range(len(lista)): #Percorre os indices da lista Complexidade O(n)
        if lista[i] == elem:    #Verifica se o elemento na posição i é igual a elem
            return i            #Se encontrar, retorna a posição do elemento    
    return None                 #Se não encontrar retorna None           

print(busca(numeros, 80))
print(busca(numeros,"café"))
print(busca(numeros, "9"))
print(busca(numeros, 9))