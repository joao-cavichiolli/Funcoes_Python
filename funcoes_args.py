## Funções *args são utilizadas quando não sabemos o numero
# de argumentos necessários em uma função
# Deixamos isso flexivel em aberto
# O retorno ou saida dessa função retorna uma tupla

def soma(*args):
    print(args)

soma(1,3,2,42,1,2,53,12,2,343,23,312,1,2,123,5454,6,565)


def soma_total(*args):
    total = 0
    for n in args:
        total = n+total
    return total

print(soma_total(1,3,7,5,10,6,3,6,3,1,2,6))



