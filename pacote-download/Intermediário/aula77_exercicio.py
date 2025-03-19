# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta' : 'Quanto é 2+2?',
        'Opções' : ['1','3','4','5'],
        'Resposta' : '4',
    },
    {
        'Pergunta' : 'Quanto é 5*5?',
        'Opções' : ['25','55','10','51'],
        'Resposta' : '25',
    },
    {
        'Pergunta' : 'Quanto é 10/2?',
        'Opções' : ['4','5','2','1'],
        'Resposta' : '5',
    },
]

total = 0

#Pergunta 0
p0 = perguntas[0]
print('Pergunta:',p0.get('Pergunta'))
print()

o0 = perguntas[0].get ('Opções')
r0 = perguntas[0].get ('Resposta')
print('Opções:')
for opcao in o0:
    print(opcao)
print()

resposta = input('Escolha uma opção: ')
if resposta == '3':
    print('Resposta correta 🤙')
    total += 1
else:
    print('Erroooou ❌')
    print('A resposta correta é', r0)

print()
#Pergunta 1
p1 = perguntas[1]
print('Pergunta:',p1.get('Pergunta'))
print()

o1 = perguntas[1].get ('Opções')
r1 = perguntas[1].get ('Resposta')
print('Opções:')
for opcao in o1:
    print(opcao)
print()

resposta = input('Escolha uma opção: ')
if resposta == '1':
    print('Resposta correta 🤙')
    total += 1
else:
    print('Erroooou ❌')
    print('A resposta correta é', r1)

#Pergunta2
p2 = perguntas[2]
print('Pergunta:',p2.get('Pergunta'))
print()

o2 = perguntas[2].get ('Opções')
r2 = perguntas[2].get ('Resposta')
print('Opções:')
for opcao in o2:
    print(opcao)
print()

resposta = input('Escolha uma opção: ')
if resposta == '2':
    print('Resposta correta 🤙')
    total += 1
else:
    print('Erroooou ❌')
    print('A resposta correta é', r2)


print('Você acertou',total,'pergunta(s)')

