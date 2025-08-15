def pesquisaBinaria(lista,item):
    baixo = 0
    alto = len(lista) -1

    while baixo <= alto:
        meio = (baixo + alto)/2
        chute = lista[int(meio)]

        if chute == item:
            return print('Numero localizado')                        
        if chute > item:
            alto = meio -1
            print('Numero não localizado') 
        else:
            baixo = meio + 1
            print('Numero não localizado') 
    return None


minha_lista = [1,2,3,4]

pesquisaBinaria(minha_lista, 3)
  