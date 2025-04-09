print("Inserção da lista")

lista = [10, 20, 30, 20, 40, 50]
print(lista)
lista.remove(20)    #Remove apenas o primeiro 20 encontrado
print(lista)        #Saída : [10, 30, 20, 40]

if 100 in lista:
    lista.remove(100)  #Se o elemento não estiver na lista, dá erro:
    print(lista)       #Então, é bom verificar antes

removido = lista.pop(2)  #Remove o elemento pelo indice
print(lista, end=" ")
print("Removido {}".format(removido))


del lista[3]  #Remove o elemento no indice
print(lista, end=" ")
print("Removido {}".format(50))


