def quicksort(lista):
    if len(lista) < 2:
        return lista
    else:
        pivo = lista[0]
        menores = []
        maiores = []
        for i in lista[1:]:
            if i <= pivo:
                menores.append(i)
            else:
                maiores.append(i)
    return quicksort(menores) + [pivo] + quicksort(maiores)



print(quicksort([10,5,2,3,100,5,23,33,40]))