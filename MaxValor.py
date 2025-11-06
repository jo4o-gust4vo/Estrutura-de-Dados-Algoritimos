def MaxValor(lista: list):
    

    if lista == []:
        return 'lista vazia'
    
    if len(lista) == 1:
        return lista[0]
    
    if len(lista) == 2:
        return lista[0] if lista[0] > lista[1] else lista[1]
    
        
    sub_max = MaxValor(lista[1:])
    return lista[0] if lista[0] > sub_max else sub_max
    

    

print(MaxValor([2,1,4,5,0,7]))

minha_lista = [1,2,3]

print(minha_lista[1:])

    

