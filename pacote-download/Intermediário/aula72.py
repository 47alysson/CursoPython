# Exercícios com funções
# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável


def mult(*args):
    total = 1

    for numero in args:
        total *= numero
        
    return total

mult1 = mult(6,5,5,6)
print(mult1)


# Crie uma função que fala se um número é par ou ímpar
# Retorne se o número é par ou ímpar

def multiplo(x):
    if x%2 == 0:
        return print(f'O número {x} é Par')
    return print(f'O número {x} é ímpar')

numero = int(input('Digite um número: '))

multiplo(numero)
