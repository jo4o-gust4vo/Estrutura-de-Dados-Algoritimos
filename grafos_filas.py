from collections import deque


#mapeando o grafo com cidades

grafo = {}

grafo['Belém'] = ['Mosqueiro', 'Marituba']
grafo['Mosqueiro'] = ['Belém','Salinas']
grafo['Marituba'] = ['Belém','Mosqueiro','Santa Maria']
grafo['Santa Maria'] = ['Salinas','Marituba']
grafo['Salinas'] = ['Santa Maria','Mosqueiro']

def pesquisar_cidade(cidade:str):
    fila_cidades_vizinhas = deque()
    fila_cidades_vizinhas += grafo[cidade]
    cidade_verificada = []
    count = 0
    while fila_cidades_vizinhas:
        cidade_vizinha = fila_cidades_vizinhas.popleft()
        cidade_verificada.append(cidade)
        if not cidade_vizinha in cidade_verificada:
            if cidade_vizinha == 'Salinas':
                print('chegou a salinas com caminho mais curto.')
                print('Cidades pecorridas: ',count)
                return True
            else:
                fila_cidades_vizinhas += grafo[cidade_vizinha] 
                cidade_verificada.append(cidade_vizinha) 
                print(cidade_vizinha)
             
        count += 1
    return False

pesquisar_cidade('Belém')