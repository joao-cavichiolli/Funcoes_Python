## Funções kwargs 
# passar um numero indeterminado de parametros
# para uma função. MAs diferente do arg voce precisa
# passar nos argumento identificador de chaves e valores

def saudacoes(**kwargs):
    print(kwargs)

saudacoes(manha='bom dia',tarde='boa tarde')

def saudacao_dia(**kwargs):
    for periodo_dia,saudacao in kwargs.items():
        print(f'Durante a {periodo_dia} dizemos {saudacao}') #fstrings

## Chamar a função

saudacao_dia(manha='bom dia',tarde='boa tarde',noite='boa noite',madrugada='vai dormiii')