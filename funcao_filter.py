## Função filter ela filtra um valor de uma estrutura de dados

lista1 = [1,"João",67,"Pedro",78.31]
listanum = [1,5,67,100]

def busca(x):
    return x < 67


print(list(filter(busca,listanum)))


##  Otimizando a busca utilizando lambda

print(list(filter(lambda x: x=="Pedro",lista1)))