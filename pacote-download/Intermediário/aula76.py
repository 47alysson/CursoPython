# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo par de "chave" e "valor".
# Chaves podem ser consideradas como "índice" que vimos na lista e podem ser de tipos imutáveis
# Como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro dicionário.
# Usamos as chaves - {} - ou a classe dict para criar dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list

#pessoa = {
#   'nome': 'Luiz Otávio',
#   'sobrenome': 'Miranda',
#   'idade': 18,
#   'altura': 1.8,
#   'enderecos':[
#       {'rua': 'tal tal', 'numero':123},
#       {'rua': 'outra rua', 'numero':321},
#   ]
#}

pessoa = {
    'Nome:': 'Alysson',
    'Sobrenome:':'Oliveira',
    'Idade:': 25,
    'Altura:': 1.80,
    'Endereços:': [
        {'Rua': 'Caetano Motta', 'Numero': 390},
        {'Rua': 'Domingos Macera', 'Numero': 330},
    ],
}
# print(pessoa, type(pessoa))

# print(pessoa['idade'])
for chave in pessoa:
    print(chave, pessoa[chave])
