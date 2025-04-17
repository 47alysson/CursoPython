#Group By - agrupando valores (itertools)

from itertools import groupby

alunos = [
    {'nome': 'Luiz','nota': 'A'},
    {'nome': 'João','nota': 'B'},
    {'nome': 'Maria','nota': 'A'},
    {'nome': 'Leticia','nota': 'C'},
    {'nome': 'Joana','nota': 'B'},
    {'nome': 'Fabrício','nota': 'D'},
    {'nome': 'Eduardo','nota': 'A'},
    {'nome': 'André','nota': 'B'},   
]


def ordena(aluno):
    return aluno['nota']

alunos_agrupados = sorted(alunos, key=ordena)

grupos = groupby(alunos_agrupados, key=ordena)

for chave,grupo in grupos:
    print(chave)
    for aluno in grupo:
        print(aluno)