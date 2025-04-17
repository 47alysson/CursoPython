# Combinations, Permutations e Produtct - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutacao - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator),sep= '\n')
    print()

pessoas = [
    'João', 'Joana','Luiz','Leticia',
]

camisetas = [
    ['Preta', 'Branca'],
    ['p','m','g'],
    ['masculino', 'feminino','unissex'],
    ['poliéster', 'algodão'],
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))
