print("Inserção da lista")

lista = [10, 20, 30]
lista.append(40)  #Adiciona no final
print(lista)      #Saída : [10, 20, 30, 40]

lista.insert(1,50)  #Adiciona no lugar especifico
print(lista)        #Saída : [10, 15, 20, 30]

lista.extend([40, 50, 60])  #Adiciona vários elementos
print(lista)                #Saída : [10, 20, 30, 40, 50, 60]