def pesquisaBinaria(lista,item):
    baixo = 0
    alto = len(lista) -1

    while baixo <= alto:
        meio = (baixo + alto)/2
        chute = lista[int(meio)]

        if chute == item:
            return meio                        
        if chute > item:
            alto = meio -1
        else:
            baixo = meio + 1
    return None


minha_lista = [1,3,4,5,6,7,8,9,10,11,12]

pesquisaBinaria(minha_lista, 3)
