# reduce - faz a redução de um iterável em um valor

from functools import reduce

produtos =[
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 10},
    {'nome': 'Produto 2', 'preco': 10},
    {'nome': 'Produto 4', 'preco': 69},
]

# def funcao(acumulador, produto):
#     print('acumulador', acumulador)
#     print('produto', produto)
#     return acumulador + produto['preco']

total = reduce(
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print('O total é', total)

# total = 0 
# for p in produtos:
#     total += p['preco']

# print(total)