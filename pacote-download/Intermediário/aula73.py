# Higher order functions

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args):
    return funcao(*args)

print(executa(saudacao,'Bom dia', 'Alysson'))
print(executa(saudacao,'Boa noite', 'Joyce'))
