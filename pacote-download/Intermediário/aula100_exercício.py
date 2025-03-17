# copy, sorted, produtos.sort
# Exercícios
# Aumente o preço dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
produtos = [
    {'nome':'Produto 5','preco':10.00},
    {'nome':'Produto 1','preco':22.32},
    {'nome':'Produto 3','preco':10.11},
    {'nome':'Produto 2','preco':105.87},
    {'nome':'Produto 4','preco':69.90},
]

# Ordene os produtos por nome decrescente (do maior para o menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para o maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

from copy import deepcopy

def aumenta_preco(p):
    p = p + (p * 0.1)
    return round(p,2)

novos_produtos = deepcopy(produtos)

novos_produtos = [
    {**produto,'preco':aumenta_preco(produto['preco'])}
    for produto in novos_produtos    
]

print(novos_produtos)
