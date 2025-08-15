def BuscaMenor(lista):
    menor = lista[0]
    menor_indice = 0

    for i in range(1,len(lista)):
        if lista[i] < menor:
            menor = lista[i]
            menor_indice = i
    return menor_indice
    





def OrdenacaoPorSelacao(lista):
    novaLista = []
    for i in range(len(lista)):
         novoElementoMenor = BuscaMenor(lista)
         novaLista.append(lista.pop(novoElementoMenor))
         
    return novaLista

minha_lista = [12,1100,123,1,4,2]
#print(minha_lista.pop(1))

print(OrdenacaoPorSelacao(minha_lista))


#print(BuscaMenor(minha_lista))