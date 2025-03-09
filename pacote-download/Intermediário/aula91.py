# Introdução às Generator functions em Python
# generator = (n for n in range (1000000))

# def generator(n=0):
#     yield 1 #Pausa
#     print('Continuando...')
#     yield 2 #Pausa
#     print('Denovo...')
#     yield 3 #Pausa
#     print('Terminar')
#     return 'Acabou'

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return print('Fim')

gen = generator(n=5, maximum=8)
for n in gen:
    print(n)