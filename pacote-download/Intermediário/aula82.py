def executa (funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x + y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

print(
    executa(lambda x, y: x + y, 2, 4)
)

print (
    executa(lambda multiplicador,numero: numero*multiplicador,3, 4)
)

duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print (duplica(4))

print(
    executa(
        lambda *args: sum(args),
        1,3,5,6
    )
)