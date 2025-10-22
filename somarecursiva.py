elementos = [3,2,1,1,4,6,8,64]



def soma(lista):
   if lista == []:
        return 0
   print(lista[0])
   print(lista[1:])
   return lista[0] + soma(lista[1:])


soma(elementos)


