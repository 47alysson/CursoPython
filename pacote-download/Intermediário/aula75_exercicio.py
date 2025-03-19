'''Crie funções que duplicam, triplicam e quadruplicam o número recebido como parâmetro'''

def multiplicar(multiplo):
    def multi (numero):
        return numero * multiplo
    return multi

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
