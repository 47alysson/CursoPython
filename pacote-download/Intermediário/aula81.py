# Função lambda em Python
# A função lambda é uma função como qualquer outraa em Python
# Porém, são funções anônimas que contém apenas uma linha
# Ou seja, tudo deve ser contido dentro de uma única expressão.

lista = [
    {'nome': 'Alysson', 'sobrenome': 'Oliveira'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]
# lista = [4,32,1,34,5,6,6,21]
# lista.sort(reverse=True)
# sorted(lista)

# def ordena(item):
#     return item['sobrenome']

def exibir (lista):
    for item in lista:
        print (item)
    print ()

l1 = sorted(lista, key = lambda item: item ['nome'])
l2 = sorted(lista, key = lambda item: item ['sobrenome'])

#exibir(l1)
#exibir(l2)

preco = 1000

calcular_imposto = lambda x:    x * 0.3
                    #recebe     #retorna

precos = [100, 500, 40, 10]

impostos = list(map(lambda x: x*0.3, precos))
print (impostos)

