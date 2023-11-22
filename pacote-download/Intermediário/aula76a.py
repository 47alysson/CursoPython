# Manipulando chaves e valores em dicionários
pessoa = {}

chave = 'nome_completo'

pessoa[chave] = 'Alysson Oliveira'
pessoa['sobrenome'] = 'Gonçalves'


print(pessoa[chave])

pessoa[chave] = 'Joyce'

# del pessoa['sobrenome']

print(pessoa)

# print(pessoa.get('sobrenome', 'Não existe'))

if pessoa.get('sobrenome') is None:
    print('Não existe')

else:
    print(pessoa['sobrenome'])
