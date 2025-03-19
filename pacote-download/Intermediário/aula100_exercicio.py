# copy, sorted, produtos.sort
# Exercícios
# Aumente o preço dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from dados import produtos
from copy import deepcopy

def aumenta_preco(p):
    p = p + (p * 0.1)
    return round(p,2)

novos_produtos = deepcopy(produtos)

novos_produtos = [
    {**p,'preco':aumenta_preco(p['preco'])}
    for p in novos_produtos
]
print('Produtos sem alteração',*produtos, sep='\n')
print()

produtos_ordenados_por_nome = deepcopy(produtos)
print('Ordenados por nome',*sorted(produtos_ordenados_por_nome, key=lambda p: p['nome'], reverse=True),sep='\n')
print()

produtos_ordenados_por_preco = deepcopy(produtos)
print('Ordenados por preco',*sorted(produtos_ordenados_por_preco, key=lambda p: p['preco']),sep='\n')
print()