def contador(lista:list):
    if lista == []:
        return 0
    return 1 + contador(lista[1:])



elementos = [11312, 1312, 13123,13153463,1,5,7]


print(contador(elementos))


