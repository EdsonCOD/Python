print("Busca binaria")

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90]

def busca_binaria(lista, elem):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  #Encontra o meio da lista

        if lista[meio] == elem:
            return meio             #Elemento encontrado
        elif lista[meio] < elem:
            inicio = meio + 1       #Busca na metade direita
        else:
            fim = meio - 1          #Busca na metade esquerda
        
    return None                     #Elemento não encontrado

print(busca_binaria(numeros, 40))

#Mas lembre-se: a busca binária só funciona corretamente se a lista estiver ordenada! 