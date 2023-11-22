'''Métodos úteis dos dicionários em python
len - quantas chaves
keys - iteráveis com as chaves
values - iteráveis com valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item coma  chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
'''

pessoa = {
    'nome':'Alysson Silva',
    'sobrenome':'Oliveira',
    'idade': 25,
}
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# pessoa.setdefault('idade',None)
# print(pessoa['idade'])

